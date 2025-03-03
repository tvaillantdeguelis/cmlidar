# cmlidar

A package that contains colormaps for commonly used atmospheric lidar parameters:


#### Color ratio colormaps

- `colorratio`: A sequential perceptually uniform colormap.

- `colorratio_9`: A discrete colormap of 9 colors to use with the color boundaries `[0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.6]` (`cmlidar.cm.COLORRATIO_DISCRETE_BOUNDS`) to highlight particulate atmospheric features such as are seen by the CALIOP lidar and other similar elastic backscatter lidars. Can be used with BoundaryNorm: `colorratio_9_norm`.


#### Depolarization ratio colormaps

- `depol`: A sequential perceptually uniform colormap.

- `depol_8`: A discrete colormap of 8 colors to use with the color boundaries `[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]` (`cmlidar.cm.DEPOLARIZATION_DISCRETE_BOUNDS`) to highlight particulate atmospheric features such as are seen by the CALIOP lidar and other similar elastic backscatter lidars. Can be used with BoundaryNorm: `depol_8_norm`.


#### Attenuated backscatter colormaps

- `backscatter`: A sequential perceptually uniform colormap.

- `backscatter_18`: A discrete colormap of 8 colors to use with the color boundaries `[1e-5, 1e-4, 3e-4, 6e-4, 1e-3, 1.5e-3, 2e-3, 3e-3, 4e-3, 5e-3, 6e-3, 8e-3, 1e-2, 1.5e-2, 2e-2, 3e-2, 5e-2]` (`cmlidar.cm.BACKSCATTER_DISCRETE_BOUNDS`) to highlight particulate atmospheric features such as are seen by the CALIOP lidar and other similar elastic backscatter lidars. Can be used with BoundaryNorm: `backscatter_18_norm`.

- `backscatter_242`: A continuous version of the discrete colormap keeping the contrast variations of the discrete colormap. Can be used with BoundaryNorm: `backscatter_242_norm`.


## Install

To install this package, use the following command:

`pip install cmlidar`


## RGB values

RGB values of the colormaps are provided in CSV files under cmlidar/rgb/.


## Examples

A script example showing how to use these colormaps with the color boundaries is provided in "example/plot.py".