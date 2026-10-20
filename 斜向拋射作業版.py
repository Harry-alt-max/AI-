import math
from math import sin,radians

θ = math.radians(45)
v_θ = 30
g = 9.81

#H = (v_θ**2*sin(θ)**2)/2*g  # H = pow(v_theta,2)*pow(sin(theta),2)/(2*g)
H = pow(v_θ,2)*pow(sin(θ),2)/(2*g)
R = (v_θ**2*sin(2*θ))/g     # R = pow(v_theta,2)*sin(2*theta)/g
T = (2*v_θ*sin(θ))/g        # T = 2*v_theta*sin(theta)/g
print(f"H={H},R={R},T={T}")