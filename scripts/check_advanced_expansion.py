#!/usr/bin/env python3
"""Recompute authored advanced teaching cases; semantic guards are not validation."""
from collections import Counter
from decimal import Decimal as D
from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, product
from pathlib import Path
from statistics import NormalDist
import hashlib
import json
import re
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
def read(path):return json.loads((ROOT/path).read_text(),parse_float=D)
def same(actual,expected,label):assert actual==expected,(label,actual,expected)
count=0
for packet in ('structural','spatial','computational'):
 cases=read(f'tests/fixtures/{packet}.json')['cases']
 assert len(cases)=={'structural':14,'spatial':12,'computational':13}[packet]
 for c in cases:
  k=c['id'];count+=1
  def eq(a,key):same(a,c[key],k+': '+key)
  if k=='struct-xl-candidate-pairs':
   eq(len(list(combinations(c['candidate_peptides'],2))),'unordered_distinct_pairs');eq(len(list(combinations_with_replacement(c['candidate_peptides'],2))),'unordered_pairs_with_self')
  elif k=='struct-xl-aggregation':
   eq(D(c['wrong_csms'])/(c['correct_csms']+c['wrong_csms']),'csm_error_fraction');fraction=F(c['false_residue_pairs'],c['true_residue_pairs']+c['false_residue_pairs']);same(fraction,F(c['residue_pair_error_fraction']),k);eq(round(100*fraction),'rounded_residue_pair_error_percent')
  elif k=='struct-xl-csm-collapse':
   # The fixture explicitly assigns every spectrum to the same localized link.
   records=[('peptide-pair','residue-pair') for _ in range(c['spectra'])];eq(len(set(p for p,r in records)),'peptide_pairs');eq(len(set(r for p,r in records)),'localized_residue_pairs')
  elif k=='struct-xl-copy-ambiguity':
   assert set(tuple(v) for v in c['peptide_parent_mappings'].values())=={('P',)};assert c['possible_copy_assignments']==[['P1','P1'],['P1','P2']];eq(len(c['possible_copy_assignments'])==1,'resolved_by_sequence_mapping_alone')
  elif k=='struct-glyco-site-membership':
   sets={name:list(range(1,int(name.removeprefix('prefix'))+1)) for name in c['fragment_position_sets']};same(sets,c['fragment_position_sets'],k);membership={name:[int(p in positions) for p in c['candidate_positions']] for name,positions in sets.items()};eq(membership,'glycan_count_under_S2_T3');eq([name for name,values in membership.items() if len(set(values))>1],'discriminating_fragments')
  elif k=='struct-glyco-composition-ambiguity':
   reference=next(iter(c['candidates'].values()));eq([name for name,value in c['candidates'].items() if value==reference],'retained_after_composition_match');assert c['different_linkages']
  elif k=='struct-glyco-joint-error':
   assert c['wrong_peptides']==0;eq(D(c['wrong_peptides'])/c['assignments'],'peptide_error_fraction');eq(D(c['wrong_glycan_compositions'])/c['assignments'],'joint_error_fraction')
  elif k=='struct-glyco-response-fractions':
   signals=[a*b for a,b in zip(c['amounts'],c['response_factors'])];eq(signals,'signals')
   for values,key in [(c['amounts'],'amount_fractions'),(signals,'signal_fractions')]:same([F(v,sum(values)) for v in values],[F(v) for v in c[key]],k)
  elif k=='struct-glyco-combinations':
   eq(len(list(product(*c['alternatives'].values()))),'possible_joint_combinations');assert c['joint_combinations_proven_by_separate_peptides'] is None
  elif k=='struct-phospho-selectivity-recovery':
   eq(D(c['accepted_phosphopeptide_identifications'])/(c['accepted_phosphopeptide_identifications']+c['other_accepted_identifications']),'identification_based_proportion');eq(D(c['reference_recovered_amount'])/c['reference_input_amount'],'reference_recovery')
  elif k=='struct-phospho-expected-localization-error':
   wrong=sum(1-D(p) for p in c['localization_probabilities']);same(wrong,D(c['expected_wrong_count']),k);same(F(wrong)/len(c['localization_probabilities']),F(c['expected_wrong_fraction'].split('/')[0])/F(c['expected_wrong_fraction'].split('/')[1]),k);eq(str((100*wrong/len(c['localization_probabilities'])).quantize(D('.1'))),'rounded_expected_wrong_percent')
  elif k=='struct-phospho-relative-occupancy':
   ratio=D(c['phosphopeptide_amount_ratio'])/c['protein_amount_ratio'];eq(ratio,'relative_occupancy_ratio');assert all(b/a==ratio for a,b in c['possible_occupancy_pairs']);eq(len({a for a,b in c['possible_occupancy_pairs']})==1,'absolute_baseline_identified')
  elif k=='struct-phosphosite-numbering':eq(c['protein_start_one_based']+c['peptide_site_one_based']-1,'protein_site_one_based')
  elif k=='struct-site-occupancy':
   occ=[D(a)/b for a,b in zip(c['modified_molecules'],c['eligible_molecules'])];eq(occ,'occupancies');eq(D(c['modified_molecules'][1])/c['modified_molecules'][0],'modified_amount_fold_change');eq(occ[1]/occ[0],'occupancy_fold_change')
  elif k=='spatial-grid-count':
   positions=[(c['field_um'][0]//p)*(c['field_um'][1]//p) for p in c['pitches_um']];assert all(v%p==0 for v in c['field_um'] for p in c['pitches_um']);eq(positions,'positions');eq(D(positions[0])/positions[1],'position_ratio')
  elif k=='spatial-normalization-denominator':
   norm=[D(a)/b for a,b in zip(c['target_raw'],c['total_signal'])];eq(norm,'normalized');eq(D(c['target_raw'][1])/c['target_raw'][0],'raw_ratio');eq(norm[1]/norm[0],'normalized_ratio')
  elif k=='spatial-specimen-units':eq(c['specimens']*c['pixels_per_specimen'],'observations');eq(c['specimens'],'specimen_level_units')
  elif k=='spatial-pitch-not-resolution':
   eq(c['smallest_tested_passing_feature_um'],'demonstrated_feature_um');assert c['claimed_exact_resolution_um'] is None and c['pitch_um']<c['demonstrated_feature_um']
  elif k=='spatial-ion-window':
   included=[abs(D(m)-D(c['center_mz']))<=D(c['half_width_mz']) for m in c['mz']];eq(included,'included');eq(sum(v for v,yes in zip(c['intensities'],included) if yes),'summed_signal')
  elif k=='spatial-poisson-counting':eq([1/D(n).sqrt() for n in c['expected_counts']],'relative_standard_deviation')
  elif k=='spatial-reporter-interference':
   observed=[a+b for a,b in zip(c['target'],c['interference'])];eq(observed,'observed');eq(D(c['target'][1])/c['target'][0],'target_ratio');eq(D(observed[1])/observed[0],'observed_ratio')
  elif k=='spatial-donor-units':eq(c['donors']*c['cells_per_donor'],'cell_observations');eq(c['donors'],'donor_level_units')
  elif k=='spatial-carrier-quantification':
   assert len(c['quality_pass'])==c['cell_channels'];eq(sum(c['quality_pass']),'usable_cell_measurements');assert c['peptide_identified'] and c['missing_measurements_created_by_carrier']==0
  elif k=='spatial-known-blank-percentile':
   mean,sd,z=[D(c[key]) for key in ('normal_mean','normal_sd','approx_one_sided_z95')];same(mean+sd*z,D(c['approx_threshold']),k);assert abs((1-NormalDist().cdf(float(z)))-float(c['approx_upper_tail_probability']))<.0001
  elif k=='spatial-batch-confounding':eq(c['condition_indicator']!=c['batch_indicator'],'effects_separately_identifiable')
  elif k=='spatial-missing-not-zero':assert c['reported_value'] is None and len(c['compatible_explanations'])>1 and not c['proves_biological_absence']
  elif k=='comp-spectrum-split':
   assert c['train_per_peptide']+c['test_per_peptide']==c['spectra_per_peptide'];eq(c['peptides']*c['train_per_peptide'],'expected_train_spectra');eq(c['peptides']*c['test_per_peptide'],'expected_test_spectra');eq(0 if c['train_per_peptide'] else c['peptides'],'expected_unseen_test_sequences')
  elif k=='comp-peptide-split':
   eq((c['peptides']-c['heldout_peptides'])*c['spectra_per_peptide'],'expected_train_spectra');eq(c['heldout_peptides']*c['spectra_per_peptide'],'expected_test_spectra');eq(c['heldout_peptides'],'expected_unseen_test_sequences')
  elif k=='comp-cosine-scale':
   numerator=D(sum(a*b for a,b in zip(c['a'],c['b'])));denominator=(D(sum(a*a for a in c['a']))*sum(b*b for b in c['b'])).sqrt();eq(numerator/denominator,'expected_cosine');eq(sum(c['a']),'expected_total_a');eq(sum(c['b']),'expected_total_b');assert not c['identity_proven']
  elif k=='comp-confidence-bin':
   fraction=D(c['correct_assignments'])/c['assignments'];eq(fraction,'expected_observed_fraction');eq(c['reported_probability']-fraction,'expected_observed_gap')
  elif k=='comp-precision-recall':
   values={}
   for method in ('a','b'):
    d=c['method_'+method];values[method+'_precision']=D(d['correct_calls'])/(d['correct_calls']+d['incorrect_calls']);values[method+'_recall']=D(d['correct_calls'])/c['known_identification_cases']
   eq(values,'expected')
  elif k=='comp-tdc-count-expression':eq(D(c['decoy_winners']+1)/max(c['target_winners'],1),'expected_expression');assert c['actual_false_target_count'] is None
  elif k=='comp-retention-offset':
   a,b=c['measured_minutes'],c['predicted_minutes'];ma,mb=D(sum(a))/len(a),D(sum(b))/len(b);corr=sum((x-ma)*(y-mb) for x,y in zip(a,b))/(sum((x-ma)**2 for x in a)*sum((y-mb)**2 for y in b)).sqrt();eq(corr,'expected_pearson_correlation');eq(D(sum(abs(x-y) for x,y in zip(a,b)))/len(a),'expected_mean_absolute_error_minutes')
  elif k=='comp-retention-units':
   seconds=c['minutes']*c['seconds_per_minute'];eq(seconds,'expected_seconds');eq(D(seconds)/c['other_record_seconds'],'expected_ratio')
  elif k=='comp-sdrf-relations':eq(c['fractions'],'expected_ms_files');eq(c['samples']*c['fractions'],'expected_sample_file_relations');assert c['expected_biological_replicates_from_relation_count'] is None
  elif k=='comp-format-scope':assert len(set(c['roles'].values()))==4 and not c['expected_interchangeable'] and not c['expected_format_conformance_proves_scientific_validity']
  elif k=='comp-provenance-bytes':assert c['same_bytes'] and c['different_analysis_parameters'] and not c['expected_same_downstream_result_guaranteed'] and not c['expected_correct_sample_attribution_guaranteed']
  elif k=='comp-known-peptide-new-spectrum':eq(c['train_sequence']!=c['test_sequence'],'expected_valid_for_unseen_sequence_claim');eq(c['train_sequence']==c['test_sequence'] and c['different_spectra'],'expected_may_suit_known_sequence_repeat_prediction')
  elif k=='comp-generalization-axes':eq(c['instrument_heldout'],'expected_demonstrated_instrument_transfer');assert c['molecule_disjoint']
  else:raise AssertionError('Unimplemented fixture '+k)
  for kind in ('guide','term'):
   if kind in c:
    slug,anchor=c[kind].split('#')
    for lang in ('en','zh'):
     path=ROOT/'content'/('terms' if kind=='term' else '')/lang/(slug+'.html');assert f'id="{anchor}"' in path.read_text(),(k,path,anchor)
 pairs=0
 directory=ROOT/'review'/('expansion-'+packet)
 hashes=read(str(directory.relative_to(ROOT)/'packet-files.sha256.json'))
 for path,digest in hashes.items():
  if path.startswith(('content/','tests/fixtures/')):assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==digest,path
 for kind,filename in [('guide','articles'),('term','terms')]:
  for a in read(str(directory.relative_to(ROOT)/f'metadata/{filename}.additions.json')):
   texts=[]
   for lang in ('en','zh'):
    source=ROOT/'content'/('terms' if kind=='term' else '')/lang/(a['slug']+'.html');body=source.read_text();texts.append(body);ET.fromstring('<article>'+body+'</article>')
    route=ROOT/('zh' if lang=='zh' else '')/('terms' if kind=='term' else 'guides')/a['slug']/'index.html';assert body in route.read_text()
    citations=re.findall(r'href="#ref-([^"]+)">\[(\d+)\]',body);assert {ref for ref,n in citations}==set(a['refs']);assert all(a['refs'][int(n)-1]==ref for ref,n in citations)
   ids=lambda b:re.findall(r'id="([^"]+)"',b)
   assert ids(texts[0])==ids(texts[1]),a['slug']
   assert Counter(re.findall(r'\d+(?:\.\d+)?',texts[0]))==Counter(re.findall(r'\d+(?:\.\d+)?',texts[1])),a['slug']
   assert re.findall(r'href="#ref-([^"]+)">\[(\d+)\]',texts[0])==re.findall(r'href="#ref-([^"]+)">\[(\d+)\]',texts[1]),a['slug']
   pairs+=1
 assert pairs=={'structural':9,'spatial':6,'computational':9}[packet]
assert count==39
print('PASS: 39 advanced fixtures (14 structural, 12 spatial, 13 computational); 24 bilingual pairs, 48 source and 3 fixture hashes, rendered-body/citation/anchor/numerical parity. Semantic guards are not experimental validation.')
