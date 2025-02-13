'''
Standardized colormaps for cloud and aerosol lidar plots.

Created by Thibault Vaillant de Guélis
2024-09-02

Edited by Rob Ryan
2025-02-06
'''

import os

import numpy as np
import matplotlib

try:
    from matplotlib import colormaps
    _register_cmap = lambda name, cmap: colormaps.register(cmap, name=name)
except ImportError:
    # PendingDeprecationWarning from matplotlib 3.6
    from matplotlib.cm import register_cmap
    _register_cmap = lambda name, cmap: register_cmap(cmap, name=name)

# Location of rgb files
_datadir = os.path.join(os.path.dirname(__file__), 'rgb')


def _make_matplotlib_linearsegcmap_from_csv_file(cmapname: str, datadir: str, reverse=False) -> matplotlib.colors.LinearSegmentedColormap:
    """Make a matplotlib colormap from a CSV file containing the list a RGB 0-255 color values.

    Args:
        cmapname (str): name of the colormap
        datadir (str): directory containing the file with RGB 0-255 color values
        reverse (bool, optional): if True, reverse the colormap. Defaults to False.

    Returns:
        matplotlib.colors.LinearSegmentedColormap: matplotlib colormap
    """
    # Get list of 0-255 RGB colors
    csv_filename = os.path.join(datadir, cmapname + '-rgb.csv')
    rgb_0_255 = np.genfromtxt(csv_filename, delimiter=',')
    
    if reverse:
        # Reverse the colormap
        cmapname = cmapname + '_r'
        rgb_0_255 = rgb_0_255[::-1, :]

    # Convert 0-255 color values to 0.0-1.0 float values
    rgb_0_1 = rgb_0_255/255.

    # Extract first and last colors of the list as over and under colors
    under_color = rgb_0_1[0]
    cmap_colors = rgb_0_1[1:-1,:]
    over_color = rgb_0_1[-1]

    # Make a matplotlib LinearSegmentedColormap
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list(
        cmapname, cmap_colors, N=cmap_colors.shape[0])
    cmap.name = cmapname
    cmap.set_under(under_color)
    cmap.set_over(over_color)

    # Register colormap for matplotlib to use (e.g., "cmap=<cmapname>")
    _register_cmap(cmapname, cmap) 

    return cmap


_cmap_name = 'backscatter'
backscatter = _make_matplotlib_linearsegcmap_from_csv_file(_cmap_name, _datadir)
"""A continuous perceptually uniform colormap, with over and under range colors, specifically 
selected to highlight cloud, aerosol and molecular particulate atmospheric features in 
attenuated backscatter data such as is provided by the CALIOP lidar and other similar elastic 
backscatter lidars."""
backscatter_r = _make_matplotlib_linearsegcmap_from_csv_file(_cmap_name, _datadir, reverse=True)
"""A reversed version of the 'backscatter' colormap."""

_cmap_name = 'backscatter_18'
backscatter_18 = _make_matplotlib_linearsegcmap_from_csv_file(_cmap_name, _datadir)
"""A discrete colormap with 18 colors, including over and under range colors, specifically 
selected to highlight cloud, aerosol and molecular particulate atmospheric features 
in attenuated backscatter data such as is provided by the CALIOP lidar and other similar elastic 
backscatter lidars."""
BACKSCATTER_DISCRETE_BOUNDS = [
    1e-5, 1e-4, 3e-4, 6e-4, 1e-3, 1.5e-3, 2e-3, 3e-3, 4e-3, 5e-3, 6e-3, 8e-3,
    1e-2, 1.5e-2, 2e-2, 3e-2, 5e-2]
"""Boundary limits specifically designed to highlight particulate atmospheric 
features in the attenuated backscatter data provided by the CALIOP lidar and other similar 
elastic backscatter lidars."""
backscatter_18_norm = matplotlib.colors.BoundaryNorm(
    BACKSCATTER_DISCRETE_BOUNDS, len(BACKSCATTER_DISCRETE_BOUNDS)-1)
"""A matplotlib.colors.BoundaryNorm object initialized with the BACKSCATTER_DISCRETE_BOUNDS 
and designed to use with the 'backscatter_18' colormap."""

_cmap_name = 'backscatter_242'
backscatter_242 = _make_matplotlib_linearsegcmap_from_csv_file(_cmap_name, _datadir)
"""A continuous colormap, with over and under range colors, specifically selected 
to highlight cloud, aerosol and molecular particulate atmospheric features in 
attenuated backscatter data such as is provided by the CALIOP lidar and other similar elastic 
backscatter lidars."""
_NB_COLORS_BETWEEN_MID_DISCRETE_BIN = 15
_bounds = np.array(())
for _i in range(len(BACKSCATTER_DISCRETE_BOUNDS)-1): # color of discrete bounds at the mid value of the range bin
    _bounds = np.append(_bounds, np.linspace(BACKSCATTER_DISCRETE_BOUNDS[_i], BACKSCATTER_DISCRETE_BOUNDS[_i+1], _NB_COLORS_BETWEEN_MID_DISCRETE_BIN+1)[:-1])
_bounds = np.append(_bounds, BACKSCATTER_DISCRETE_BOUNDS[-1])
_backscatter_continuous_bounds = _bounds.tolist()
backscatter_242_norm = matplotlib.colors.BoundaryNorm(
    _backscatter_continuous_bounds, len(_backscatter_continuous_bounds)-1)
"""A matplotlib.colors.BoundaryNorm object initialized with the DEPOLARIZATION_DISCRETE_BOUNDS 
and designed to use with the 'backscatter_242' colormap."""

_cmap_name = 'depol'
depol = _make_matplotlib_linearsegcmap_from_csv_file(_cmap_name, _datadir)
"""A continuous perceptually uniform colormap, with over and under range colors, specifically 
selected to highlight cloud, aerosol and molecular particulate atmospheric features in 
depolarization ratio data such as is provided by the CALIOP lidar and other similar 
elastic backscatter lidars."""
depol_r = _make_matplotlib_linearsegcmap_from_csv_file(_cmap_name, _datadir, reverse=True)
"""A reversed version of the 'depol' colormap."""

_cmap_name = 'depol_8'
depol_8 = _make_matplotlib_linearsegcmap_from_csv_file(_cmap_name, _datadir)
"""A discrete colormap with 8 colors, including over and under range colors, specifically 
selected to highlight cloud, aerosol and molecular particulate atmospheric features 
in depolarization ratio data such as is provided by the CALIOP lidar and other 
similar elastic backscatter lidars."""
DEPOL_DISCRETE_BOUNDS = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
"""Boundary limits specifically designed to highlight particulate atmospheric 
features in the depolarization ratio data provided by the CALIOP lidar and other 
similar elastic backscatter lidars."""
depol_8_norm = matplotlib.colors.BoundaryNorm(
    DEPOL_DISCRETE_BOUNDS, len(DEPOL_DISCRETE_BOUNDS)-1)
"""A matplotlib.colors.BoundaryNorm object initialized with the DEPOLARIZATION_DISCRETE_BOUNDS 
and designed to use with the 'depol_8' colormap."""

_cmap_name = 'colorratio'
colorratio = _make_matplotlib_linearsegcmap_from_csv_file(_cmap_name, _datadir)
"""A continuous perceptually uniform colormap, with over and under range colors, to highlight 
particulate atmospheric features in the 1064 nm/532 nm color ratio data such as 
are provided by the CALIOP lidar and other similar elastic backscatter lidars."""
colorratio_r = _make_matplotlib_linearsegcmap_from_csv_file(_cmap_name, _datadir, reverse=True)
"""A reversed version of the 'colorratio' colormap."""

_cmap_name = 'colorratio_9'
colorratio_9 = _make_matplotlib_linearsegcmap_from_csv_file(_cmap_name, _datadir)
"""A discrete colormap of 9 colors, including over and under range colors, to highlight 
particulate atmospheric features in the 1064 nm/532 nm color ratio data such as 
are provided by the CALIOP lidar and other similar elastic backscatter lidars."""
COLORRATIO_DISCRETE_BOUNDS = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.6]
"""Boundary limits specifically designed to highlight particulate atmospheric 
features in the 1064 nm/532 nm color ratio data such as are provided by the CALIOP 
lidar and other similar elastic backscatter lidars."""
colorratio_9_norm = matplotlib.colors.BoundaryNorm(
    COLORRATIO_DISCRETE_BOUNDS, len(COLORRATIO_DISCRETE_BOUNDS)-1)
"""A matplotlib.colors.BoundaryNorm object initialized with the COLORRATIO_DISCRETE_BOUNDS 
and designed to use with the 'colorratio_9' colormap."""
