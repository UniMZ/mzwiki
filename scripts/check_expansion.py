#!/usr/bin/env python3
"""Recompute four supplied expansion fixture sets; verify exact authored sources."""
from collections import Counter
from decimal import Decimal as D, ROUND_HALF_UP
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from statistics import median
import ast
import hashlib
import json
import re
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
failures=[]
def check(ok,label):
 if not ok:failures.append(label)
def read(path):return json.loads((ROOT/path).read_text(),parse_float=D)
def equal(a,b):
 if isinstance(b,dict):return isinstance(a,dict) and set(a)==set(b) and all(equal(a[k],v) for k,v in b.items())
 if isinstance(b,list):return len(a)==len(b) and all(equal(x,y) for x,y in zip(a,b))
 if isinstance(b,bool):return a is b
 if isinstance(b,(int,D)):return abs(D(a)-D(b))<=D('1e-12')
 return a==b
def rank(rows):
 a=[[Fraction(x) for x in row] for row in rows];r=0
 for col in range(len(a[0])):
  pivot=next((j for j in range(r,len(a)) if a[j][col]),None)
  if pivot is None:continue
  a[r],a[pivot]=a[pivot],a[r];scale=a[r][col];a[r]=[x/scale for x in a[r]]
  for j in range(len(a)):
   if j!=r:
    scale=a[j][col];a[j]=[x-scale*y for x,y in zip(a[j],a[r])]
  r+=1
 return r

def arithmetic(expression,values):
 def visit(n):
  if isinstance(n,ast.Expression):return visit(n.body)
  if isinstance(n,ast.Constant) and isinstance(n.value,(int,float)):return D(str(n.value))
  if isinstance(n,ast.Name):return D(values[n.id])
  if isinstance(n,ast.BinOp):
   a,b=visit(n.left),visit(n.right)
   if isinstance(n.op,ast.Add):return a+b
   if isinstance(n.op,ast.Sub):return a-b
   if isinstance(n.op,ast.Mult):return a*b
   if isinstance(n.op,ast.Div):return a/b
  raise ValueError('Unsupported fixture expression')
 return visit(ast.parse(expression,mode='eval'))

sep=read('tests/fixtures/separation.json');assert len(sep['fixtures'])==11
for c in sep['fixtures']:
 for calc in c['calculations']:check(equal(arithmetic(calc['formula'],c['inputs']),calc['expected']),c['id']+': '+calc['formula'])
 if not c['calculations']:
  values=c['inputs']['post_challenge_blanks'];check(all(a>b for a,b in zip(values,values[1:])) and values[-1]>c['inputs']['pre_challenge_blank'],c['id'])
 for lang in ('en','zh'):
  body=(ROOT/f'content/{lang}/{c["article"]}.html').read_text();check(f'id="{c["section"]}"' in body,c['id']+': published anchor')

quant=read('tests/fixtures/quantification-design-qc.json');assert len(quant['cases'])==13
for c in quant['cases']:
 i=c['input'];k=c['kind']
 if k=='calibration':
  slope=i['slope_ml_ng'];intercept=i['intercept'];measured=(i['unknown_response']-intercept)/slope;wrong=i['unknown_response']/slope
  o=dict(responses=[intercept+slope*x for x in i['concentrations_ng_ml']],measured_solution_ng_ml=measured,original_sample_ng_ml=measured*i['dilution_factor'],zero_intercept_ng_ml=wrong,zero_intercept_relative_error_percent=100*(wrong-measured)/measured)
 elif k=='lower_limits':o=dict(dl_ng_ml=i['dl_multiplier']*i['response_sd']/i['slope_ml_ng'],ql_ng_ml=i['ql_multiplier']*i['response_sd']/i['slope_ml_ng'])
 elif k=='reference_difference':
  mean=sum(i['measurements_ng_ml'])/len(i['measurements_ng_ml']);difference=mean-i['reference_ng_ml'];o=dict(mean_ng_ml=mean,mean_minus_reference_ng_ml=difference,relative_difference_percent=100*difference/i['reference_ng_ml'])
 elif k=='replicates':o=dict(preparations=i['donors']*i['preparations_per_donor'],injections=i['donors']*i['preparations_per_donor']*i['injections_per_preparation'],donor_level_units=i['donors'])
 elif k=='matrix_rank':
  batches=sorted(set(i['batch']));rows=[[1,c]+[int(b==v) for v in batches[1:]] for c,b in zip(i['condition'],i['batch'])];r=rank(rows);o=dict(columns=len(rows[0]),rank=r)
  if 'independent_units' in c['expected']:o.update(independent_units=len(rows),units_per_condition=i['condition'].count(1));assert i['condition'].count(0)==i['condition'].count(1)
  else:o['separate_effects_identifiable']=r==len(rows[0])
 elif k=='paired_changes':
  ratios=[D(a)/b for a,b in zip(i['after'],i['before'])];changes=[a-b for a,b in zip(i['after'],i['before'])];o=dict(ratios=ratios,log2_ratios=[x.ln()/D(2).ln() for x in ratios],absolute_changes=changes,mean_absolute_change=D(sum(changes))/len(changes),donors=len(changes))
 elif k=='drift':
  predicted=D(i['qc_responses'][0])+D(i['sample_position']-i['qc_positions'][0])*(i['qc_responses'][1]-i['qc_responses'][0])/(i['qc_positions'][1]-i['qc_positions'][0]);o=dict(predicted_qc_response=predicted,corrected_response=D(i['sample_response'])*i['reference_response']/predicted)
 elif k=='median_scaling':
  ma,mb=D(median(i['sample_a'])),D(median(i['sample_b']));factor=ma/mb;scaled=[x*factor for x in i['sample_b']];o=dict(median_a=ma,median_b=mb,factor=factor,scaled_b=scaled,raw_ratios=[D(b)/a for a,b in zip(i['sample_a'],i['sample_b'])],scaled_ratios=[b/a for a,b in zip(i['sample_a'],scaled)])
 elif k=='cv':
  values=i['qc_responses'];mean=D(sum(values))/len(values);sd=(sum((x-mean)**2 for x in values)/(len(values)-1)).sqrt();assert i['sd_divisor']=='n-1';o=dict(mean=mean,sample_sd=sd,cv_percent=100*sd/mean)
 elif k=='is_ratio':o=dict(ratios=[D(a)/s for a,s in zip(i['analyte'],i['standard'])],analyte_multiplier=D(i['analyte'][1])/i['analyte'][0],standard_multiplier=D(i['standard'][1])/i['standard'][0])
 elif k=='dilution_limit':o=dict(original_sample_loq_ng_ml=i['measured_solution_loq_ng_ml']*i['dilution_factor'])
 else:
  assert k=='multiplicative_ambiguity';ratios=[a*b for a,b in zip(i['biological_multipliers'],i['batch_multipliers'])];o=dict(predicted_group_ratios=ratios,effects_separable_from_group_means=len(set(ratios))!=1)
 check(equal(o,c['expected']),c['id']+': '+str(o))
for c in quant['published_checks']:
 body=(ROOT/c['file']).read_text()
 for value in c['required_strings']:check(value in body,c['file']+': '+value)

prot=read('tests/fixtures/proteomics.json');assert len(prot['cases'])==12
for c in prot['cases']:
 k=c['id']
 if k=='prot-digestion-rule':
  seq=c['sequence'];cuts=[n+1 for n,a in enumerate(seq[:-1]) if a in 'KR' and seq[n+1]!='P'];bounds=[0]+cuts+[len(seq)];products=[seq[a:b] for a,b in zip(bounds,bounds[1:])]
  check(cuts==c['eligible_internal_cleavage_after_positions'],k+': computed cleavage positions '+str(cuts))
  check(products==c['complete_products'] and ''.join(products)==c['one_missed_cleavage_product'] and len(cuts)==c['missed_cleavage_count'],k+': products')
 elif k=='prot-recovery-ratio':
  values=[a*b for a,b in zip(c['starting_amounts'],c['recovery_fractions'])];check(values==c['recovered_amounts'] and D(c['starting_amounts'][0])/c['starting_amounts'][1]==c['starting_ratio'] and values[0]/values[1]==c['measured_ratio_with_equal_downstream_response'],k)
 elif k=='prot-variable-site-count':check(c['states_per_site']**c['eligible_sites']==c['unrestricted_states'] and 1+c['eligible_sites']*(c['states_per_site']-1)==c['maximum_one_modified_site_states'],k)
 elif k=='prot-psm-peptide-error-levels':check(c['correct_psms_same_peptide']+c['incorrect_psms_distinct_peptide']==c['total_psms'] and D(c['incorrect_psms_distinct_peptide'])/c['total_psms']==c['psm_false_fraction'] and D(c['false_peptide_sequences'])/c['distinct_peptide_sequences']==c['peptide_false_fraction'],k)
 elif k=='prot-shared-peptide-logic':
  sets=[list(s) for n in range(1,len(c['proteins'])+1) for s in combinations(c['proteins'],n)]
  for observed,key in [({'p'},'only_p_compatible_nonempty_parent_sets'),({'p','q'},'p_and_q_compatible_nonempty_parent_sets')]:check([s for s in sets if observed<=set().union(*(set(c['proteins'][p]) for p in s))]==c[key],k+key)
 elif k=='prot-coverage-union':
  covered=set().union(*(set(range(a,b+1)) for a,b in c['inclusive_intervals']));check(len(covered)==c['covered_positions_count'] and D(100)*len(covered)/c['reference_length']==c['coverage_percent'] and D(100)*sum(b-a+1 for a,b in c['inclusive_intervals'])/c['reference_length']==c['incorrect_length_sum_percent'],k)
 elif k=='prot-phosphorylation-mz':
  delta=D(c['mass_increment_da'])/c['charge'];check(delta==D(c['delta_mz_exact']) and str(delta.quantize(D('.000001'),rounding=ROUND_HALF_UP))==c['delta_mz_rounded_6dp'],k)
 elif k=='prot-localization-fragments':
  positions={name:list(range(1,int(name[1:])+1)) if name[0]=='b' else list(range(len(c['peptide'])-int(name[1:])+1,len(c['peptide'])+1)) for name in c['fragment_positions']};counts={name:[int(site in pos) for site in c['candidate_modified_positions']] for name,pos in positions.items()};check(positions==c['fragment_positions'] and counts==c['modification_count_for_S2_S3'],k);check([name for name,v in counts.items() if len(set(v))>1]==c['site_determining_fragments'] and [name for name,v in counts.items() if len(set(v))==1]==c['not_site_determining_fragments'],k+': discrimination')
 elif k=='prot-localization-error-level':check(D(c['wrong_sequence_or_modification_count'])/c['accepted_spectra']==c['peptide_assignment_false_fraction'] and D(c['wrong_site_assignments'])/c['accepted_spectra']==c['site_assignment_false_fraction'],k)
 elif k=='prot-occupancy-amount':
  values=[a*b for a,b in zip(c['total_amounts'],c['occupancies'])];check(values==c['modified_amounts'] and values[1]/values[0]==c['modified_amount_ratio'] and c['occupancies'][1]/c['occupancies'][0]==c['occupancy_ratio'],k)
 elif k=='prot-psm-sequence-form-count':check(c['unmodified_form_psms']+c['oxidized_form_psms']==c['psms'] and sum(n>0 for n in (c['unmodified_form_psms'],c['oxidized_form_psms']))==c['distinct_forms'] and c['one_unmodified_sequence']==1,k)
 else:
  assert k=='prot-observability-vs-specificity';check(c['peptide_p_detections']>c['peptide_q_detections'] and c['peptide_p_detections']<=c['injections'] and c['peptide_p_parent_count']>1 and c['peptide_q_parent_count']==1,k)

small=read('tests/fixtures/small-molecules-expansion.json');assert len(small['cases'])==7
for c in small['cases']:
 i=c.get('input',{});k=c['kind']
 if k=='monoisotopic_mass':
  constants=small['source_constants'];m=sum(i['formula'][el]*constants[key] for el,key in [('C','carbon12_da'),('H','hydrogen1_da'),('O','oxygen16_da')]);mz=(m+constants['proton_da_adopted'])/i['charge'];o=dict(neutral_mass_da=m,ion_mz=mz,neutral_display=m.quantize(D('.000001')),ion_display=mz.quantize(D('.000001')))
 elif k=='signed_ppm':
  error=(i['observed_mz']-i['theoretical_mz_rounded'])/i['theoretical_mz_rounded']*10**6;half=i['theoretical_mz_rounded']*i['search_tolerance_ppm']/10**6;o=dict(error_ppm_display=error.quantize(D('.1')),half_width_mz_display=half.quantize(D('.000001')),accepted=abs(error)<=i['search_tolerance_ppm'],identified=False)
 elif k=='lipid_chain_totals':
  totals=[tuple(sum(x[n] for x in chains) for n in (0,1)) for chains in i['candidates'].values()];assert len(set(totals))==1;a,b=totals[0];o=dict(carbon_sum=a,unsaturation_sum=b,sum_label=f'PC {a}:{b}',chains_distinguished_by_sum=False)
 elif k=='evidence_claims':
  assert i['same_precursor_association_validated'] and not any(i[x] for x in ('sn_evidence','double_bond_location_evidence','double_bond_geometry_evidence'));o=dict(supported_label=i['class']+' '+'_'.join(i['chain_evidence']),unsupported_labels=[i['class']+' '+'/'.join(i['chain_evidence']),i['class']+' '+'/'.join(i['chain_evidence'])+'(9Z)'])
 elif k=='mobility_calculation':
  t=i['arrival_time_s']-i['outside_drift_time_s'];mobility=i['length_m']/(i['field_v_per_m']*t);uncorrected=i['length_m']/(i['field_v_per_m']*i['arrival_time_s']);o=dict(drift_time_s=t,mobility_m2_per_Vs=mobility,mobility_cm2_per_Vs=mobility*10000,uncorrected_mobility_cm2_per_Vs=uncorrected*10000,uncorrected_bias_percent=100*(uncorrected/mobility-1),reduced_mobility_cm2_per_Vs=mobility*10000*i['gas_density_ratio_N_over_N0'])
 elif k=='percent_difference':o=dict(signed_difference_percent=100*D(i['query_A2']-i['reference_A2'])/i['reference_A2'],identification_from_difference_alone=False)
 else:
  assert k=='terminology_boundary';o=dict(isomer_same_formula=True,isomer_distinguished_by_exact_mass_alone=False,iupac_isobar_same_nominal_mass=True,iupac_isobar_different_exact_mass=True)
 check(equal(o,c['expected']),c['id']+': '+str(o))

pairs=0;source_hashes=0
for name in ('separation','quantification','proteomics','small-molecules'):
 packet=ROOT/'review'/('expansion-'+name)
 hashes=json.loads((packet/'packet-files.sha256.json').read_text())
 for path,expected in hashes.items():
  if path.startswith('tests/fixtures/'):
   check(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==expected,path+': fixture hash')
  if path.startswith('content/') and path.endswith('.html'):
   check(hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==expected,path+': source hash');source_hashes+=1
 for kind,filename in [('guide','articles'),('term','terms')]:
  for a in json.loads((packet/f'metadata/{filename}.additions.json').read_text()):
   slug=a['slug'];bodies=[(ROOT/('content/terms/' if kind=='term' else 'content/')/lang/(slug+'.html')).read_text() for lang in ('en','zh')]
   for body in bodies:ET.fromstring('<article>'+body+'</article>')
   ids=lambda b:re.findall(r'id="([^"]+)"',b)
   check(ids(bodies[0])==ids(bodies[1]),slug+': anchors')
   # Equivalent ordinal label in the authored MSI identification description.
   normalized=bodies[1].replace('一级','level-1')
   check(Counter(re.findall(r'\d+(?:\.\d+)?',bodies[0]))==Counter(re.findall(r'\d+(?:\.\d+)?',normalized)),slug+': numerical tokens')
   check(re.findall(r'href="#ref-([^"]+)">\[(\d+)\]',bodies[0])==re.findall(r'href="#ref-([^"]+)">\[(\d+)\]',bodies[1]),slug+': citation parity')
   pairs+=1
assert pairs==36 and source_hashes==72
if failures:
 for failure in failures:print('FAIL:',failure)
 raise SystemExit(1)
print('PASS: 43 expansion fixtures (separation 11, quantification 13, proteomics 12, small molecules 7), 36 paired articles and 72 authored source hashes. Semantic guards are not experimental validation.')
