# Write a program to calculate the deflection of a beam

#define the quantities in the problem
force = 100                  # Force applied in newtons
dist_to_force = 6            # distance in m to the force
beam_length = 13             # total length of beam
Youngs_mod = 2.0685e11       # Young’s modulus in Pa
moment_inertia = 0.005208    # Moment of inertia in m^4

# with the above quantities, the value of delta_max is 1.8379711471947547e-05
numerator = force * dist_to_force**2
denom = 6 * Youngs_mod * moment_inertia
delta_max = numerator/denom * (3*beam_length - dist_to_force)
print(delta_max)