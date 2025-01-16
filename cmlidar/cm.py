'''
Standardized colormaps for cloud and aerosol lidar plots.

Created by Thibault Vaillant de Guélis
2024-09-02
'''

import os

import numpy as np
import matplotlib as mpl


# Location of rgb files
datadir = os.path.join(os.path.dirname(__file__), 'rgb')

# List of colormap names
cmapnames = ['backscatter', 'backscatter_discrete', 'backscatter_continuous', 
             'depolarization', 'depolarization_discrete',
             'colorratio', 'colorratio_discrete']

# Initialize dictionary to contain colormaps
cmaps_d = dict()

# Add colormaps and reversed to dictionary
for cmapname in cmapnames:
    # Load RGB values
    rgb_0_255 = np.genfromtxt(os.path.join(datadir, cmapname + '-rgb.csv'), delimiter=',')

    # Get number of colors
    nb_colors = rgb_0_255.shape[0]

    # Normalize 0-255 RGB values to 0-1
    rgb_0_1 = rgb_0_255/255

    # Extract under and over colors
    under_color = rgb_0_1[0]
    over_color = rgb_0_1[-1]
    rgb_0_1 = rgb_0_1[1:-1,:]

    # Get number of colors
    nb_colors = rgb_0_1.shape[0]

    # Add colormap and reversed to dictionary
    cmaps_d[cmapname] = mpl.colors.LinearSegmentedColormap.from_list(cmapname, rgb_0_1, N=nb_colors)
    cmaps_d[cmapname].name = cmapname
    cmaps_d[cmapname].set_under(under_color)
    cmaps_d[cmapname].set_over(over_color)
    cmaps_d[cmapname + '_r'] = mpl.colors.LinearSegmentedColormap.from_list(cmapname + '_r', rgb_0_1[::-1, :], N=nb_colors)
    cmaps_d[cmapname + '_r'].name = cmapname + '_r'
    cmaps_d[cmapname + '_r'].set_under(over_color)
    cmaps_d[cmapname + '_r'].set_over(under_color)

# Boundary arrays
COLORRATIO_DISCRETE_BOUNDS = [0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.6]
DEPOLARIZATION_DISCRETE_BOUNDS = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
BACKSCATTER_DISCRETE_BOUNDS = [1e-5, 
                               1e-4, 3e-4, 6e-4,
                               1e-3, 1.5e-3, 2e-3, 3e-3, 4e-3, 5e-3, 6e-3, 8e-3,
                               1e-2, 1.5e-2, 2e-2, 3e-2, 5e-2]
nb_colors_between_mid_discrete_bin = 15 # 16*15+2 = 242
bounds = np.array(())
for i in range(len(BACKSCATTER_DISCRETE_BOUNDS)-1): # color of discrete bounds at the mid value of the range bin
    bounds = np.append(bounds, np.linspace(BACKSCATTER_DISCRETE_BOUNDS[i], BACKSCATTER_DISCRETE_BOUNDS[i+1], nb_colors_between_mid_discrete_bin+1)[:-1])
bounds = np.append(bounds, BACKSCATTER_DISCRETE_BOUNDS[-1])
BACKSCATTER_CONTINUOUS_BOUNDS = bounds.tolist()

# Make colormaps available to call
locals().update(cmaps_d)