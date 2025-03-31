import xarray as xr
import numpy as np

def set_regions(source='RECCAP2'):
    
    if source == 'RECCAP2':
        reg_ds = xr.open_dataset('RECCAP2_region_masks_all_v20221025.nc')
        region_dict = dict()
        for oce in ['arctic','atlantic','pacific','indian','southern']:#,'open_ocean','coast']:
            dummy_mask = reg_ds[oce]
            for idx in range(1,np.max(dummy_mask.values)+1):
                dummy_mask2 = xr.where(dummy_mask==idx,1,0)
                region_dict[f'{oce}{int(idx)}'] = dummy_mask2
     
        region_lookup_dict = dict()
        region_lookup_dict['arctic1'] = 'central Arctic'
        region_lookup_dict['arctic2'] = 'East Greenland'
        region_lookup_dict['arctic3'] = 'Baffin Bay'
        region_lookup_dict['arctic4'] = 'Canadian Archipelago'
        region_lookup_dict['arctic5'] = 'Canadian North Coast'
        region_lookup_dict['arctic6'] = 'Chukchi Sea'
        region_lookup_dict['arctic7'] = 'East Siberian Sea'
        region_lookup_dict['arctic8'] = 'Laptev Sea'
        region_lookup_dict['arctic9'] = 'Kara Sea'
        region_lookup_dict['arctic10'] = 'Barents Sea'
        region_lookup_dict['atlantic1'] = 'subpolar North Atlantic'
        region_lookup_dict['atlantic2'] = 'intergyre North Atlantic'
        region_lookup_dict['atlantic3'] = 'subtropical North Atlantic'
        region_lookup_dict['atlantic4'] = 'tropical Atlantic'
        region_lookup_dict['atlantic5'] = 'subtropical South Atlantic'
        region_lookup_dict['atlantic6'] = 'Mediterranean Sea'
        region_lookup_dict['pacific1'] = 'subpolar North Pacific'
        region_lookup_dict['pacific2'] = 'intergyre North Pacific'
        region_lookup_dict['pacific3'] = 'subtropical North Pacific'
        region_lookup_dict['pacific4'] = 'western tropical Pacific'
        region_lookup_dict['pacific5'] = 'eastern tropical Pacific'
        region_lookup_dict['pacific6'] = 'subtropical South Pacific'
        region_lookup_dict['indian1'] = 'Arabian Sea'
        region_lookup_dict['indian2'] = 'Bay of Bengal'
        region_lookup_dict['indian3'] = 'tropical Indian Ocean'
        region_lookup_dict['indian4'] = 'subtropical South Indian Ocean'
        region_lookup_dict['southern1'] = 'Subantarctic Zone'
        region_lookup_dict['southern2'] = 'Polar Front Zone'
        region_lookup_dict['southern3'] = 'Antarctic Zone'
    else:
        raise Exception('Other mask sources not yet implemented.')
    
    return region_dict, region_lookup_dict

