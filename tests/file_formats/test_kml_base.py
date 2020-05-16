import unittest
import xml.etree.ElementTree as ET
from strix.file_formats import kml_base as kmlb
from tests.file_formats.variables import kml_base_vars


def xml_to_str(xml_obj):
    return ET.tostring(xml_obj, encoding='unicode', method='xml')


class TestKMLBase(unittest.TestCase):

    def test_altitude_modes(self):
        self.assertEqual(kmlb.altitude_modes('abs'), 'absolute')
        self.assertEqual(kmlb.altitude_modes('ctg'), 'clampToGround')
        self.assertEqual(kmlb.altitude_modes('rtg'), 'relativeToGround')
        self.assertEqual(kmlb.altitude_modes('RANDOM'), 'clampToGround')

    def test_kml_color(self):
        self.assertEqual(kmlb.kml_color('#4287f5'), 'fff58742')
        self.assertEqual(kmlb.kml_color('#4287f5', 100), 'fff58742')
        self.assertEqual(kmlb.kml_color('#4287f5', 50), '80f58742')
        self.assertEqual(kmlb.kml_color('#4287f5', 0), '00f58742')

        self.assertRaises(ValueError, kmlb.kml_color, '#4287f5', -10)
        self.assertRaises(ValueError, kmlb.kml_color, '#4287f5', 101)

    def test_point(self):
        x = kmlb.point([-71.097769, 42.346249, 0], 'Home Plate', ['City', 'Park', 'Base'], ['Boston', 'Fenway', 'Home'], altitude_mode='ctg', style_to_use='Bases Style')
        self.assertEqual(xml_to_str(x), kml_base_vars.point_xml_str)

    def test_line(self):
        warning_track_boundary_coords = [[-71.097727, 42.346729, 0],
                                         [-71.097721, 42.347030, 0],
                                         [-71.097023, 42.347030, 0],
                                         [-71.096694, 42.346892, 0],
                                         [-71.096457, 42.346414, 0],
                                         [-71.096499, 42.346359, 0],
                                         [-71.096695, 42.346306, 0],
                                         [-71.096971, 42.346287, 0]]

        x = kmlb.line(warning_track_boundary_coords, 'Warning Track', ['City', 'Park', 'Line'], ['Boston', 'Fenway', 'Warning track'], style_to_use='Warning Track Style')
        self.assertEqual(xml_to_str(x), kml_base_vars.line_xml_str)

    def test_polygon(self):
        bases = [[-71.097769, 42.346249, 0],
                 [-71.097440, 42.346251, 0],
                 [-71.097441, 42.346496, 0],
                 [-71.097772, 42.346491, 0],
                 [-71.097769, 42.346249, 0]]

        # Hole for pitcher's mound
        mound = [[-71.097656, 42.346331, 0],
                 [-71.097580, 42.346331, 0],
                 [-71.097580, 42.346387, 0],
                 [-71.097656, 42.346387, 0],
                 [-71.097656, 42.346331, 0]]

        coords = [bases, mound]

        x = kmlb.polygon(coords, 'Bases Area', ['City', 'Park', 'Area'], ['Boston', 'Fenway', 'Inside of bases'], style_to_use='Bases Area Style')

        self.assertEqual(xml_to_str(x), kml_base_vars.polygon_xml_str)

    def test_point_style(self):
        x = kmlb.point_style('Bases Style', icon="http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png", color=('#ffff00', 100), scale=1.0, label_color=('#ffffff', 100), label_size=1.0)
        self.assertEqual(xml_to_str(x), kml_base_vars.point_style)

    def test_line_style(self):
        x = kmlb.line_style('Warning Track Style', color=('#ff0000', 100), width=3.0, extrude_color=('#34c9eb', 35))
        self.assertEqual(xml_to_str(x), kml_base_vars.line_style)

    def test_polygon_style(self):
        x = kmlb.polygon_style('Bases Area Style', color=('#03cafc', 40), outline_width=1.0, outline_color=('#fcdf03', 100))
        self.assertEqual(xml_to_str(x), kml_base_vars.polygon_style)

    def test_folder(self):
        pt = kmlb.point([-71.097769, 42.346249, 0], 'Home Plate', ['City', 'Park', 'Base'], ['Boston', 'Fenway', 'Home'], style_to_use='Bases Style')

        warning_track_boundary_coords = [[-71.097727, 42.346729, 0],
                                         [-71.097721, 42.347030, 0],
                                         [-71.097023, 42.347030, 0],
                                         [-71.096694, 42.346892, 0],
                                         [-71.096457, 42.346414, 0],
                                         [-71.096499, 42.346359, 0],
                                         [-71.096695, 42.346306, 0],
                                         [-71.096971, 42.346287, 0]]

        ls = kmlb.line(warning_track_boundary_coords, 'Warning Track', ['City', 'Park', 'Line'], ['Boston', 'Fenway', 'Warning track'], style_to_use='Warning Track Style')

        features = [pt, ls]

        folder = kmlb.folder('Point and Line', features, 'Description of Folder')

        self.assertEqual(xml_to_str(folder), kml_base_vars.folder)

    def test_kml(self):
        # POINT
        pt = kmlb.point([-71.097769, 42.346249, 0], 'Home Plate', ['City', 'Park', 'Base'],
                        ['Boston', 'Fenway', 'Home'], style_to_use='Bases Style')

        # LINE
        line_coords = [[-71.097727, 42.346729, 0],
                         [-71.097721, 42.347030, 0],
                         [-71.097023, 42.347030, 0],
                         [-71.096694, 42.346892, 0],
                         [-71.096457, 42.346414, 0],
                         [-71.096499, 42.346359, 0],
                         [-71.096695, 42.346306, 0],
                         [-71.096971, 42.346287, 0]]

        ls = kmlb.line(line_coords, 'Warning Track', ['City', 'Park', 'Line'],
                       ['Boston', 'Fenway', 'Warning track'], style_to_use='Warning Track Style')

        # POLYGON
        bases = [[-71.097769, 42.346249, 0],
                 [-71.097440, 42.346251, 0],
                 [-71.097441, 42.346496, 0],
                 [-71.097772, 42.346491, 0],
                 [-71.097769, 42.346249, 0]]

        # Hole for pitcher's mound
        mound = [[-71.097656, 42.346331, 0],
                 [-71.097580, 42.346331, 0],
                 [-71.097580, 42.346387, 0],
                 [-71.097656, 42.346387, 0],
                 [-71.097656, 42.346331, 0]]

        poly_coords = [bases, mound]

        poly = kmlb.polygon(poly_coords, 'Bases Area', ['City', 'Park', 'Area'], ['Boston', 'Fenway', 'Inside of bases'],
                         style_to_use='Bases Area Style')

        features = [pt, ls, poly]

        folder = kmlb.folder('Fenway Park', features, 'Demo of KML features')

        point_style = kmlb.point_style('Bases Style', icon="http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png", color=('#ffff00', 100), scale=1.0, label_color=('#ffffff', 100), label_size=1.0)
        line_style = kmlb.line_style('Warning Track Style', color=('#ff0000', 100), width=3.0, extrude_color=('#34c9eb', 35))
        poly_style = kmlb.polygon_style('Bases Area Style', color=('#03cafc', 40), outline_width=1.0, outline_color=('#fcdf03', 100))

        styles = [point_style, line_style, poly_style]
        kml_features = [folder]

        kml = kmlb.kml('Fenway Park', styles, kml_features, 'A KML File of Fenway Park')

        self.assertEqual(kml, kml_base_vars.kml)


if __name__ == '__main__':
    unittest.main()