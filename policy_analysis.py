"""Paper 08 R1. All numerical examples are SYNTHETIC.
Finite-menu global solution, F=0 benchmark, corner tests, and interval certificates.
Run python3 policy_analysis.py from any directory. No network or private data.
"""
from pathlib import Path
import csv,json
from fractions import Fraction as Q
import numpy as np
from scipy.optimize import brentq, minimize
from mpmath import iv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
O=Path(__file__).parent/'results'; O.mkdir(exist_ok=True)
P=dict(p0=.2,ce=.2,k=.3,u=.9,v=.1,eta=1.,h=2.,b=2.)
def solve(a,s,F=0.,p=P):
    c=float(np.clip((s-p['v']-a*F)/p['eta'],0,1))
    g=p['u']+(p['v']-s)*(1-c)-p['eta']*c*c/2-a*F*c
    H=p['h']+a*p['b']
    # This implementation is restricted to the manuscript's globally concave class.
    assert p['p0']*max(g,0)/p['k']<1
    assert H>2*p['p0']*max(g,0)**2/p['k']
    fun=lambda e:p['ce']*e-p['p0']*np.exp(-e)*(H-p['p0']*np.exp(-e)*max(g,0)**2/p['k'])
    e=brentq(fun,0,30,xtol=1e-14)
    prob=p['p0']*np.exp(-e);d=prob*max(g,0)/p['k'];q=d*(1-c)
    cost=p['ce']*e*e/2+p['k']*d*d/2+prob*d*p['eta']*c*c/2
    return dict(a=float(a),s=float(s),F=float(F),e=e,p=prob,d=d,c=c,g=g,q=q,r=prob*q,cost=cost)
def utility(e,d,c,a,s,F,p=P):
    prob=p['p0']*np.exp(-e)
    return -p['ce']*e*e/2-(p['h']+a*p['b'])*prob+prob*d*(p['u']+(p['v']-s)*(1-c)-p['eta']*c*c/2-a*F*c)-p['k']*d*d/2
D,kap,gam,rho,B=3.,.05,.02,1.,2.8
rows=[]
for a in [0,.4,.8]:
 for s in [0,.4,.8,1.2]:
    z=solve(a,s);z['feasible']=(P['b'] if a>0 else 0)+s<=B+1e-12
    z['phi']=max(1-s/.8,0)**2
    z['J']=z['q']+a*rho*(1-z['q'])
    z['I']=z['p']*z['J'];z['T']=z['p']*(z['q']+a*(1-z['q']))
    z['base']=-D*z['p']+P['u']*z['p']*z['d']-z['cost']-kap*a*a/2-gam*z['phi']
    z['id']=f'a{a:.1f}_s{s:.1f}'
    rows.append(z)
feas=[z for z in rows if z['feasible']]
# All-line intersections + feasibility inequalities give the exact finite-menu hull.
intervals=[]
for z in feas:
    lo=0.;hi=float('inf')
    for w in feas:
        di=z['I']-w['I'];db=z['base']-w['base']
        if abs(di)<1e-14:
            if db< -1e-13:hi=-1
        elif di>0:lo=max(lo,-db/di)
        else:hi=min(hi,-db/di)
    if lo<hi:intervals.append(dict(id=z['id'],lower=lo,upper=None if np.isinf(hi) else hi))
intervals.sort(key=lambda x:x['lower'])
assert [x['id'] for x in intervals]==['a0.4_s0.8','a0.4_s0.4','a0.8_s0.8','a0.8_s0.4','a0.8_s0.0']
for it in intervals:
    L=it['lower']+1 if it['upper'] is None else (it['lower']+it['upper'])/2
    winner=max(feas,key=lambda x:x['base']+L*x['I'])
    assert winner['id']==it['id']
# Exact decimal primitives and outward interval arithmetic certify all comparisons.
iv.dps=50
def R(n):
    f=Q(str(n));return iv.mpf(f.numerator)/f.denominator
def rat(f):return iv.mpf(f.numerator)/f.denominator
def bounds(x):return [float(np.nextafter(float(x.a),-np.inf)),float(np.nextafter(float(x.b),np.inf))]
def sign(x):
    if x.a>0:return 1
    if x.b<0:return -1
    return 0
cert=[]
root_certificates=[]
for z in feas:
    a,s=Q(str(z['a'])),Q(str(z['s']))
    c=max(Q(0),min(Q(1),s-Q('0.1')))
    g=Q('.9')+(Q('.1')-s)*(1-c)-c*c/2
    H=2+2*a
    def ff(t):
        ee=rat(t);pp=R('.2')*iv.exp(-ee)
        return R('.2')*ee-pp*(rat(H)-pp*rat(g*g)/R('.3'))
    l,h=Q(0),Q(8)
    assert sign(ff(l))<0 and sign(ff(h))>0
    for _ in range(120):
        m=(l+h)/2;sg=sign(ff(m))
        if sg<0:l=m
        elif sg>0:h=m
        else:break
    root_certificates.append(dict(id=z['id'],lower_fraction=str(l),upper_fraction=str(h),lower_f_sign=sign(ff(l)),upper_f_sign=sign(ff(h))))
    E=iv.mpf([rat(l).a,rat(h).b]);prob=R('.2')*iv.exp(-E);dd=prob*rat(g)/R('.3');qq=dd*rat(1-c)
    I=prob*(qq+rat(a)*(1-qq));cost=R('.2')*E**2/2+R('.3')*dd**2/2+prob*dd*rat(c*c)/2
    base=-3*prob+R('.9')*prob*dd-cost-R('.05')*rat(a*a)/2-R('.02')*rat(max(1-s/Q('.8'),Q(0))**2)
    cert.append(dict(id=z['id'],e=E,I=I,base=base,reported=prob*qq,audit_new=prob*rat(a)*(1-qq)))
cd={z['id']:z for z in cert}
# Certify active policy at rational witnesses; affine comparisons certify interval interiors
# once every pairwise bound is enclosed and consecutive roots strictly ordered.
witnesses=['0','.66','1','3','6']
certificate_margins=[]
for it,L in zip(intervals,witnesses):
    z=cd[it['id']];margins=[z['base']-w['base']+R(L)*(z['I']-w['I']) for w in cert if w['id']!=z['id']]
    assert all(sign(x)>0 for x in margins)
    certificate_margins.append(dict(id=z['id'],L=L,min_gap_lower=min(bounds(x)[0] for x in margins)))
# Five strict winners persist at the same learning-value witnesses for every rho in [.8,1].
# Pairwise surplus differences are affine in rho, so endpoint positivity suffices.
robust_margins=[]
for it,L in zip(intervals,witnesses):
 z=cd[it['id']]
 for rr in ['.8','1']:
  gaps=[z['base']-w['base']+R(L)*(z['reported']-w['reported']+R(rr)*(z['audit_new']-w['audit_new'])) for w in cert if w['id']!=z['id']]
  assert all(sign(t)>0 for t in gaps)
  robust_margins.append(dict(id=z['id'],L=L,rho=rr,min_gap_lower=min(bounds(t)[0] for t in gaps)))
thresholds=[]
for x,y in zip(intervals,intervals[1:]):
    z,w=cd[x['id']],cd[y['id']]
    t=(z['base']-w['base'])/(w['I']-z['I'])
    thresholds.append(bounds(t))
assert all(thresholds[i][1]<thresholds[i+1][0] for i in range(3))
# Exact hull region proof: for each active line, every pairwise lower/upper threshold
# is certified to lie outside its proposed active segment.
for idx,it in enumerate(intervals):
    z=cd[it['id']];low=iv.mpf(0) if idx==0 else (cd[intervals[idx-1]['id']]['base']-z['base'])/(z['I']-cd[intervals[idx-1]['id']]['I'])
    high=None if idx==len(intervals)-1 else (z['base']-cd[intervals[idx+1]['id']]['base'])/(cd[intervals[idx+1]['id']]['I']-z['I'])
    adjacent={it['id']}
    if idx:adjacent.add(intervals[idx-1]['id'])
    if idx<len(intervals)-1:adjacent.add(intervals[idx+1]['id'])
    for w in cert:
        if w['id'] in adjacent:continue
        di=z['I']-w['I'];db=z['base']-w['base']
        if sign(di)>0:
            t=-db/di;assert sign(low-t)>0
        else:
            assert sign(di)<0
            t=-db/di
            assert high is not None and sign(t-high)>0
# Global corner and derivative checks across the compact policy set and stress cases.
max_err=0.;cases=0
for F in [0.,1.]:
 for a in np.linspace(0,1,9):
  for s in [0,.1,.4,.8,1.1,1.6,2.]:
    z=solve(a,s,F);cases+=1
    fit=minimize(lambda x:-utility(*x,a,s,F),[z['e']+.05,max(z['d'],.05),z['c']],bounds=[(0,10),(0,1),(0,1)],tol=1e-12)
    assert abs(-fit.fun-utility(z['e'],z['d'],z['c'],a,s,F))<1e-8
    if F==0 and .01<a<.99 and z['q']>0:
        eps=1e-5;fd=(solve(a+eps,s)['q']-solve(a-eps,s)['q'])/(2*eps)
        den=P['ce']+(P['h']+a*P['b'])*z['p']-2*z['p']**2*max(z['g'],0)**2/P['k']
        ea=z['p']*P['b']/den;err=abs(fd+ea*z['q']);max_err=max(max_err,err)
assert max_err<1e-8
# Zero attention feasible example with u small; c continuation action is unobserved.
corner=solve(.4,.6,p={**P,'u':.05});assert corner['d']==0 and corner['q']==0
# Primitive fixed-incidence reversal: u=.4, x=.6, eta=F=1 at a=.2.
pfix=.1;s=.7;a=.2;u=.4;c=s-.1-a;g=u-(s-.1)+c*c/2
# g negative here: choose u=.6, x=.6 => c=.4, g=.08, sign negative.
u=.6;g=u-(s-.1)+c*c/2
partial=pfix*(g-c*(1-c))/.3
assert g>0 and partial<0
with open(O/'menu.csv','w') as f:
    w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
ii=next(z for z in feas if z['id']=='a0.4_s0.4');jj=next(z for z in feas if z['id']=='a0.8_s0.8')
rho_star=(ii['r']-jj['r'])/(jj['a']*jj['p']*(1-jj['q'])-ii['a']*ii['p']*(1-ii['q']))
tight_winner=max([z for z in rows if (P['b'] if z['a']>0 else 0)+z['s']<=2.4+1e-12],key=lambda z:z['base'])
assert tight_winner['id']=='a0.4_s0.4'
report=dict(rho_threshold_for_pair=rho_star,tighter_liability_cap_L0_winner=tight_winner['id'],feasible_policies=len(feas),status='SYNTHETIC' ,parameters=P,D=D,kappa=kap,gamma=gam,rho=rho,liability_cap=B,intervals=intervals,threshold_interval_enclosures=thresholds,certified_policy_witnesses=certificate_margins,rho_robustness_witnesses=robust_margins,all_pairwise_region_comparisons_interval_certified=True,max_F0_derivative_error=max_err,global_optimization_cases=cases,zero_attention=corner,fixed_incidence_reversal=dict(p=pfix,s=s,a=a,u=u,c=c,g=g,partial_q_a=partial))
(O/'root_brackets.json').write_text(json.dumps(root_certificates,indent=2))
(O/'verification.json').write_text(json.dumps(report,indent=2))
# Continuous cost/learning parameter map, but policy choices are the finite menu.
Ls=np.linspace(0,7,281)
fig,ax=plt.subplots(1,2,figsize=(10,3.8))
for z in feas:ax[0].plot(Ls,z['base']+Ls*z['I'],alpha=.6,lw=1,label=z['id'])
ax[0].plot(Ls,[max(z['base']+l*z['I'] for z in feas) for l in Ls],color='black',lw=2,label='Global envelope');ax[0].set(xlabel='Diagnostic information value L',ylabel='Synthetic surplus')
# On-envelope s and a show nonmonotone report use.
for field in ['a','s']:ax[1].step(Ls,[max(feas,key=lambda z:z['base']+l*z['I'])[field] for l in Ls],where='post',label=field)
ax[1].set(xlabel='Diagnostic information value L',ylabel='Optimal menu choice');ax[1].legend()
for aa in ax:aa.grid(alpha=.2)
fig.suptitle('SYNTHETIC: awareness-blind audits (F=0), rho=1');fig.tight_layout();fig.savefig(O/'governance.pdf');fig.savefig(O/'governance.png',dpi=180)
print(json.dumps(report,indent=2))
