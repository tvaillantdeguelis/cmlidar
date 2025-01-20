import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, LogLocator
import cmlidar

def backscatter_cbar_labels(cbar):
    cbar.ax.yaxis.set_major_locator(LogLocator(numticks=15))
    cbar.ax.tick_params(which='both', labelright=False)
    minor_bounds = cmlidar.cm.BACKSCATTER_DISCRETE_BOUNDS
    cbar.ax.yaxis.set_minor_locator(FixedLocator(minor_bounds))
    cbar_minor_label = ['1.0',
                        '1.0', '3.0', '6.0',
                        '1.0', '1.5', '2.0', '3.0', '4.0', '5.0', '6.0', '8.0',
                        '1.0', '1.5', '2.0', '3.0', '5.0']
    for j, bound in enumerate(minor_bounds):
        cbar.ax.text(1.5, bound, cbar_minor_label[j], va='center', fontsize=6)
    cbar_major_label = ['$\mathbf{×10^{-5}}$', '$\mathbf{×10^{-4}}$', '$\mathbf{×10^{-3}}$', '$\mathbf{×10^{-2}}$']
    c_bar_major_values = np.array((1e-5, 1e-4, 1e-3, 1e-2))
    for j, bound in enumerate(c_bar_major_values):
        cbar.ax.text(2.5, bound, cbar_major_label[j], va='center', fontsize=8)

# Generate random data for the subplots
np.random.seed(42)  # For reproducibility
random_depolarization_data = np.random.uniform(0, 0.8, (10, 10)) 
random_colorratio_data = np.random.uniform(0, 1.6, (10, 10))   
random_backscatter_data = np.random.uniform(1.0e-6, 6.0e-2, (10, 10))

# Create a figure
fig, axes = plt.subplots(4, 1, figsize=(8, 15), dpi=300)

ax = axes[0]
p = ax.pcolormesh(random_depolarization_data, cmap="depolarization_discrete", 
                        norm=cmlidar.cm.depolarization_discrete_norm)
cbar = plt.colorbar(p, ax=ax, extend='both')
ax.set_title('depolarization_discrete')

ax = axes[1]
p = ax.pcolormesh(random_colorratio_data, cmap="colorratio_discrete", 
                        norm=cmlidar.cm.colorratio_discrete_norm)
cbar = plt.colorbar(p, ax=ax, extend='both')
ax.set_title('colorratio_discrete')

ax = axes[2]
p = ax.pcolormesh(random_backscatter_data, cmap="backscatter_discrete", 
                        norm=cmlidar.cm.backscatter_discrete_norm)
cbar = plt.colorbar(p, ax=ax, extend='both')
backscatter_cbar_labels(cbar)
ax.set_title('backscatter_discrete')

ax = axes[3]
p = ax.pcolormesh(random_backscatter_data, cmap="backscatter_continuous", 
                        norm=cmlidar.cm.backscatter_continuous_norm)
cbar = plt.colorbar(p, ax=ax, extend='both')
backscatter_cbar_labels(cbar)
ax.set_title('backscatter_continuous')

plt.tight_layout()

# Save figure
plt.savefig('./examples/colorbars.png')