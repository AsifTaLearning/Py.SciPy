from sympy import var
var('fun x0 method callback options boolean number')

from scipy.optimize import root , minimize
from math import cos
# SciPy Optimizers
# Roots of an Equation
# x + cos(x)

fun # - a function representing an equation.

x0 # - an initial guess for the root.


def eqn(x):
  
  return x + cos(x)

myroot = root(eqn, 0)

print(myroot.x)

# Minimizing a Function
# Finding Minima

fun # - a function representing an equation.

x0 # - an initial guess for the root.

method # - name of the method to use. Legal values:

'CG'
'BFGS'
'Newton-CG'
'L-BFGS-B'
'TNC'
'COBYLA'
'SLSQP'

def eqn(x):
  return x**2 + x + 2

mymin = minimize(eqn, 0, method='BFGS')

print(mymin)




