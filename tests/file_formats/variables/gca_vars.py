"""
Variables pertaining to GCA components and GCA conversion for use in testing.

"""

# Geom Types
pt_geom = 'PT'
ls_geom = 'LS'
poly_geom = 'POLY'

# POINT
pt_coords = [[-71.055631, 42.356243, 2.0], [-71.066412, 42.355465, 10.0]]
pt_attrs = [['Park Name', 'City', 'Pond', 'Fountain'], ['Post office Square', 'Boston', 'FALSE', 'TRUE'], ['Boston Common', 'Boston', 'TRUE', 'TRUE']]

pt_features = [(['Post office Square', 'Boston', 'FALSE', 'TRUE'], [-71.055631, 42.356243, 2.0]), (['Boston Common', 'Boston', 'TRUE', 'TRUE'], [-71.066412, 42.355465, 10.0])]


# LINESTRING
ls_coords = [[[-71.055685, 42.356716, 0.0], [-71.055769, 42.356587, 0.0], [-71.055754, 42.356566, 0.0], [-71.055746, 42.356539, 0.0], [-71.055757, 42.356511, 0.0], [-71.05579, 42.356495, 0.0], [-71.05583, 42.356485, 0.0], [-71.055842, 42.356389, 0.0], [-71.055796, 42.356252, 0.0], [-71.055642, 42.356046, 0.0], [-71.055697, 42.355876, 0.0], [-71.055758, 42.355828, 0.0]], [[-71.062737, 42.356251, 0.0], [-71.063012, 42.35621, 0.0], [-71.06305, 42.356153, 0.0], [-71.063115, 42.356144, 0.0], [-71.063261, 42.356136, 0.0], [-71.064018, 42.355825, 0.0]]]
ls_attrs = [['Park Name', 'Feature Description'], ['Post Office Square', 'A walk by the fountain'], ['Boston Common', 'A walk by the fountain']]

ls_features = [(['Post Office Square', 'A walk by the fountain'], [[-71.055685, 42.356716, 0.0], [-71.055769, 42.356587, 0.0], [-71.055754, 42.356566, 0.0], [-71.055746, 42.356539, 0.0], [-71.055757, 42.356511, 0.0], [-71.05579, 42.356495, 0.0], [-71.05583, 42.356485, 0.0], [-71.055842, 42.356389, 0.0], [-71.055796, 42.356252, 0.0], [-71.055642, 42.356046, 0.0], [-71.055697, 42.355876, 0.0], [-71.055758, 42.355828, 0.0]]), (['Boston Common', 'A walk by the fountain'], [[-71.062737, 42.356251, 0.0], [-71.063012, 42.35621, 0.0], [-71.06305, 42.356153, 0.0], [-71.063115, 42.356144, 0.0], [-71.063261, 42.356136, 0.0], [-71.064018, 42.355825, 0.0]])]

# POLYGON
poly_coords = [[[[-71.055757, 42.356856, 0.0], [-71.054976, 42.35608, 0.0], [-71.055636, 42.355697, 0.0], [-71.055941, 42.356003, 0.0], [-71.05622, 42.356767, 0.0], [-71.055757, 42.356856, 0.0]], [[-71.055522, 42.355955, 0.0], [-71.055458, 42.355894, 0.0], [-71.055546, 42.355846, 0.0], [-71.055615, 42.355908, 0.0], [-71.055522, 42.355955, 0.0]], [[-71.055312, 42.356089, 0.0], [-71.055226, 42.356005, 0.0], [-71.055288, 42.355969, 0.0], [-71.055373, 42.356058, 0.0], [-71.055312, 42.356089, 0.0]]], [[[-71.062157, 42.356514, 0.0], [-71.063337, 42.355222, 0.0], [-71.064638, 42.352457, 0.0], [-71.067238, 42.352639, 0.0], [-71.06915, 42.356132, 0.0], [-71.06326, 42.357591, 0.0], [-71.062157, 42.356514, 0.0]], [[-71.065045, 42.356047, 0.0], [-71.065107, 42.355953, 0.0], [-71.065249, 42.355911, 0.0], [-71.065909, 42.356018, 0.0], [-71.066016, 42.35601, 0.0], [-71.066198, 42.355918, 0.0], [-71.066417, 42.355854, 0.0], [-71.066521, 42.355876, 0.0], [-71.066564, 42.355938, 0.0], [-71.066547, 42.355985, 0.0], [-71.066, 42.356221, 0.0], [-71.065647, 42.356296, 0.0], [-71.065341, 42.35627, 0.0], [-71.065127, 42.356186, 0.0], [-71.065061, 42.356123, 0.0], [-71.065045, 42.356047, 0.0]]]]
poly_attrs = [['Park Name', 'Feature Description'], ['Post Office Square', 'Boundary of Post Office Square with holes for buildings'], ['Boston Common', 'Boundary of Boston Common with a hole for the Frog Pond']]

poly_features = [(['Post Office Square', 'Boundary of Post Office Square with holes for buildings'], [[[-71.055757, 42.356856, 0.0], [-71.054976, 42.35608, 0.0], [-71.055636, 42.355697, 0.0], [-71.055941, 42.356003, 0.0], [-71.05622, 42.356767, 0.0], [-71.055757, 42.356856, 0.0]], [[-71.055522, 42.355955, 0.0], [-71.055458, 42.355894, 0.0], [-71.055546, 42.355846, 0.0], [-71.055615, 42.355908, 0.0], [-71.055522, 42.355955, 0.0]], [[-71.055312, 42.356089, 0.0], [-71.055226, 42.356005, 0.0], [-71.055288, 42.355969, 0.0], [-71.055373, 42.356058, 0.0], [-71.055312, 42.356089, 0.0]]]), (['Boston Common', 'Boundary of Boston Common with a hole for the Frog Pond'], [[[-71.062157, 42.356514, 0.0], [-71.063337, 42.355222, 0.0], [-71.064638, 42.352457, 0.0], [-71.067238, 42.352639, 0.0], [-71.06915, 42.356132, 0.0], [-71.06326, 42.357591, 0.0], [-71.062157, 42.356514, 0.0]], [[-71.065045, 42.356047, 0.0], [-71.065107, 42.355953, 0.0], [-71.065249, 42.355911, 0.0], [-71.065909, 42.356018, 0.0], [-71.066016, 42.35601, 0.0], [-71.066198, 42.355918, 0.0], [-71.066417, 42.355854, 0.0], [-71.066521, 42.355876, 0.0], [-71.066564, 42.355938, 0.0], [-71.066547, 42.355985, 0.0], [-71.066, 42.356221, 0.0], [-71.065647, 42.356296, 0.0], [-71.065341, 42.35627, 0.0], [-71.065127, 42.356186, 0.0], [-71.065061, 42.356123, 0.0], [-71.065045, 42.356047, 0.0]]])]

# GCA
gca_pt_components = (pt_geom, pt_coords, pt_attrs)
gca_ls_components = (ls_geom, ls_coords, ls_attrs)
gca_poly_components = (poly_geom, poly_coords, poly_attrs)

# GCA AS EGF STRINGS
pt_as_egf = """PT



Park Name, City, Pond, Fountain



Post office Square, Boston, FALSE, TRUE
42.356243, -71.055631, 2.0



Boston Common, Boston, TRUE, TRUE
42.355465, -71.066412, 10.0
"""

ls_as_egf = """LS



Park Name, Feature Description



Post Office Square, A walk by the fountain
42.356716, -71.055685, 0.0
42.356587, -71.055769, 0.0
42.356566, -71.055754, 0.0
42.356539, -71.055746, 0.0
42.356511, -71.055757, 0.0
42.356495, -71.05579, 0.0
42.356485, -71.05583, 0.0
42.356389, -71.055842, 0.0
42.356252, -71.055796, 0.0
42.356046, -71.055642, 0.0
42.355876, -71.055697, 0.0
42.355828, -71.055758, 0.0



Boston Common, A walk by the fountain
42.356251, -71.062737, 0.0
42.35621, -71.063012, 0.0
42.356153, -71.06305, 0.0
42.356144, -71.063115, 0.0
42.356136, -71.063261, 0.0
42.355825, -71.064018, 0.0
"""

poly_as_egf = """POLY



Park Name, Feature Description



Post Office Square, Boundary of Post Office Square with holes for buildings
42.356856, -71.055757, 0.0
42.35608, -71.054976, 0.0
42.355697, -71.055636, 0.0
42.356003, -71.055941, 0.0
42.356767, -71.05622, 0.0

42.355955, -71.055522, 0.0
42.355894, -71.055458, 0.0
42.355846, -71.055546, 0.0
42.355908, -71.055615, 0.0

42.356089, -71.055312, 0.0
42.356005, -71.055226, 0.0
42.355969, -71.055288, 0.0
42.356058, -71.055373, 0.0



Boston Common, Boundary of Boston Common with a hole for the Frog Pond
42.356514, -71.062157, 0.0
42.355222, -71.063337, 0.0
42.352457, -71.064638, 0.0
42.352639, -71.067238, 0.0
42.356132, -71.06915, 0.0
42.357591, -71.06326, 0.0

42.356047, -71.065045, 0.0
42.355953, -71.065107, 0.0
42.355911, -71.065249, 0.0
42.356018, -71.065909, 0.0
42.35601, -71.066016, 0.0
42.355918, -71.066198, 0.0
42.355854, -71.066417, 0.0
42.355876, -71.066521, 0.0
42.355938, -71.066564, 0.0
42.355985, -71.066547, 0.0
42.356221, -71.066, 0.0
42.356296, -71.065647, 0.0
42.35627, -71.065341, 0.0
42.356186, -71.065127, 0.0
42.356123, -71.065061, 0.0
"""


# GCA AS JSON STRINGS
pt_as_json = """{"type": "FeatureCollection", "features": [{"type": "Feature", "geometry": {"type": "Point", "coordinates": [-71.055631, 42.356243, 2.0]}, "properties": {"Park Name": "Post office Square", "City": "Boston", "Pond": "FALSE", "Fountain": "TRUE"}}, {"type": "Feature", "geometry": {"type": "Point", "coordinates": [-71.066412, 42.355465, 10.0]}, "properties": {"Park Name": "Boston Common", "City": "Boston", "Pond": "TRUE", "Fountain": "TRUE"}}]}"""

ls_as_json = """{"type": "FeatureCollection", "features": [{"type": "Feature", "geometry": {"type": "LineString", "coordinates": [[-71.055685, 42.356716, 0.0], [-71.055769, 42.356587, 0.0], [-71.055754, 42.356566, 0.0], [-71.055746, 42.356539, 0.0], [-71.055757, 42.356511, 0.0], [-71.05579, 42.356495, 0.0], [-71.05583, 42.356485, 0.0], [-71.055842, 42.356389, 0.0], [-71.055796, 42.356252, 0.0], [-71.055642, 42.356046, 0.0], [-71.055697, 42.355876, 0.0], [-71.055758, 42.355828, 0.0]]}, "properties": {"Park Name": "Post Office Square", "Feature Description": "A walk by the fountain"}}, {"type": "Feature", "geometry": {"type": "LineString", "coordinates": [[-71.062737, 42.356251, 0.0], [-71.063012, 42.35621, 0.0], [-71.06305, 42.356153, 0.0], [-71.063115, 42.356144, 0.0], [-71.063261, 42.356136, 0.0], [-71.064018, 42.355825, 0.0]]}, "properties": {"Park Name": "Boston Common", "Feature Description": "A walk by the fountain"}}]}"""

poly_as_json = """{"type": "FeatureCollection", "features": [{"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[-71.055757, 42.356856, 0.0], [-71.054976, 42.35608, 0.0], [-71.055636, 42.355697, 0.0], [-71.055941, 42.356003, 0.0], [-71.05622, 42.356767, 0.0], [-71.055757, 42.356856, 0.0]], [[-71.055522, 42.355955, 0.0], [-71.055458, 42.355894, 0.0], [-71.055546, 42.355846, 0.0], [-71.055615, 42.355908, 0.0], [-71.055522, 42.355955, 0.0]], [[-71.055312, 42.356089, 0.0], [-71.055226, 42.356005, 0.0], [-71.055288, 42.355969, 0.0], [-71.055373, 42.356058, 0.0], [-71.055312, 42.356089, 0.0]]]}, "properties": {"Park Name": "Post Office Square", "Feature Description": "Boundary of Post Office Square with holes for buildings"}}, {"type": "Feature", "geometry": {"type": "Polygon", "coordinates": [[[-71.062157, 42.356514, 0.0], [-71.063337, 42.355222, 0.0], [-71.064638, 42.352457, 0.0], [-71.067238, 42.352639, 0.0], [-71.06915, 42.356132, 0.0], [-71.06326, 42.357591, 0.0], [-71.062157, 42.356514, 0.0]], [[-71.065045, 42.356047, 0.0], [-71.065107, 42.355953, 0.0], [-71.065249, 42.355911, 0.0], [-71.065909, 42.356018, 0.0], [-71.066016, 42.35601, 0.0], [-71.066198, 42.355918, 0.0], [-71.066417, 42.355854, 0.0], [-71.066521, 42.355876, 0.0], [-71.066564, 42.355938, 0.0], [-71.066547, 42.355985, 0.0], [-71.066, 42.356221, 0.0], [-71.065647, 42.356296, 0.0], [-71.065341, 42.35627, 0.0], [-71.065127, 42.356186, 0.0], [-71.065061, 42.356123, 0.0], [-71.065045, 42.356047, 0.0]]]}, "properties": {"Park Name": "Boston Common", "Feature Description": "Boundary of Boston Common with a hole for the Frog Pond"}}]}"""

# GCA AS CSV
pt_as_csv = [['Park Name', 'City', 'Pond', 'Fountain', 'GEOMETRY_PT'], ['Post office Square', 'Boston', 'FALSE', 'TRUE', [-71.055631, 42.356243, 2.0]], ['Boston Common', 'Boston', 'TRUE', 'TRUE', [-71.066412, 42.355465, 10.0]]]
pt_as_csv_xyz_and_geometry_true = [['Park Name', 'City', 'Pond', 'Fountain', 'LAT', 'LNG', 'ELEV', 'GEOMETRY_PT'], ['Post office Square', 'Boston', 'FALSE', 'TRUE', 42.356243, -71.055631, 2.0, [-71.055631, 42.356243, 2.0]], ['Boston Common', 'Boston', 'TRUE', 'TRUE', 42.355465, -71.066412, 10.0, [-71.066412, 42.355465, 10.0]]]
pt_as_csv_xyz_and_geometry_false = [['Park Name', 'City', 'Pond', 'Fountain'], ['Post office Square', 'Boston', 'FALSE', 'TRUE'], ['Boston Common', 'Boston', 'TRUE', 'TRUE']]

ls_as_csv = [['Park Name', 'Feature Description', 'GEOMETRY_LS'], ['Post Office Square', 'A walk by the fountain', [[-71.055685, 42.356716, 0.0], [-71.055769, 42.356587, 0.0], [-71.055754, 42.356566, 0.0], [-71.055746, 42.356539, 0.0], [-71.055757, 42.356511, 0.0], [-71.05579, 42.356495, 0.0], [-71.05583, 42.356485, 0.0], [-71.055842, 42.356389, 0.0], [-71.055796, 42.356252, 0.0], [-71.055642, 42.356046, 0.0], [-71.055697, 42.355876, 0.0], [-71.055758, 42.355828, 0.0]]], ['Boston Common', 'A walk by the fountain', [[-71.062737, 42.356251, 0.0], [-71.063012, 42.35621, 0.0], [-71.06305, 42.356153, 0.0], [-71.063115, 42.356144, 0.0], [-71.063261, 42.356136, 0.0], [-71.064018, 42.355825, 0.0]]]]

poly_as_csv = [['Park Name', 'Feature Description', 'GEOMETRY_POLY'], ['Post Office Square', 'Boundary of Post Office Square with holes for buildings', [[[-71.055757, 42.356856, 0.0], [-71.054976, 42.35608, 0.0], [-71.055636, 42.355697, 0.0], [-71.055941, 42.356003, 0.0], [-71.05622, 42.356767, 0.0], [-71.055757, 42.356856, 0.0]], [[-71.055522, 42.355955, 0.0], [-71.055458, 42.355894, 0.0], [-71.055546, 42.355846, 0.0], [-71.055615, 42.355908, 0.0], [-71.055522, 42.355955, 0.0]], [[-71.055312, 42.356089, 0.0], [-71.055226, 42.356005, 0.0], [-71.055288, 42.355969, 0.0], [-71.055373, 42.356058, 0.0], [-71.055312, 42.356089, 0.0]]]], ['Boston Common', 'Boundary of Boston Common with a hole for the Frog Pond', [[[-71.062157, 42.356514, 0.0], [-71.063337, 42.355222, 0.0], [-71.064638, 42.352457, 0.0], [-71.067238, 42.352639, 0.0], [-71.06915, 42.356132, 0.0], [-71.06326, 42.357591, 0.0], [-71.062157, 42.356514, 0.0]], [[-71.065045, 42.356047, 0.0], [-71.065107, 42.355953, 0.0], [-71.065249, 42.355911, 0.0], [-71.065909, 42.356018, 0.0], [-71.066016, 42.35601, 0.0], [-71.066198, 42.355918, 0.0], [-71.066417, 42.355854, 0.0], [-71.066521, 42.355876, 0.0], [-71.066564, 42.355938, 0.0], [-71.066547, 42.355985, 0.0], [-71.066, 42.356221, 0.0], [-71.065647, 42.356296, 0.0], [-71.065341, 42.35627, 0.0], [-71.065127, 42.356186, 0.0], [-71.065061, 42.356123, 0.0], [-71.065045, 42.356047, 0.0]]]]]
