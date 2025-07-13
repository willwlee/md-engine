
def get_potential_energy(x):
    potential = x**4
    return potential

def get_kinetic_energy(v, m=1):
    kinetic = 0.5 * m * v
    return kinetic

def get_force(x):
    force = 4*x**3
    return force