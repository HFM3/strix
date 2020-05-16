point_xml_str = """<Placemark><name>Home Plate</name><visibility>1</visibility><styleUrl>Bases Style</styleUrl><description>&lt;b&gt;City&lt;/b&gt;: Boston&lt;br&gt;&lt;b&gt;Park&lt;/b&gt;: Fenway&lt;br&gt;&lt;b&gt;Base&lt;/b&gt;: Home&lt;br&gt;</description><Point><altitudeMode>clampToGround</altitudeMode><coordinates>-71.097769,42.346249,0</coordinates></Point><ExtendedData><Data name="City"><displayName>City</displayName><value>Boston</value></Data><Data name="Park"><displayName>Park</displayName><value>Fenway</value></Data><Data name="Base"><displayName>Base</displayName><value>Home</value></Data></ExtendedData></Placemark>"""

line_xml_str = """<Placemark><name>Warning Track</name><visibility>1</visibility><styleUrl>#Warning Track Style</styleUrl><description>&lt;b&gt;City&lt;/b&gt;: Boston&lt;br&gt;&lt;b&gt;Park&lt;/b&gt;: Fenway&lt;br&gt;&lt;b&gt;Line&lt;/b&gt;: Warning track&lt;br&gt;</description><LineString><altitudeMode>clampToGround</altitudeMode><tessellate>1</tessellate><extrude>0</extrude><coordinates>-71.097727,42.346729,0 -71.097721,42.34703,0 -71.097023,42.34703,0 -71.096694,42.346892,0 -71.096457,42.346414,0 -71.096499,42.346359,0 -71.096695,42.346306,0 -71.096971,42.346287,0 </coordinates></LineString><ExtendedData><Data name="City"><displayName>City</displayName><value>Boston</value></Data><Data name="Park"><displayName>Park</displayName><value>Fenway</value></Data><Data name="Line"><displayName>Line</displayName><value>Warning track</value></Data></ExtendedData></Placemark>"""

polygon_xml_str = """<Placemark><name>Bases Area</name><visibility>1</visibility><styleUrl>#Bases Area Style</styleUrl><description>&lt;b&gt;City&lt;/b&gt;: Boston&lt;br&gt;&lt;b&gt;Park&lt;/b&gt;: Fenway&lt;br&gt;&lt;b&gt;Area&lt;/b&gt;: Inside of bases&lt;br&gt;</description><Polygon><altitudeMode>clampToGround</altitudeMode><tessellate>1</tessellate><extrude>0</extrude><outerBoundaryIs><LinearRing><coordinates>-71.097769,42.346249,0 -71.09744,42.346251,0 -71.097441,42.346496,0 -71.097772,42.346491,0 -71.097769,42.346249,0 </coordinates></LinearRing></outerBoundaryIs><innerBoundaryIs><LinearRing><coordinates>-71.097656,42.346331,0 -71.09758,42.346331,0 -71.09758,42.346387,0 -71.097656,42.346387,0 -71.097656,42.346331,0 </coordinates></LinearRing></innerBoundaryIs></Polygon><ExtendedData><Data name="City"><displayName>City</displayName><value>Boston</value></Data><Data name="Park"><displayName>Park</displayName><value>Fenway</value></Data><Data name="Area"><displayName>Area</displayName><value>Inside of bases</value></Data></ExtendedData></Placemark>"""

point_style = """<Style id="Bases Style"><IconStyle><color>ff00ffff</color><scale>1.0</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png</href></Icon></IconStyle><LabelStyle><scale>1.0</scale><color>ffffffff</color></LabelStyle></Style>"""

line_style = """<Style id="Warning Track Style"><LineStyle><color>ff0000ff</color><width>3.0</width></LineStyle><PolyStyle><color>59ebc934</color></PolyStyle></Style>"""

polygon_style = """<Style id="Bases Area Style"><PolyStyle><color>66fcca03</color></PolyStyle><LineStyle><color>ff03dffc</color><width>1.0</width></LineStyle></Style>"""

folder = """<Folder><name>Point and Line</name><description>Description of Folder</description><open>0</open><visibility>0</visibility><Placemark><name>Home Plate</name><visibility>1</visibility><styleUrl>Bases Style</styleUrl><description>&lt;b&gt;City&lt;/b&gt;: Boston&lt;br&gt;&lt;b&gt;Park&lt;/b&gt;: Fenway&lt;br&gt;&lt;b&gt;Base&lt;/b&gt;: Home&lt;br&gt;</description><Point><altitudeMode>clampToGround</altitudeMode><coordinates>-71.097769,42.346249,0</coordinates></Point><ExtendedData><Data name="City"><displayName>City</displayName><value>Boston</value></Data><Data name="Park"><displayName>Park</displayName><value>Fenway</value></Data><Data name="Base"><displayName>Base</displayName><value>Home</value></Data></ExtendedData></Placemark><Placemark><name>Warning Track</name><visibility>1</visibility><styleUrl>#Warning Track Style</styleUrl><description>&lt;b&gt;City&lt;/b&gt;: Boston&lt;br&gt;&lt;b&gt;Park&lt;/b&gt;: Fenway&lt;br&gt;&lt;b&gt;Line&lt;/b&gt;: Warning track&lt;br&gt;</description><LineString><altitudeMode>clampToGround</altitudeMode><tessellate>1</tessellate><extrude>0</extrude><coordinates>-71.097727,42.346729,0 -71.097721,42.34703,0 -71.097023,42.34703,0 -71.096694,42.346892,0 -71.096457,42.346414,0 -71.096499,42.346359,0 -71.096695,42.346306,0 -71.096971,42.346287,0 </coordinates></LineString><ExtendedData><Data name="City"><displayName>City</displayName><value>Boston</value></Data><Data name="Park"><displayName>Park</displayName><value>Fenway</value></Data><Data name="Line"><displayName>Line</displayName><value>Warning track</value></Data></ExtendedData></Placemark></Folder>"""

kml  = """<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2"><Document><name>Fenway Park</name><description>A KML File of Fenway Park</description><open>0</open><Style id="Bases Style"><IconStyle><color>ff00ffff</color><scale>1.0</scale><Icon><href>http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png</href></Icon></IconStyle><LabelStyle><scale>1.0</scale><color>ffffffff</color></LabelStyle></Style><Style id="Warning Track Style"><LineStyle><color>ff0000ff</color><width>3.0</width></LineStyle><PolyStyle><color>59ebc934</color></PolyStyle></Style><Style id="Bases Area Style"><PolyStyle><color>66fcca03</color></PolyStyle><LineStyle><color>ff03dffc</color><width>1.0</width></LineStyle></Style><Folder><name>Fenway Park</name><description>Demo of KML features</description><open>0</open><visibility>0</visibility><Placemark><name>Home Plate</name><visibility>1</visibility><styleUrl>Bases Style</styleUrl><description>&lt;b&gt;City&lt;/b&gt;: Boston&lt;br&gt;&lt;b&gt;Park&lt;/b&gt;: Fenway&lt;br&gt;&lt;b&gt;Base&lt;/b&gt;: Home&lt;br&gt;</description><Point><altitudeMode>clampToGround</altitudeMode><coordinates>-71.097769,42.346249,0</coordinates></Point><ExtendedData><Data name="City"><displayName>City</displayName><value>Boston</value></Data><Data name="Park"><displayName>Park</displayName><value>Fenway</value></Data><Data name="Base"><displayName>Base</displayName><value>Home</value></Data></ExtendedData></Placemark><Placemark><name>Warning Track</name><visibility>1</visibility><styleUrl>#Warning Track Style</styleUrl><description>&lt;b&gt;City&lt;/b&gt;: Boston&lt;br&gt;&lt;b&gt;Park&lt;/b&gt;: Fenway&lt;br&gt;&lt;b&gt;Line&lt;/b&gt;: Warning track&lt;br&gt;</description><LineString><altitudeMode>clampToGround</altitudeMode><tessellate>1</tessellate><extrude>0</extrude><coordinates>-71.097727,42.346729,0 -71.097721,42.34703,0 -71.097023,42.34703,0 -71.096694,42.346892,0 -71.096457,42.346414,0 -71.096499,42.346359,0 -71.096695,42.346306,0 -71.096971,42.346287,0 </coordinates></LineString><ExtendedData><Data name="City"><displayName>City</displayName><value>Boston</value></Data><Data name="Park"><displayName>Park</displayName><value>Fenway</value></Data><Data name="Line"><displayName>Line</displayName><value>Warning track</value></Data></ExtendedData></Placemark><Placemark><name>Bases Area</name><visibility>1</visibility><styleUrl>#Bases Area Style</styleUrl><description>&lt;b&gt;City&lt;/b&gt;: Boston&lt;br&gt;&lt;b&gt;Park&lt;/b&gt;: Fenway&lt;br&gt;&lt;b&gt;Area&lt;/b&gt;: Inside of bases&lt;br&gt;</description><Polygon><altitudeMode>clampToGround</altitudeMode><tessellate>1</tessellate><extrude>0</extrude><outerBoundaryIs><LinearRing><coordinates>-71.097769,42.346249,0 -71.09744,42.346251,0 -71.097441,42.346496,0 -71.097772,42.346491,0 -71.097769,42.346249,0 </coordinates></LinearRing></outerBoundaryIs><innerBoundaryIs><LinearRing><coordinates>-71.097656,42.346331,0 -71.09758,42.346331,0 -71.09758,42.346387,0 -71.097656,42.346387,0 -71.097656,42.346331,0 </coordinates></LinearRing></innerBoundaryIs></Polygon><ExtendedData><Data name="City"><displayName>City</displayName><value>Boston</value></Data><Data name="Park"><displayName>Park</displayName><value>Fenway</value></Data><Data name="Area"><displayName>Area</displayName><value>Inside of bases</value></Data></ExtendedData></Placemark></Folder></Document></kml>"""
