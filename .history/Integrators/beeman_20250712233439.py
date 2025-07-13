"""
"""

def beeman(x, v, force, oldx, m=1, dt=0.001):
    old_a = force(oldx)/m
    a = force(x)/m

    x += v*dt + (4*a - old_a)*dt**2/6

    new_a = force(x)/m
    v += (5*new_a + 8*a - old_a)*dt/12
    return x,v