import sympi
from sympi import symbols 
from sympi.solvers import solve

x = symbols("x")

#equation 
eq = x**2-4 

#solving#sets()=0 any x

print("x = ", solve(eq,x)) 
