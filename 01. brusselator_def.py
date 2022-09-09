import math

A, B = 1, 3
w = 0
e = 0

def brusselator(t, z):
    x, y = z
    return [A + x*x*y - (B+1)*x + e*math.cos(w*t), B*x - x*x*y]

print("main has been loaded")
