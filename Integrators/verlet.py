"""
"""

def velocity_verlet(x, v, force, m=1, dt=0.001):
    fx = force(x)
    v_half = v + 0.5*dt*fx/m
    x += v_half*dt

    fx = force(x)
    v = v_half + 0.5*dt*fx/m

    return x,v

def leapfrog_verlet(x, v, force, m=1, dt=0.001):
    x += v * dt
    v += dt*force(x)/m

    return x,v