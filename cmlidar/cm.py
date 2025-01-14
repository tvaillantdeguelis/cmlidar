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
cmap_d = dict()

# Add colormaps and reversed to dictionary
for cmapname in cmapnames:
    # Load RGB values
    rgb_0_255 = np.genfromtxt(os.path.join(datadir, cmapname + '-rgb.csv'), delimiter=',')

    # Get number of colors
    nb_colors = rgb_0_255.shape[0]

    # Normalize 0-255 RGB values to 0-1
    rgb_0_1 = rgb_0_255/255

    # Add colormap and reversed to dictionary
    cmap_d[cmapname] = mpl.colors.LinearSegmentedColormap.from_list(cmapname, rgb_0_1, N=nb_colors)
    cmap_d[cmapname].name = cmapname
    cmap_d[cmapname + '_r'] = mpl.colors.LinearSegmentedColormap.from_list(cmapname + '_r', rgb_0_1[::-1, :], N=nb_colors)
    cmap_d[cmapname + '_r'].name = cmapname + '_r'

# Make colormaps available to call
locals().update(cmap_d)