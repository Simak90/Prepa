from numpy import *

a, b = 0, 0 # début et fin 
diff = -5 # Ordre de grandeur

def f(x):


while (b-a) > 10**diff: 
    m = (a+b/2)
    if (f(a)*f(m) <= 0):
        b = m
    else:
        a = m

print(a, b)
