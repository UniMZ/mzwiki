#!/usr/bin/env python3
"""Reproduce the original teaching figure. Optional dependency: matplotlib.

No measured spectrum or third-party graphic is used. Input assumptions and source
constants live in content/examples/charge-isotope-spectrum.json.
"""
from pathlib import Path
import json
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/'content/examples/charge-isotope-spectrum.json').read_text())
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.hashsalt':'mzwiki-spectrum-v1','axes.spines.top':False,'axes.spines.right':False})
neutral=d['neutral_mass_da'];n=d['charge_magnitude'];h=d['proton_mass_da']
x0=neutral/n+h;spacing=d['carbon_isotope_shift_da']/n
centers=[x0+k*spacing+d['coordinate_offset'] for k in d['displayed_carbon13_counts']]
heights=[100*math.comb(d['carbon_count'],k)*(d['carbon13_fraction']/(1-d['carbon13_fraction']))**k for k in d['displayed_carbon13_counts']]
w=d['fwhm_coordinate']
def peak(x,c,height):return height*math.exp(-4*math.log(2)*((x-c)/w)**2)
def grid(lo,hi,points):return [lo+(hi-lo)*i/(points-1) for i in range(points)]
fig,(ax,zoom)=plt.subplots(2,1,figsize=(6,7.5),layout='constrained')
fig.set_facecolor('#fafbf7')
fig.suptitle('SIMULATED · NOT EXPERIMENTAL', fontsize=12, color='#526866')
for a in (ax,zoom):
 a.set_facecolor('#fafbf7');a.grid(axis='y',color='#d9e3da');a.set_axisbelow(True)
 a.set_ylabel(r'$I / I_A$ (%)');a.set_xlabel(r'$m/z$');a.set_ylim(0,125)
 a.ticklabel_format(axis='x',style='plain',useOffset=False)
x=grid(500.91,502.12,6000)
ax.plot(x,[sum(peak(t,c,height) for c,height in zip(centers,heights)) for t in x],color='#176052',lw=1.8)
for label,c,height in zip('ABC',centers,heights):ax.annotate(label,(c,height),xytext=(0,9),textcoords='offset points',ha='center',fontweight='bold')
ax.set_xticks([501.0,501.5,502.0]);ax.set_xlim(500.91,502.12)
ax.annotate('',xy=(centers[0],117),xytext=(centers[1],117),arrowprops={'arrowstyle':'<->','color':'#153b3b'})
ax.text((centers[0]+centers[1])/2,119,r'$\Delta x = 0.501677$',ha='center',va='bottom',fontsize=11)
ax.set_title('A–C',loc='left',pad=18,fontweight='bold')
x=grid(centers[0]-.02,centers[0]+.02,1000)
zoom.plot(x,[peak(t,centers[0],100) for t in x],color='#176052',lw=2)
zoom.axvline(x0,color='#ae5c3c',ls='--',lw=1.6)
zoom.axvline(centers[0],color='#526866',ls=':',lw=1.2)
zoom.annotate('',xy=(centers[0]-w/2,50),xytext=(centers[0]+w/2,50),arrowprops={'arrowstyle':'<->','color':'#153b3b'})
zoom.text(centers[0]+.006,60,'FWHM\n0.010000',fontsize=11,ha='left')
zoom.annotate(r'$x_{ref}$',xy=(x0,105),xytext=(x0-.011,116),arrowprops={'arrowstyle':'->','color':'#ae5c3c'},color='#ae5c3c',fontsize=12)
zoom.annotate(r'$x_{obs}$',xy=(centers[0],105),xytext=(centers[0]+.008,116),arrowprops={'arrowstyle':'->','color':'#526866'},color='#526866',fontsize=12)
zoom.set_title('A',loc='left',fontweight='bold');zoom.set_xticks([501.00,501.01,501.02]);zoom.set_xlim(centers[0]-.02,centers[0]+.02)
fig.savefig(ROOT/'assets/teaching-spectrum.svg',metadata={'Date':None,'Description':'Simulated carbon-only teaching spectrum; not experimental data. See accompanying article for assumptions and numeric table.'})
# Keep generated SVG text clean for repository whitespace checks.
svg_path=ROOT/'assets/teaching-spectrum.svg'
svg_path.write_text('\n'.join(line.rstrip() for line in svg_path.read_text().splitlines())+'\n')
fig.savefig(ROOT/'assets/teaching-spectrum.png',dpi=180,metadata={'Description':'Simulated teaching spectrum, not experimental data.'})
print('Rendered teaching spectrum from documented model inputs.')
