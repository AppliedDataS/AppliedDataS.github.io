from sympy import pprint, init_printing, latex
init_printing()
from sympy import var, diff, exp, sin, cos, tan, sqrt, pi, Function
t =var('t')
# # x = Function('t')
# # y = Function('t')
# m = var('m')
# z = var('z')
# res = diff(diff(exp(x) + 2 * sin(x) + x ** 3))
# res = diff(exp(x) / x)
# res = diff(x*exp(x)*cos(x))
# res = diff((x**3)*sin(x))
# res = diff(tan(x))
# res = diff(exp(sin(x**2)))
# res = diff(x**(3/2)+(pi)*x**2+sqrt(7))
# res = diff(x**3*cos(x)*exp(x))
# res = diff(exp((x+1)**2))
# res = diff(x**2*cos(x**3))
# res = diff(sin(x))*exp(cos(x))
# eq = pi * x**3 + x * y**2 + m * y**4
# eq = x**2 * y + y**2 * z + z**2 * x
# eq = exp(2*x) * sin(y) * z**2 + cos(z) * exp(x) * exp(y)
# eq = sqrt(x)/y

x = t 
y =sin(t)

f = sqrt(x)/y
# resX = diff(eq, x)
# resY = diff(eq, y)
# resZ = diff(eq, z)

# pprint(diff(f,t))

x = t + 1
y = t - 1 
z = t**2
f = cos(x) * sin(y) * exp(2*z)
# resX = diff(eq, x)
# resY = diff(eq, y)
# resZ = diff(eq, z)

pprint(latex(diff(f,t)))
