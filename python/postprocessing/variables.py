import math
class variable(object):
    def __init__(self,name,title,taglio=None,nbins = None, xmin= None, xmax= None, xarray = None,MConly = False, noUnOvFlowbin = False):
        self._name = name
        self._title = title
        self._taglio = taglio
        self._nbins = nbins
        self._xmin = xmin
        self._xmax = xmax
        self._xarray = xarray
        self._MConly = MConly
        self._noUnOvFlowbin = noUnOvFlowbin  

requirements = ""

vars = []

vars.append(variable(name="h_Top_M_", title="Top mass reconstructed", nbins=20, xmin=0, xmax=300))
vars.append(variable(name="h_MtW_", title="W transverse mass", nbins=20, xmin=0, xmax=300))
vars.append(variable(name="h_nEta_", title="|eta Foward Jet|", nbins=8, xmin=0, xmax=5))
vars.append(variable(name="h_M_light_", title="Light jet mass + lepton", nbins=20, xmin=0, xmax=300))
vars.append(variable(name="h_M_b_Jet_", title="b-jet mass + lepton", nbins=20, xmin=0, xmax=300))
vars.append(variable(name="h_M_extra_Jet_", title="Extra jet mass", nbins=20, xmin=0, xmax=300))
vars.append(variable(name="h_Missing_", title="Missing transverse energy", nbins=20, xmin=0, xmax=300))
vars.append(variable(name="h_Helicity_", title="Helicity angle", nbins=20, xmin=-1, xmax=1))
vars.append(variable(name="h_Polarization_", title="Polarization angle", nbins=20, xmin=-1, xmax=1))
vars.append(variable(name="h_Helicitt_", title="Helicity angle", nbins=20, xmin=-1, xmax=1))
vars.append(variable(name="h_Tag_score_bjet_", title="b-tag score", nbins=20, xmin=0, xmax=1))
vars.append(variable(name="h_Difference_eta_bjet_", title="|eta b jet difference|", nbins=20, xmin=0, xmax=5))
vars.append(variable(name="h_Missing_Energy_",title="Missing_energy", nbins=20,xmin=0,xmax=250))


regions = {
    "2j1b_Muon"            : "2 jets, 1 b-tag, Muon channel",
    "2j1b_Electron"        : "2 jets, 1 b-tag, Electron channel",
    "3j1b_Muon"            : "3 jets, 1 b-tag, Muon channel",
    "3j1b_Electron"        : "3 jets, 1 b-tag, Electron channel",
    "3j2b_Muon"            : "3 jets, 2 b-tags, Muon channel",
    "3j2b_Electron"        : "3 jets, 2 b-tags, Electron channel",
    "bjet_3j1b_Muon"       : "b-jet kinematics, 3j1b, Muon",
    "bjet_3j1b_Electron"   : "b-jet kinematics, 3j1b, Electron",
    "extra_3j1b_Muon"      : "Extra jet kinematics, 3j1b, Muon",
    "extra_3j1b_Electron"  : "Extra jet kinematics, 3j1b, Electron",
    "foward_Jet_3j1b_Muon" : "Forward jet, 3j1b, Muon",
    "foward_Jet_3j1b_Electron" : "Forward jet, 3j1b, Electron",
    "foward_Jet_3j2b_Muon" : "Forward jet, 3j2b, Muon",
    "foward_Jet_3j2b_Electron" : "Forward jet, 3j2b, Electron",
    "Electron" : "Electron category",
    "Muon" : "Muon category"

}



#Name histo:


#Name_histo = {
#    "h_Top_M_2j1b" : "Top mass recostructed"
#    "h_MtW_2j1b_Muon" : "Trasverse Mass W"
#    ""




#}






#Rebbining:
"""
import array

Rebin = {
    # --- 2j1b Muon ---
    "h_Top_M_2j1b_Muon"             : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_MtW_2j1b_Muon"               : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_nEta_2j1b_Muon"              : array.array('d', [0, 0.5, 1, 1.5 ,2, 2.5, 3, 3.5, 4, 4.5, 5]),
    "h_M_light_2j1b_Muon"           : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_M_b_Jet_2j1b_Muon"           : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_Missing_Energy_2j1b_Muon"    : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_Helicity_2j1b_Muon"          : array.array('d', [-1, -0.5, 0, 0.5, 1]),
    "h_Polarization_2j1b_Muon"      : array.array('d', [-1, -0.5, 0, 0.5, 1]),

    # --- 2j1b Electron ---
    "h_Top_M_2j1b_Electron"         : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_MtW_2j1b_Electron"           : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_nEta_2j1b_Electron"          : array.array('d', [0, 0.5 ,1 , 1.5, 2, 2.5 , 3, 3.5, 4, 4.5, 5]),
    "h_M_light_2j1b_Electron"       : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_M_b_Jet_2j1b_Electron"       : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_Missing_Energy_2j1b_Electron": array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_Helicity_2j1b_Electron"      : array.array('d', [-1, -0.5, 0, 0.5, 1]),
    "h_Polarization_2j1b_Electron"  : array.array('d', [-1, -0.5, 0, 0.5, 1]),

    # --- 3j1b Muon ---
    "h_Top_M_bjet_3j1b_Muon"        : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_Top_M_extra_3j1b_Muon"       : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_MtW_3j1b_Muon"               : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_nEta_foward_Jet_3j1b_Muon"   : array.array('d', [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]),
    "h_M_b_Jet_3j1b_Muon"           : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_M_extra_Jet_3j1b_Muon"       : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_M_light_Jet_3j1b_Muon"       : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_Missing_3j1b_Muon"           : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_Helicity_btag_3j1b_Muon"     : array.array('d', [-1, -0.5, 0, 0.5, 1]),
    "h_Helicity_Extra_3j1b_Muon"    : array.array('d', [-1, -0.5, 0, 0.5, 1]),
    "h_Polarization_btag_3j1b_Muon" : array.array('d', [-1, -0.5, 0, 0.5, 1]),
    "h_Polarization_Extra_3j1b_Muon": array.array('d', [-1, -0.5, 0, 0.5, 1]),
    "h_Tag_score_bjet_3j1b_Muon"    : array.array('d', [0, 0.2, 0.4, 0.6, 0.8, 1]),

    # --- 3j1b Electron ---
    "h_Top_M_bjet_3j1b_Electron"        : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_Top_M_extra_3j1b_Electron"       : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_MtW_3j1b_Electron"               : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_nEta_foward_Jet_3j1b_Electron"   : array.array('d', [0, 0.5, 1, 1.5 , 2, 2.5, 3, 3.5, 4, 4.5, 5]),
    "h_M_b_Jet_3j1b_Electron"           : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_M_extra_Jet_3j1b_Electron"       : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_M_light_Jet_3j1b_Electron"       : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_Missing_3j1b_Electron"           : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_Helicity_btag_3j1b_Electron"     : array.array('d', [-1, -0.5, 0, 0.5, 1]),
    "h_Helicitt_Extra_3j1b_Electron"    : array.array('d', [-1, -0.5, 0, 0.5, 1]),  # typo mantenuto
    "h_Polarization_Extra_3j1b_Electron": array.array('d', [-1, -0.5, 0, 0.5, 1]),
    "h_Polarization_btag_3j1b_Electron" : array.array('d', [-1, -0.5, 0, 0.5, 1]),
    "h_Tag_score_bjet_3j1b_Electron"    : array.array('d', [0, 0.2, 0.4, 0.6, 0.8, 1]),

    # --- 3j2b Muon ---
    "h_Top_M_3j2b_Muon"              : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_MtW_3j2b_Muon"                : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_nEta_foward_Jet_3j2b_Muon"    : array.array('d', [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]),
    "h_M_light_Jet_3j2b_Muon"        : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_M_b_Jet_3j2b_Muon"            : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_Missing_Energy_3j2b_Muon"     : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_Helicity_3j2b_Muon"           : array.array('d', [-1, -0.5, 0, 0.5, 1]),
    "h_Polarization_3j2b_Muon"       : array.array('d', [-1, -0.5, 0, 0.5, 1]),
    "h_Difference_eta_bjet_Muon"     : array.array('d', [0, 1, 2, 3, 4, 5]),

    # --- 3j2b Electron ---
    "h_Top_M_3j2b_Electron"              : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_MtW_3j2b_Electron"                : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_nEta_foward_Jet_3j2b_Electron"    : array.array('d', [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]),
    "h_M_light_Jet_3j2b_Electron"        : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_M_b_Jet_3j2b_Electron"            : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_Missing_Energy_3j2b_Electron"     : array.array('d', [0, 50, 100, 150, 200, 300]),
    "h_Helicity_3j2b_Electron"           : array.array('d', [-1, -0.5, 0, 0.5, 1]),
    "h_Polarization_3j2b_Electron"       : array.array('d', [-1, -0.5, 0, 0.5, 1]),
    "h_Difference_eta_bjet_Electron"     : array.array('d', [0, 1, 2, 3, 4, 5]),
}
"""







"""
histogram_names = []

for var in vars:
    for region in regions.keys():
        full_name = f"{var._name}{region}"
        histogram_names.append(full_name)

# --- Stampa di controllo ---
print("Totale istogrammi generati:", len(histogram_names))
for h in histogram_names:
    print(h)
"""





