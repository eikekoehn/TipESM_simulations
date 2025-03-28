import os
import xarray as xr
from cdo import Cdo

def cdo_remapdis(da,method='remapdis'):

    cdo = Cdo()

    # define some dummy filenames
    dummy_tmpfile_1 = 'dummy_tmp1.nc'
    dummy_tmpfile_2 = 'dummy_tmp2.nc'
    
    # Make sure that the dummy files do not exist
    if os.path.exists(dummy_tmpfile_1):
        os.remove(dummy_tmpfile_1)
    if os.path.exists(dummy_tmpfile_2):
        os.remove(dummy_tmpfile_2)
    
    # Do the regridding
    da.to_netcdf(dummy_tmpfile_1)
    if method == 'remapdis':
        cdo.remapdis('r360x180', input=dummy_tmpfile_1, output=dummy_tmpfile_2)
    elif method:
        cdo.remapbil('r360x180', input=dummy_tmpfile_1, output=dummy_tmpfile_2)
    else:
        raise Exception('Regridding method not yet implemented.')
    da_gr = xr.open_dataset(dummy_tmpfile_2)
    
    # Delet the temporary files
    os.remove(dummy_tmpfile_1)
    os.remove(dummy_tmpfile_2)

    return da_gr
