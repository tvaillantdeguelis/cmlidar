import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FixedLocator, LogLocator
from pyhdf.SD import SD
from pyhdf.error import HDF4Error
import cmlidar


def get_data(hdf, key, do_squeeze=True):
    data = hdf.select(key).get()
    try:
        fillvalue = hdf.select(key).getfillvalue()
        data = np.ma.masked_where(data==fillvalue, data)
    except HDF4Error:
        print('')
    if do_squeeze:
        data = data.squeeze()
    return data


def lat_lon_xaxis(ax, lat, lon):
    # Lat/Lon x-axis
    ax.xaxis.set_minor_locator(MultipleLocator(1000000.)) # to remove minor ticks
    x_ticks = np.linspace(0, lat.size-1, 6, dtype=int)
    lat_ticks = []
    lon_ticks = []
    for x in x_ticks:
        latx = '%.2f° S' % np.abs(lat[x]) if lat[x] < 0 else '%.2f° N' % lat[x]
        lonx = '%.2f° W' % np.abs(lon[x]) if lon[x] < 0 else '%.2f° E' % lon[x]
        lat_ticks.append(latx)
        lon_ticks.append(lonx)
    plt.xticks([np.arange(lat.size)[x] for x in x_ticks],
               ['%s\n%s' % (lat_ticks[i], lon_ticks[i]) for i in range(len(lat_ticks))])
    plt.tick_params(axis='x', which='minor', bottom=False)
    return


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
        cbar.ax.text(1.5, bound, cbar_minor_label[j], va='center')
    cbar_major_label = ['$×10^{-5}$', '$×10^{-4}$', '$×10^{-3}$', '$×10^{-2}$']
    c_bar_major_values = np.array((1e-5, 1e-4, 1e-3, 1e-2))
    for j, bound in enumerate(c_bar_major_values):
        cbar.ax.text(2.5, bound, cbar_major_label[j], va='center')
    cbar.set_label(label=r"$\beta'$ (km$^{-1}$ sr$^{-1}$)", labelpad=40)
    return


if __name__ == "__main__":
    
    ##########################################################################
    # Load CALIOP variables
    ##########################################################################

    # CALIOP L1 data can be downloaded from https://doi.org/10.5067/CALIOP/CALIPSO/CAL_LID_L1-Standard-V4-51
    CALIOP_L1_FILEPATH = "/DATA/LIENS/CALIOP/CAL_LID_L1.v5.00/2009/2009_02_10/CAL_LID_L1-Standard-V5-00.2009-02-10T12-33-03ZN.hdf"
    INDEX_PROFILE_START = 30000
    INDEX_PROFILE_END = 50000
    INDEX_ALTITUDE_MAX = 80

    # Load data with various regular grid sizes
    hdf = SD(CALIOP_L1_FILEPATH)
    lat = get_data(hdf, 'Latitude')
    lon = get_data(hdf, 'Longitude')
    alt = get_data(hdf, 'Lidar_Data_Altitudes')
    tab_532 = get_data(hdf, 'Total_Attenuated_Backscatter_532')
    ab_532_per = get_data(hdf, 'Perpendicular_Attenuated_Backscatter_532')
    ab_1064 = get_data(hdf, 'Attenuated_Backscatter_1064')
    hdf.end()

    # Compute 532 nm perpendicular attenuated backscatter
    ab_532_par = tab_532 - ab_532_per


    ##########################################################################
    # Plot CALIOP variables with the cmlidar colormaps
    ##########################################################################

    # Parameters
    xarray = np.arange(INDEX_PROFILE_END-INDEX_PROFILE_START)
    alt_range = np.arange(INDEX_ALTITUDE_MAX, alt.size)
    prof_range = np.arange(INDEX_PROFILE_START, INDEX_PROFILE_END)

    # Create figure
    fig = plt.figure(figsize=(18, 15))

    # Plot 532 nm parallel attenuted backscatter
    ax = plt.subplot(321)
    pc = plt.pcolormesh(xarray, alt[alt_range], ab_532_par[np.ix_(prof_range, alt_range)].T, 
                        cmap=cmlidar.cm.backscatter_18, 
                        norm=cmlidar.cm.backscatter_18_norm, 
                        rasterized=True)
    plt.ylabel('Altitude (km)')
    lat_lon_xaxis(ax, lat[prof_range], lon[prof_range])
    plt.title("532 nm Parallel Attenuated Backscatter")
    cbar = plt.colorbar(extend='both', drawedges=True)
    backscatter_cbar_labels(cbar)

    # Plot 532 nm total attenuted backscatter
    ax = plt.subplot(323)
    pc = plt.pcolormesh(xarray, alt[alt_range], ab_532_per[np.ix_(prof_range, alt_range)].T, 
                        cmap=cmlidar.cm.backscatter_18, 
                        norm=cmlidar.cm.backscatter_18_norm, 
                        rasterized=True)
    plt.ylabel('Altitude (km)')
    lat_lon_xaxis(ax, lat[prof_range], lon[prof_range])
    plt.title("532 nm Perpendicular Attenuated Backscatter")
    cbar = plt.colorbar(extend='both', drawedges=True)
    backscatter_cbar_labels(cbar)

    # Plot 1064 nm attenuted backscatter
    ax = plt.subplot(325)
    pc = plt.pcolormesh(xarray, alt[alt_range], ab_1064[np.ix_(prof_range, alt_range)].T, 
                        cmap=cmlidar.cm.backscatter_18, 
                        norm=cmlidar.cm.backscatter_18_norm, 
                        rasterized=True)
    plt.ylabel('Altitude (km)')
    lat_lon_xaxis(ax, lat[prof_range], lon[prof_range])
    plt.title("1064 nm Attenuated Backscatter")
    cbar = plt.colorbar(extend='both', drawedges=True)
    backscatter_cbar_labels(cbar)

    # Plot total 532 nm attenuted backscatter
    ax = plt.subplot(322)
    pc = plt.pcolormesh(xarray, alt[alt_range], tab_532[np.ix_(prof_range, alt_range)].T, 
                        cmap=cmlidar.cm.backscatter_18, 
                        norm=cmlidar.cm.backscatter_18_norm, 
                        rasterized=True)
    plt.ylabel('Altitude (km)')
    lat_lon_xaxis(ax, lat[prof_range], lon[prof_range])
    plt.title("532 nm Total Attenuated Backscatter")
    cbar = plt.colorbar(extend='both', drawedges=True)
    backscatter_cbar_labels(cbar)

    # Plot depolarization ratio
    ax = plt.subplot(324)
    pc = plt.pcolormesh(xarray, alt[alt_range], ab_532_per[np.ix_(prof_range, alt_range)].T/ab_532_par[np.ix_(prof_range, alt_range)].T, 
                        cmap=cmlidar.cm.depol_8, 
                        norm=cmlidar.cm.depol_8_norm, 
                        rasterized=True)
    plt.ylabel('Altitude (km)')
    lat_lon_xaxis(ax, lat[prof_range], lon[prof_range])
    plt.title("Depolarization Ratio")
    cbar = plt.colorbar(extend='both', drawedges=True)
    cbar.set_label(label=r"Depolarization Ratio")

    # Plot color ratio
    ax = plt.subplot(326)
    pc = plt.pcolormesh(xarray, alt[alt_range], ab_1064[np.ix_(prof_range, alt_range)].T/tab_532[np.ix_(prof_range, alt_range)].T, 
                        cmap=cmlidar.cm.colorratio_9, 
                        norm=cmlidar.cm.colorratio_9_norm, 
                        rasterized=True)
    plt.ylabel('Altitude (km)')
    lat_lon_xaxis(ax, lat[prof_range], lon[prof_range])
    plt.title("Color Ratio")
    cbar = plt.colorbar(extend='both', drawedges=True)
    cbar.set_label(label=r"Color Ratio")

    # Save figure
    plt.tight_layout()
    plt.savefig('./examples/caliop_plots.png')