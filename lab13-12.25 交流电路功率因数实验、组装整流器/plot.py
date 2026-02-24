import numpy as np
import matplotlib.pyplot as plt
# --------------------------
# 1. Define experimental data
# --------------------------
# Capacitance (μF)
C = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Power factor (cosφ)
cos_phi = np.array([0.3234, 0.4202, 0.5454, 0.6087, 0.8632, 0.8680, 0.7189, 0.5304, 0.4147, 0.3843])

# --------------------------
# 2. Polynomial fitting (3rd order, optimal for this data trend)
# --------------------------

# Create dense x-values for smooth fitting curve
C_fit = np.linspace(min(C), max(C), 100)

# --------------------------
# 4. Plot the curve (save directly, no display)
# --------------------------
plt.figure(figsize=(10, 6))  # Set figure size

# Plot original data (solid line + markers)
plt.plot(C, cos_phi, 'b-', marker='o', linewidth=2, markersize=8, label='Original Data (cosφ vs C)')

# Set plot properties
plt.title('Power Factor (cosφ) vs Capacitance (C) Curve', fontsize=14, pad=15)
plt.xlabel('Capacitance (μF)', fontsize=12)
plt.ylabel('Power Factor (cosφ)', fontsize=12)
plt.xticks(C)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(loc='upper left', fontsize=11)

# --------------------------
# Save image (key modification: replace plt.show() with plt.savefig())
# --------------------------
# Save as PNG file (high resolution: dpi=300)
# - bbox_inches='tight': Prevent label/text cutoff
# - overwrite existing file by default
plt.tight_layout()
plt.savefig('power_factor_curve.png', dpi=300, bbox_inches='tight')

# Close the plot to release memory (optional but recommended)
plt.close()

# --------------------------
# 5. Print results to console
# --------------------------
print("="*50)
print("="*50)
print(f"Image saved successfully as: power_factor_curve.png")