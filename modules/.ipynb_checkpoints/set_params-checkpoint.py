class VarSimuObject:
    def __init__(self, **attributes):
        """
        Initialize a new instance of the VarSimuObject class.
        :param attributes: Dictionary of attributes to set on the instance.
        """
        for key, value in attributes.items():
            setattr(self, key, value)

def get_IPSL_simulation_set(var,domain,grid,frequency):
    rparams = dict()
    color_cycle = ["#3f90da", "#ffa90e", "#bd1f01", "#94a4a2", "#832db6", "#a96b59", "#e76300", "#b9ac70", "#717581", "#92dadd"] # https://github.com/matplotlib/matplotlib/issues/9460
    
    # Historical runs
    rparams['esm_hist_r1'] = VarSimuObject(variable=var,
                                mip='CMIP',
                                institute = 'IPSL',
                                model = 'IPSL-CM6-ESMCO2',
                                experiment = 'esm-hist',
                                member = 'r1i1p3f1',
                                domain = domain,
                                frequency = frequency,
                                grid = grid,
                                #version = 'latest_manual',
                                id_color = color_cycle[0]
                                )
    
    rparams['esm_hist_r2'] = VarSimuObject(variable=var,
                                mip='CMIP',
                                institute = 'IPSL',
                                model = 'IPSL-CM6-ESMCO2',
                                experiment = 'esm-hist',
                                member = 'r2i1p3f1',
                                domain = domain,
                                frequency = frequency,
                                grid = grid,
                                #version = 'latest_manual',
                                id_color = color_cycle[1]
                                )
    
    rparams['esm_hist_r3'] = VarSimuObject(variable=var,
                                mip='CMIP',
                                institute = 'IPSL',
                                model = 'IPSL-CM6-ESMCO2',
                                experiment = 'esm-hist',
                                member = 'r3i1p3f1',
                                domain = domain,
                                frequency = frequency,
                                grid = grid,
                                #version = 'latest_manual',
                                id_color = color_cycle[2]
                                )
    
    
    rparams['esm_hist_r4'] = VarSimuObject(variable=var,
                                mip='CMIP',
                                institute = 'IPSL',
                                model = 'IPSL-CM6-ESMCO2',
                                experiment = 'esm-hist',
                                member = 'r4i1p3f1',
                                domain = domain,
                                frequency = frequency,
                                grid = grid,
                                #version = 'latest_manual',
                                id_color = color_cycle[3]
                                )
    # PiControl run
    rparams['esm_pic_r1'] = VarSimuObject(variable=var,
                                mip='CMIP',
                                institute = 'IPSL',
                                model = 'IPSL-CM6-ESMCO2',
                                experiment = 'esm-piControl',
                                member = 'r1i1p3f1',
                                domain = domain,
                                frequency = frequency,
                                grid = grid,
                                #version = 'latest_manual',
                                id_color = color_cycle[4]
                                )
    
    # Rampup run
    rparams['esm_rampup'] = VarSimuObject(variable=var,
                                mip='TIPMIP',
                                institute = 'IPSL',
                                model = 'IPSL-CM6-ESMCO2',
                                experiment = 'esm-up2p0',
                                member = 'r1i1p3f1',
                                domain = domain,
                                frequency = frequency,
                                grid = grid,
                                #version = 'latest_manual',
                                id_color = color_cycle[5]
                                )
    
    # Sabilizations
    rparams['esm_stab_1p5'] = VarSimuObject(variable=var,
                                mip='TIPMIP',
                                institute = 'IPSL',
                                model = 'IPSL-CM6-ESMCO2',
                                experiment = 'esm-up2p0-gwl1p5',
                                member = 'r1i1p3f1',
                                domain = domain,
                                frequency = frequency,
                                grid = grid,
                                #version = 'latest_manual',
                                id_color = color_cycle[6]
                                )
    
    rparams['esm_stab_2p0'] = VarSimuObject(variable=var,
                                mip='TIPMIP',
                                institute = 'IPSL',
                                model = 'IPSL-CM6-ESMCO2',
                                experiment = 'esm-up2p0-gwl2p0',
                                member = 'r1i1p3f1',
                                domain = domain,
                                frequency = frequency,
                                grid = grid,
                                #version = 'latest_manual',
                                id_color = color_cycle[7]
                                )
    
    rparams['esm_stab_3p0'] = VarSimuObject(variable=var,
                                mip='TIPMIP',
                                institute = 'IPSL',
                                model = 'IPSL-CM6-ESMCO2',
                                experiment = 'esm-up2p0-gwl3p0',
                                member = 'r1i1p3f1',
                                domain = domain,
                                frequency = frequency,
                                grid = grid,
                                #version = 'latest_manual',
                                id_color = color_cycle[8]
                                )
    
    rparams['esm_stab_4p0'] = VarSimuObject(variable=var,
                                mip='TIPMIP',
                                institute = 'IPSL',
                                model = 'IPSL-CM6-ESMCO2',
                                experiment = 'esm-up2p0-gwl4p0',
                                member = 'r1i1p3f1',
                                domain = domain,
                                frequency = frequency,
                                grid = grid,
                                #version = 'latest_manual',
                                id_color = color_cycle[9]
                                )
    
    return rparams