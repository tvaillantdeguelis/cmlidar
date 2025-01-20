'''
Standardized colormaps for cloud and aerosol lidar plots.

Created by Thibault Vaillant de Guélis
2024-09-02

Edited by Rob Ryan
2025-01-16
'''

import os

import numpy as np
import matplotlib

try:
    from matplotlib import colormaps
    register_cmap = lambda name, cmap: colormaps.register(cmap, name=name)
except ImportError:
    # PendingDeprecationWarning from matplotlib 3.6
    from matplotlib.cm import register_cmap


# Location of rgb files
_datadir = os.path.join(os.path.dirname(__file__), 'rgb')

# List of colormap names
_cmapnames = ['backscatter', 'backscatter_discrete', 'backscatter_continuous', 
              'depolarization', 'depolarization_discrete',
              'colorratio', 'colorratio_discrete']

# Initialize dictionaries to contain cmap and norm
cmap_d = dict()
norm_d = dict()

def _make_mpl_lscm(cmapname, rgb_0_1, rgb_over, rgb_under, reverse=False):
    over_color = rgb_over
    under_color = rgb_under
    if reverse:
        cmapname = cmapname + '_r'
        rgb_0_1 = rgb_0_1[::-1, :]
        over_color = rgb_under
        under_color = rgb_over
    # Add colormap to dictionary
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list(
        cmapname, rgb_0_1, N=rgb_0_1.shape[0])
    cmap.name = cmapname
    cmap.set_under(under_color)
    cmap.set_over(over_color)
    # register colormap for matplotlib to use
    register_cmap(cmapname, cmap)
    return cmap, cmapname

def _getrgb_0_1_over_under(datadir, cmapname):
    # Load RGB values
    rgb_0_255 = np.genfromtxt(os.path.join(datadir, cmapname + '-rgb.csv'), delimiter=',')
    # Normalize 0-255 RGB values to 0-1
    rgb_0_1 = rgb_0_255/255
    
    # Extract under and over colors
    over_color = rgb_0_1[-1]
    under_color = rgb_0_1[0]
    rgb_0_1 = rgb_0_1[1:-1,:]

    return rgb_0_1, over_color, under_color

# Add colormaps and reversed to dictionary
for cmapname in _cmapnames:
    rgb_0_1, over_color, under_color = _getrgb_0_1_over_under(_datadir, cmapname)
    cmap, cmapname = _make_mpl_lscm(cmapname, rgb_0_1, over_color, under_color)
    cmap_d[cmapname] = cmap
    cmap_r, cmapname_r = _make_mpl_lscm(cmapname, rgb_0_1, over_color, under_color, reverse=True)
    cmap_d[cmapname_r] = cmap_r

# Boundary arrays
BACKSCATTER_DISCRETE_BOUNDS = [
    1e-5,
    1e-4, 3e-4, 6e-4,
    1e-3, 1.5e-3, 2e-3, 3e-3, 4e-3, 5e-3, 6e-3, 8e-3,
    1e-2, 1.5e-2, 2e-2, 3e-2, 5e-2
    ]
norm_d['backscatter_discrete_norm'] = matplotlib.colors.BoundaryNorm(
    BACKSCATTER_DISCRETE_BOUNDS, len(BACKSCATTER_DISCRETE_BOUNDS)-1)

DEPOLARIZATION_DISCRETE_BOUNDS = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
norm_d['depolarization_discrete_norm'] = matplotlib.colors.BoundaryNorm(
    DEPOLARIZATION_DISCRETE_BOUNDS, len(DEPOLARIZATION_DISCRETE_BOUNDS)-1)

COLORRATIO_DISCRETE_BOUNDS = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4]
norm_d['colorratio_discrete_norm'] = matplotlib.colors.BoundaryNorm(
    COLORRATIO_DISCRETE_BOUNDS, len(COLORRATIO_DISCRETE_BOUNDS)-1)

NB_COLORS_BETWEEN_MID_DISCRETE_BIN = 15
bounds = np.array(())
for i in range(len(BACKSCATTER_DISCRETE_BOUNDS)-1): # color of discrete bounds at the mid value of the range bin
    bounds = np.append(bounds, np.linspace(BACKSCATTER_DISCRETE_BOUNDS[i], BACKSCATTER_DISCRETE_BOUNDS[i+1], NB_COLORS_BETWEEN_MID_DISCRETE_BIN+1)[:-1])
bounds = np.append(bounds, BACKSCATTER_DISCRETE_BOUNDS[-1])
BACKSCATTER_CONTINUOUS_BOUNDS = bounds.tolist()
norm_d['backscatter_continuous_norm'] = matplotlib.colors.BoundaryNorm(
    BACKSCATTER_CONTINUOUS_BOUNDS, len(BACKSCATTER_CONTINUOUS_BOUNDS)-1)

# Make cmaps and norms available to call
locals().update(cmap_d)
locals().update(norm_d)