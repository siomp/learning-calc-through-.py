#solving limits 

import sympy
from sympy import symbols 
from sympy.solvers import solve

x = symbols("x")

#equation 
eq = x**2-4 

#solving#sets()=0 any x

print("x = ", solve(eq,x)) 
