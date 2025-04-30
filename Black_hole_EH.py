
import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import G, c

# Define constants and mass range
M_sun = 1.989e30  # Solar mass in kg
masses = np.linspace(1, 1e7, 30) * M_sun  # 1 to 10000000, 30 solar mass in kg
a = 0.5  # Kerr spin parameter (dimensionless, 0 to 1, moderate spin)

# Calculate Schwarzschild radius
R_s = (2 * G * masses) / (c ** 2)  # R_s = 2GM/c^2, in meters
R_s_km = R_s / 1000  # in kms

# Calculate Kerr event horizon radius
R_kerr = (G * masses / (c ** 2)) * (1 + np.sqrt(1 - a ** 2))  # R_+ = (GM/c^2)(1 + sqrt(1-a^2))
R_kerr_km = R_kerr / 1000  # in kms

# Real black holes
cygnus_mass = 15 * M_sun  # Cygnus X-1, ~15 solar masses
sgr_a_mass = 4e6 * M_sun  # Sgr A*, ~4 million solar masses
Gaia_BH1_mass = 9.62* M_sun   # Gaia BH1, ~9.62 solar masses
cygnus_R_s = (2 * G * cygnus_mass) / (c ** 2) / 1000  # Schwarzschild in km
sgr_a_R_s = (2 * G * sgr_a_mass) / (c ** 2) / 1000  # Schwarzschild in km
Gaia_BH1_R_s = (2 * G * Gaia_BH1_mass) / (c ** 2) / 1000 # Schwarzschild in km

# Create the plot
plt.figure(figsize=(10, 6))  # Wide plot
plt.plot(masses / M_sun, R_s_km, 'b-', label='Schwarzschild (Non-Rotating)')  # Blue line
plt.plot(masses / M_sun, R_kerr_km, 'r--', label='Kerr (Rotating, a=0.5)')  # Red dashed line
plt.scatter([15], cygnus_R_s, color='green', s=100, label='Cygnus X-1 (~15 M⊙)')  # Green dot
plt.scatter([4e6], sgr_a_R_s, color='orange', s=100, label='Sgr A* (~4M M⊙)')  # Orange dot
plt.scatter(9.26, Gaia_BH1_R_s, color = 'purple', s=100, label='Gaia BH1* (~ 9.62M⊙)') #purple dot
plt.xscale('log')  # Log scale for x-axis to show Sgr A*
plt.xlabel('Black Hole Mass (Solar Masses)')
plt.ylabel('Event Horizon Radius (km)')
plt.title('Event Horizon Radii: Schwarzschild vs. Kerr Black Holes')
plt.legend()
plt.grid(True)

# Save and show
plt.savefig('black_hole_comparison.png')
plt.savefig('black_hole_comparison.pdf')
plt.show()
