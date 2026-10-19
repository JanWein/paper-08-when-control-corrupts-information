"""Synthetic audit-identification example and bounded error sensitivity.
Known benchmark only in this synthetic example. This is not field validation.
"""
from pathlib import Path
import json
import numpy as np
p,q,f=.12,.6,.02
truth=np.array([[(1-p)*(1-f),(1-p)*f],[p*(1-q),p*q]])
def matrix(alpha,beta):return np.array([[beta,1-alpha],[1-beta,alpha]])
observed=matrix(.9,.95)@truth
feasible=[]
for alpha in np.linspace(.85,.95,101):
 for beta in np.linspace(.93,.98,101):
  cells=np.linalg.solve(matrix(alpha,beta),observed)
  if cells.min()>=-1e-12:
   prev=cells[1].sum();sens=cells[1,1]/prev;fa=cells[0,1]/cells[0].sum()
   feasible.append([prev,sens,fa])
a=np.array(feasible)
assert len(a)>0
assert np.all(np.array([p,q,f])>=a.min(0)-1e-10) and np.all(np.array([p,q,f])<=a.max(0)+1e-10)
result={'status':'SYNTHETIC only; grid envelope, not certified sharp continuum bounds','observed_Y_by_R':observed.tolist(),'true_parameters':[p,q,f],'assumed_alpha_range':[.85,.95],'assumed_beta_range':[.93,.98],'grid_step':.001,'beta_grid_step':.0005,'feasible_grid_points':len(a),'grid_min_p_q_f':a.min(0).tolist(),'grid_max_p_q_f':a.max(0).tolist()}
Path(__file__).with_name('results').joinpath('audit_bounds.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
