import numpy as np
from atoms import *

class NVE():
    def __init__(self, x0=0, v0=0, mass=1, timestep=1, algorithm="velocityverlet"):
        self.x = x0
        self.v = v0
        self.m = mass
        self.dt = timestep
        self.algorithm = algorithm

    def run(self, nsteps):

        x = self.x
        v = self.v
        m = self.m
        dt = self.dt

        positions = np.zeros(nsteps)
        velocities = np.zeros(nsteps)
    
        if self.algorithm=="taylor":
            for i in range(nsteps):
                from Integrators import taylor
                positions[i], velocities[i] = taylor(x, v, m=m, dt=dt)       
        
        elif self.algorithm=="velocityverlet":
            from Integrators.verlet import velocity_verlet
            positions[i], velocities[i] = velocity_verlet(x, v, m=m, dt=dt)
        
        elif self.algorithm=="leapfrogverlet":
            from Integrators.verlet import leapfrog_verlet
            positions[i], velocities[i] = leapfrog_verlet(x, v, m=m, dt=dt)
        
        elif self.algorithm=="beeman":
            from Integrators.verlet import beeman
            positions[i], velocities[i] = beeman(x, v, m=m, dt=dt)
        else:
            raise ValueError("Algorithm is undefined or does not exist.")
        
        PEs = get_potential_energy(positions)
        KEs = get_kinetic_energy(velocities, m=m)
        Es = PEs + KEs

        trajectory = dict()
        trajectory['x'] = positions
        trajectory['v'] = velocities
        trajectory['KE'] = KEs
        trajectory['PE'] = PEs
        trajectory['E'] = Es

        return trajectory


class NVT():
    pass

