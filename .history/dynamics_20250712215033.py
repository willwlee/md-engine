import numpy as np

class NVE():
    def __init__(self, x0=0, v0=0, mass=1, timestep=1, algorithm=''):
        self.x = x0
        self.v = v0
        self.m = mass
        self.dt = timestep
        self.algorithm = algorithm

    def run(nsteps):

        positions = np.zeros(nsteps)
        velocities = np.zeros(nsteps)

        PEs = np.zeros(nsteps)
        KEs = np.zeros(nsteps)
        Es = np.zeros(nsteps)
    
        if algorithm=="taylor":
            for i in range(nsteps):
                import Integrators import beeman
                positions[i] = taylor(x,v,)
        elif algorithm=="velocityverlet":
            pass
        elif algorithm=="leapfrogverlet":
            pass
        elif algorithm=="beeman":
            pass
        else:
            raise ValueError("Algorithm is undefined or does not exist.")
        
        return trajectory


class NVT():
    pass

