csv_pt = """Park Name,City,Pond,Fountain,LAT,LNG,ELEV,GEOMETRY_PT
Post office Square,Boston,FALSE,TRUE,42.356243,-71.055631,2.0,"[-71.055631, 42.356243, 2.0]"
Boston Common,Boston,TRUE,TRUE,42.355465,-71.066412,10.0,"[-71.066412, 42.355465, 10.0]"""

csv_ls = """Park Name,Feature Description,GEOMETRY_LS
Post Office Square,A walk by the fountain,"[[-71.055685, 42.356716, 0.0], [-71.055769, 42.356587, 0.0], [-71.055754, 42.356566, 0.0], [-71.055746, 42.356539, 0.0], [-71.055757, 42.356511, 0.0], [-71.05579, 42.356495, 0.0], [-71.05583, 42.356485, 0.0], [-71.055842, 42.356389, 0.0], [-71.055796, 42.356252, 0.0], [-71.055642, 42.356046, 0.0], [-71.055697, 42.355876, 0.0], [-71.055758, 42.355828, 0.0]]"
Boston Common,A walk by the fountain,"[[-71.062737, 42.356251, 0.0], [-71.063012, 42.35621, 0.0], [-71.06305, 42.356153, 0.0], [-71.063115, 42.356144, 0.0], [-71.063261, 42.356136, 0.0], [-71.064018, 42.355825, 0.0]]"
"""

csv_poly = """Park Name,Feature Description,GEOMETRY_POLY
Post Office Square,Boundary of Post Office Square with holes for buildings,"[[[-71.055757, 42.356856, 0.0], [-71.054976, 42.35608, 0.0], [-71.055636, 42.355697, 0.0], [-71.055941, 42.356003, 0.0], [-71.05622, 42.356767, 0.0], [-71.055757, 42.356856, 0.0]], [[-71.055522, 42.355955, 0.0], [-71.055458, 42.355894, 0.0], [-71.055546, 42.355846, 0.0], [-71.055615, 42.355908, 0.0], [-71.055522, 42.355955, 0.0]], [[-71.055312, 42.356089, 0.0], [-71.055226, 42.356005, 0.0], [-71.055288, 42.355969, 0.0], [-71.055373, 42.356058, 0.0], [-71.055312, 42.356089, 0.0]]]"
Boston Common,Boundary of Boston Common with a hole for the Frog Pond,"[[[-71.062157, 42.356514, 0.0], [-71.063337, 42.355222, 0.0], [-71.064638, 42.352457, 0.0], [-71.067238, 42.352639, 0.0], [-71.06915, 42.356132, 0.0], [-71.06326, 42.357591, 0.0], [-71.062157, 42.356514, 0.0]], [[-71.065045, 42.356047, 0.0], [-71.065107, 42.355953, 0.0], [-71.065249, 42.355911, 0.0], [-71.065909, 42.356018, 0.0], [-71.066016, 42.35601, 0.0], [-71.066198, 42.355918, 0.0], [-71.066417, 42.355854, 0.0], [-71.066521, 42.355876, 0.0], [-71.066564, 42.355938, 0.0], [-71.066547, 42.355985, 0.0], [-71.066, 42.356221, 0.0], [-71.065647, 42.356296, 0.0], [-71.065341, 42.35627, 0.0], [-71.065127, 42.356186, 0.0], [-71.065061, 42.356123, 0.0], [-71.065045, 42.356047, 0.0]]]"
"""

# CSVs that have been opened an parsed using csv.reader from Python's built-in csv module
pt_csv_parsed = [['Park Name', 'City', 'Pond', 'Fountain', 'GEOMETRY_PT'], ['Post office Square', 'Boston', 'FALSE', 'TRUE', '[-71.055631, 42.356243, 2.0]'], ['Boston Common', 'Boston', 'TRUE', 'TRUE', '[-71.066412, 42.355465, 10.0]']]

ls_csv_parsed = [['Park Name', 'Feature Description', 'GEOMETRY_LS'], ['Post Office Square', 'A walk by the fountain', '[[-71.055685, 42.356716, 0.0], [-71.055769, 42.356587, 0.0], [-71.055754, 42.356566, 0.0], [-71.055746, 42.356539, 0.0], [-71.055757, 42.356511, 0.0], [-71.05579, 42.356495, 0.0], [-71.05583, 42.356485, 0.0], [-71.055842, 42.356389, 0.0], [-71.055796, 42.356252, 0.0], [-71.055642, 42.356046, 0.0], [-71.055697, 42.355876, 0.0], [-71.055758, 42.355828, 0.0]]'], ['Boston Common', 'A walk by the fountain', '[[-71.062737, 42.356251, 0.0], [-71.063012, 42.35621, 0.0], [-71.06305, 42.356153, 0.0], [-71.063115, 42.356144, 0.0], [-71.063261, 42.356136, 0.0], [-71.064018, 42.355825, 0.0]]']]

poly_csv_parsed = [['Park Name', 'Feature Description', 'GEOMETRY_POLY'], ['Post Office Square', 'Boundary of Post Office Square with holes for buildings', '[[[-71.055757, 42.356856, 0.0], [-71.054976, 42.35608, 0.0], [-71.055636, 42.355697, 0.0], [-71.055941, 42.356003, 0.0], [-71.05622, 42.356767, 0.0], [-71.055757, 42.356856, 0.0]], [[-71.055522, 42.355955, 0.0], [-71.055458, 42.355894, 0.0], [-71.055546, 42.355846, 0.0], [-71.055615, 42.355908, 0.0], [-71.055522, 42.355955, 0.0]], [[-71.055312, 42.356089, 0.0], [-71.055226, 42.356005, 0.0], [-71.055288, 42.355969, 0.0], [-71.055373, 42.356058, 0.0], [-71.055312, 42.356089, 0.0]]]'], ['Boston Common', 'Boundary of Boston Common with a hole for the Frog Pond', '[[[-71.062157, 42.356514, 0.0], [-71.063337, 42.355222, 0.0], [-71.064638, 42.352457, 0.0], [-71.067238, 42.352639, 0.0], [-71.06915, 42.356132, 0.0], [-71.06326, 42.357591, 0.0], [-71.062157, 42.356514, 0.0]], [[-71.065045, 42.356047, 0.0], [-71.065107, 42.355953, 0.0], [-71.065249, 42.355911, 0.0], [-71.065909, 42.356018, 0.0], [-71.066016, 42.35601, 0.0], [-71.066198, 42.355918, 0.0], [-71.066417, 42.355854, 0.0], [-71.066521, 42.355876, 0.0], [-71.066564, 42.355938, 0.0], [-71.066547, 42.355985, 0.0], [-71.066, 42.356221, 0.0], [-71.065647, 42.356296, 0.0], [-71.065341, 42.35627, 0.0], [-71.065127, 42.356186, 0.0], [-71.065061, 42.356123, 0.0], [-71.065045, 42.356047, 0.0]]]']]
