# cmlidar

A package that contains colormaps for commonly used atmospheric lidar parameters:


#### Color ratio colormaps

- `colorratio`: A sequential perceptually uniform colormap 

- `colorratio_discrete`: A discrete colormap of 9 colors to use with the color boundaries `[0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.6]` to highlight particulate atmospheric features such as are seen by the CALIOP lidar and other similar elastic backscatter lidars.


#### Depolarization ratio colormaps

- `depolarization`: A sequential perceptually uniform colormap

- `depolarization_discrete`: A discrete colormap of 8 colors to use with the color boundaries `[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]` to highlight particulate atmospheric features such as are seen by the CALIOP lidar and other similar elastic backscatter lidars.


#### Attenuated backscatter colormaps

- `backscatter`: A sequential perceptually uniform colormap

- `backscatter_discrete`: A discrete colormap of 8 colors to use with the color boundaries `[0.00001, 0.0001, 0.0003, 0.0006, 0.001, 0.0015, 0.002, 0.003, 0.004, 0.005, 0.006, 0.008, 0.01, 0.015, 0.02, 0.03, 0.05]` to highlight particulate atmospheric features such as are seen by the CALIOP lidar and other similar elastic backscatter lidars.

- `backscatter_continuous`: A continuous version of the discrete colormap keeping the contrast variations of the discrete colormap


## Install

To install this package, use the following command:

`pip install cmlidar`


##  RGB values

RGB values of the colormaps are provided in CSV files under cmlidar/rgb/.