
# Atomic covalent radius data
# http://www.periodictable.com/Properties/A/CovalentRadius.an.html
# Updated Jun. 9th, 2016

class AtomicWeight(object):
    x = {
        "H":     1.0079, "He":    4.0026, "Li":    6.941, "Be":    9.0122, "B":    10.811, "C":    12.0107,
        "N":    14.0067, "O":    15.9994, "F":    18.9984, "Ne":   20.1797, "Na":   22.9897, "Mg":   24.305,
        "Al":   26.9815, "Si":   28.0855, "P":    30.9738, "S":    32.065, "Cl":   35.453, "Ar":   39.948,
        "K":    39.0983, "Ca":   40.078, "Sc":   44.9559, "Ti":   47.867, "V":    50.9415, "Cr":   51.9961,
        "Mn":   54.938, "Fe":   55.845, "Co":   58.9332, "Ni":   58.6934, "Cu":   63.546, "Zn":   65.39	 ,
        "Ga":   69.723 , "Ge":   72.64	 , "As":   74.9216, "Se":   78.96	 , "Br":   79.904, "Kr":   83.8	 ,
        "Rb":   85.4678, "Sr":   87.62	 , "Y":    88.9059, "Zr":   91.224, "Nb":   92.9064, "Mo":   95.94,
        "Tc":   98	   , "Ru":   101.07, "Rh":   102.90, "Pd":   106.42, "Ag":   107.868, "Cd":   112.411,
        "In":   114.818, "Sn":   118.71, "Sb":   121.76, "Te":   127.6  , "I":    126.904, "Xe":   131.293,
        "Cs":   132.905, "Ba":   137.327, "La":   138.905, "Ce":   140.116, "Pr":   140.907, "Nd":   144.24,
        "Pm":   145	   , "Sm":   150.36, "Eu":   151.964, "Gd":   157.25, "Tb":   158.925, "Dy":   162.5	 ,
        "Ho":   164.930, "Er":   167.259, "Tm":   168.934, "Yb":   173.04, "Lu":  174.967	, "Hf":  178.49	,
        "Ta":  180.9479, "W":   183.84	, "Re":  186.207	, "Os":  190.23	, "Ir":  192.217	, "Pt":  195.078	,
        "Au":  196.9665, "Hg":  200.59	, "Tl":  204.3833, "Pb":  207.2   , "Bi":  208.9804, "Po":  209     ,
        "At":  210     , "Rn":  222     , "Fr":  223     , "Ra":  226     , "Ac":  227     , "Th":  232.0381,
        "Pa":  231.0359, "U":   238.0289, "Np":  237     , "Pu":  244     , "Am":  243     , "Cm":  247     ,
        "Bk":  247     , "Cf":  251     , "Es":  252     , "Fm":  257     , "Md":  258     , "No":  259     ,
        "Lr":  262     , "Rf":  261     , "Db":  262     , "Sg":  266     , "Bh":  264     , "Hs":  277     ,
        "Mt":  268     , "Ds":  281, "Rg":  272, "Uub": 285, "Uut": 284, "Uuq": 289,
        "Uup": 288, "Uuh": 292, "Uus": 0, "Uuo": 294, 
        "H.66": 1.0079, "H1.33": 1.0079
    }

class Covalent(object):
    x = { 
        "H":  0.37, "He": 0.32, "Li": 1.34, "Be": 0.90, "B":  0.82, "C":  0.77, 
        "N":  0.75, "O":  0.73, "F":  0.71, "Ne": 0.69, "Na": 1.54, "Mg": 1.30, 
        "Al": 1.18, "Si": 1.11, "P":  1.06, "S":  1.02, "Cl": 0.99, "Ar": 0.97, 
        "K":  1.96, "Ca": 1.74, "Sc": 1.44, "Ti": 1.36, "V":  1.25, "Cr": 1.27, 
        "Mn": 1.39, "Fe": 1.25, "Co": 1.26, "Ni": 1.21, "Cu": 1.38, "Zn": 1.31, 
        "Ga": 1.26, "Ge": 1.22, "As": 1.19, "Se": 1.16, "Br": 1.14, "Kr": 1.10, 
        "Rb": 2.11, "Sr": 1.92, "Y":  1.62, "Zr": 1.48, "Nb": 1.37, "Mo": 1.45, 
        "Tc": 1.56, "Ru": 1.26, "Rh": 1.35, "Pd": 1.31, "Ag": 1.53, "Cd": 1.48, 
        "In": 1.44, "Sn": 1.41, "Sb": 1.38, "Te": 1.35, "I":  1.33, "Xe": 1.30, 
        "Cs": 2.25, "Ba": 1.98, "La": 1.69, "Ce": 0.00, "Pr": 0.00, "Nd": 0.00, 
        "Pm": 0.00, "Sm": 0.00, "Eu": 0.00, "Gd": 0.00, "Tb": 0.00, "Dy": 0.00, 
        "Ho": 0.00, "Er": 0.00, "Tm": 0.00, "Yb": 0.00, "Lu": 1.60, "Hf": 1.50, 
        "Ta": 1.38, "W":  1.46, "Re": 1.59, "Os": 1.28, "Ir": 1.37, "Pt": 1.28, 
        "Au": 1.44, "Hg": 1.49, "Tl": 1.48, "Pb": 1.47, "Bi": 1.46, "Po": 0.00, 
        "At": 0.00, "Rn": 1.45, "Fr": 0.00, "Ra": 0.00, "Ac": 0.00, "Th": 0.00, 
        "Pa": 0.00, "U":  0.00, "Np": 0.00, "Pu": 0.00, "Am": 0.00, "Cm": 0.00, 
        "Bk": 0.00, "Cf": 0.00, "Es": 0.00, "Fm": 0.00, "Md": 0.00, "No": 0.00, 
        "Lr": 0.00, "Rf": 0.00, "Db": 0.00, "Sg": 0.00, "Bh": 0.00, "Hs": 0.00, 
        "Mt": 0.00, "Ds": 0.00, "Rg": 0.00, "Uub": 0.00, "Uut": 0.00, "Uuq": 0.00, 
        "Uup": 0.00, "Uuh": 0.00, "Uus": 0.00, "Uuo": 0.00, "HX":  0.37, 
        "H.66": 0.37, "H1.33": 0.37
    }

class AtomicColor(object):
    x = { 
        "H":  "#f4f4f4", "He": "#d9ffff", "Li": "#cc80ff", "Be": "#c2ff00", "B":  "#ffb5b5", "C":  "#909090", 
        "N":  "#3050f8", "O":  "#ff0d0d", "F":  "#90e050", "Ne": "#b3e3f5", "Na": "#ab5cf2", "Mg": "#8aff00", 
        "Al": "#bfa6a6", "Si": "#f0c8a0", "P":  "#ff8000", "S":  "#ffff30", "Cl": "#1ff01f", "Ar": "#80d1e3", 
        "K":  "#8f40d4", "Ca": "#3dff00", "Sc": "#e6e6e6", "Ti": "#bfc2c7", "V":  "#a6a6ab", "Cr": "#8a99c7", 
        "Mn": "#9c7ac7", "Fe": "#e06633", "Co": "#f090a0", "Ni": "#50d050", "Cu": "#c88033", "Zn": "#7d80b0", 
        "Ga": "#c28f8f", "Ge": "#668f8f", "As": "#bd80e3", "Se": "#ffa100", "Br": "#a62929", "Kr": "#5cb8d1", 
        "Rb": "#702eb0", "Sr": "#00ff00", "Y":  "#94ffff", "Zr": "#94e0e0", "Nb": "#73c2c9", "Mo": "#54b5b5", 
        "Tc": "#3b9e9e", "Ru": "#248f8f", "Rh": "#0a7d8c", "Pd": "#006985", "Ag": "#c0c0c0", "Cd": "#ffd98f", 
        "In": "#a67573", "Sn": "#668080", "Sb": "#9e63b5", "Te": "#d47a00", "I":  "#940094", "Xe": "#429eb0", 
        "Cs": "#57178f", "Ba": "#00c900", "La": "#70d4ff", "Ce": "#ffffc7", "Pr": "#d9ffc7", "Nd": "#c7ffc7", 
        "Pm": "#a3ffc7", "Sm": "#8fffc7", "Eu": "#61ffc7", "Gd": "#45ffc7", "Tb": "#30ffc7", "Dy": "#1fffc7", 
        "Ho": "#00ff9c", "Er": "#00e675", "Tm": "#00d452", "Yb": "#00bf38", "Lu": "#00ab24", "Hf": "#4dc2ff", 
        "Ta": "#4da6ff", "W":  "#2194d6", "Re": "#267dab", "Os": "#266696", "Ir": "#175487", "Pt": "#d0d0e0", 
        "Au": "#ffd123", "Hg": "#b8b8d0", "Tl": "#a6544d", "Pb": "#575961", "Bi": "#9e4fb5", "Po": "#ab5c00", 
        "At": "#754f45", "Rn": "#428296", "Fr": "#420066", "Ra": "#007d00", "Ac": "#70abfa", "Th": "#00baff", 
        "Pa": "#00a1ff", "U":  "#008fff", "Np": "#0080ff", "Pu": "#006bff", "Am": "#545cf2", "Cm": "#785ce3", 
        "Bk": "#8a4fe3", "Cf": "#a136d4", "Es": "#b31fd4", "Fm": "#b31fba", "Md": "#b30da6", "No": "#bd0d87", 
        "Lr": "#c70066", "Rf": "#cc0059", "Db": "#d1004f", "Sg": "#d90045", "Bh": "#e00038", "Hs": "#e6002e", 
        "Mt": "#eb0026", "Ds": "#111111", "Rg": "#111111", "Uub": "#111111", "Uut": "#111111", "Uuq": "#111111", 
        "Uup": "#111111", "Uuh": "#111111", "Uus": "#111111", "Uuo": "#111111", 
        "H.66": "#f4f4f4", "H1.33": "#f4f4f4"
    }

LightElements = ['H', 'C', 'N', 'O']