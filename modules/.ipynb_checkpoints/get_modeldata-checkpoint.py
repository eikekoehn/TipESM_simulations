import os
import re
import glob
import xarray as xr

def get_modelfiles(rparam):
    """
    Get list of TipESM filenames and corresponding list of models for the given attributes of rparam
    """

    root_dir = '/thredds/tgcc/store/torreso/CMIP6Plus/'

    if rparam.mip == 'CMIP':
        mip = 'CMIP'
    elif rparam.mip == 'TIPMIP':
        mip = 'TIPMIP'

    institute = rparam.institute
    model = rparam.model
    experiment = rparam.experiment
    member = rparam.member
    extended_root_path = f'{root_dir}{mip}/{institute}/{model}/{experiment}/{member}'
    
    domain = rparam.domain
    frequency = rparam.frequency
    variable = rparam.variable
    grid = rparam.grid
    #version = rparam.version

    full_path = f'{extended_root_path}/{domain}{frequency}/{variable}/{grid}/'

    full_path = get_latest_version_folder(full_path)

    filenames = sorted(glob.glob(f'{full_path}/*.nc'))

    rparam.filenames = filenames
    return rparam

def get_latest_version_folder(base_path):
    # Regex pattern to match folders like vYYYYMMDD
    date_pattern = re.compile(r"^v(\d{8})$")

    # List all directories in the base path
    folders = [f for f in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, f))]

    # Extract valid date folders
    date_folders = [f for f in folders if date_pattern.match(f)]

    if not date_folders:
        raise ValueError("No date folders found matching the pattern vYYYYMMDD")

    # Get the latest folder by comparing the date part
    latest_folder = max(date_folders, key=lambda f: date_pattern.match(f).group(1))

    return os.path.join(base_path, latest_folder)


def get_areaweights(rparam):
    """
    Get area weights.
    """

    if rparam.institute == 'IPSL' and rparam.domain == 'O' and rparam.grid == 'gn':
        # note that this is not the ideal path, but it should be correct. Need to backcheck.
        area_file = '/bdd/CMIP6/CMIP/IPSL/IPSL-CM6A-LR/1pctCO2/r1i1p1f1/Ofx/areacello/gn/latest/areacello_Ofx_IPSL-CM6A-LR_1pctCO2_r1i1p1f1_gn.nc'
    else:
        raise Exception('The area weights are not yet included for this rparam set.')
    area_ds = xr.open_dataset(area_file)
    area_ds = area_ds.rename({'y': 'j','x': 'i'})
    areacello = area_ds.areacello
    area = area_ds.area

    rparam.areacello = areacello
    rparam.area = area

    return rparam

