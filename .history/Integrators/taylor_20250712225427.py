"""

"""

def taylor(x, v, force,m=1, dt=1):

    fx = force(x)

    x += v*dt + 0.5*dt*x/m
    v += dt*fx/m

    return x,v