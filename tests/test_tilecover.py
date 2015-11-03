import pytest
from shapely import geometry

from tiletanic.tilecover import cover_geometry
from tiletanic.tileschemes import DGTiling

@pytest.fixture
def tiler():
    return DGTiling()


@pytest.fixture
def pt():
    return geometry.Point(-94.39453125, 15.908203125)


@pytest.fixture
def mpt():
    return geometry.MultiPoint([(-94.39453125, 15.908203125),
                                (-94.306640625, 15.908203125),
                                (-94.306640625, 15.8203125),
                                (-94.39453125, 15.8203125)])


@pytest.fixture
def ls():
    return geometry.shape({"coordinates": [[-123.12515258789061, 45.70809729528788], [-122.4755859375, 45.615958580368364], [-123.32977294921874, 45.44664375276733], [-122.25173950195311, 45.334771196762766], [-123.3819580078125, 45.11133093583217], [-122.23388671874999, 45.04829981381567], [-122.57995605468749, 45.74740199642105], [-122.6348876953125, 44.961882876810925], [-122.80654907226562, 45.75315158411652], [-122.98645019531249, 44.998795943614084], [-123.05648803710938, 45.744526980468436], [-123.33938598632812, 45.031803280058554]], "type": "LineString"})


@pytest.fixture
def mls():
    return geometry.shape({'type': 'MultiLineString', 'coordinates': (((-0.9709167480468749, 35.18840002173177), (-0.9832763671875, 34.83296838321102), (-0.954437255859375, 35.02774729487063), (-0.850067138671875, 35.02662273458687), (-0.833587646484375, 34.838604318635014), (-0.8074951171874999, 35.185032937998294)), ((-0.0823974609375, 35.191766965947394), (-0.111236572265625, 34.83071390101431), (0.048065185546875, 34.829586636768205), (0.067291259765625, 35.192889249680945), (-0.06591796875, 35.191766965947394)), ((-0.28564453125, 35.19064466671118), (-0.34606933593749994, 34.84085858477277), (-0.18402099609375, 34.831841149828676)), ((-0.48614501953124994, 35.183910545750834), (-0.517730712890625, 34.854382885097905), (-0.391387939453125, 34.84874803007872)), ((-0.553436279296875, 35.183910545750834), (-0.7347106933593749, 35.185032937998294), (-0.751190185546875, 35.05922870088872), (-0.591888427734375, 35.0502352513963), (-0.758056640625, 35.03336986422378), (-0.767669677734375, 34.86227103378598), (-0.597381591796875, 34.85550980979319)))})

@pytest.fixture
def poly():
    return geometry.shape({'type': 'Polygon', 'coordinates': (((74.5751953125, 46.86019101567027), (73.916015625, 46.45299704748289), (73.564453125, 46.21785176740299), (73.32275390625, 45.920587344733654), (73.289794921875, 45.56021795715051), (73.465576171875, 45.27488643704894), (74.036865234375, 44.96479793033104), (74.256591796875, 45.07352060670971), (74.322509765625, 45.48324350868221), (74.46533203125, 45.91294412737392), (74.849853515625, 46.057985244793024), (74.99267578125, 46.354510837365254), (75.465087890625, 46.40756396630067), (76.102294921875, 46.42271253466719), (76.904296875, 46.34692761055676), (77.376708984375, 46.27863122156088), (78.2666015625, 46.195042108660154), (78.94775390625, 46.31658418182218), (79.29931640625, 46.5286346952717), (79.398193359375, 46.77749276376827), (79.12353515625, 47.017716353979225), (78.42041015625, 46.912750956378915), (77.574462890625, 46.76244305208004), (76.46484375, 46.81509864599243), (76.036376953125, 46.98025235521883), (75.399169921875, 46.830133640447386), (74.893798828125, 46.93526088057719), (74.5751953125, 46.86019101567027)),)})


@pytest.fixture
def poly_w_hole():
    return geometry.shape({'type': 'Polygon', 'coordinates': (((31.794433593749996, -28.979312036722447), (31.289062500000004, -29.401319510041485), (31.036376953125, -29.897805610155864), (30.377197265625, -30.845647420182598), (29.278564453125, -31.886886525780806), (26.74072265625, -31.94283997285307), (23.9501953125, -31.184609135743237), (23.917236328125, -28.98892237190413), (25.5322265625, -27.615406013399603), (27.894287109374996, -27.019984007982554), (30.377197265625, -27.32297494724568), (31.794433593749996, -28.979312036722447)), ((28.652343749999996, -28.584521719370393), (28.399658203125, -28.632746799225856), (28.3282470703125, -28.724313406473463), (28.1634521484375, -28.729130483430154), (28.015136718749996, -28.8831596093235), (27.745971679687496, -28.92163128242129), (27.531738281249996, -29.200123477644983), (27.410888671874996, -29.382175075145277), (27.257080078125, -29.54956657394792), (26.987915039062496, -29.640320395351402), (27.1966552734375, -30.002516938570686), (27.31201171875, -30.140376821599734), (27.3834228515625, -30.14987731644208), (27.366943359375, -30.249577240467637), (27.39990234375, -30.334953881988564), (27.454833984375, -30.33021268543272), (27.745971679687496, -30.60954979719083), (27.8997802734375, -30.619004797647793), (28.108520507812496, -30.680439786468128), (28.1744384765625, -30.50075098029068), (28.14697265625, -30.462879341709876), (28.229370117187496, -30.410781790845878), (28.2513427734375, -30.29701788337205), (28.3612060546875, -30.202113679097216), (28.71826171875, -30.135626231134587), (28.9544677734375, -30.026299582223675), (29.179687499999996, -29.912090918781477), (29.1192626953125, -29.831113764737136), (29.141235351562504, -29.67850809103362), (29.256591796874996, -29.640320395351402), (29.300537109374996, -29.492206334848714), (29.410400390625, -29.40610505570927), (29.443359375, -29.31993078977759), (29.393920898437496, -29.195328267099118), (29.2950439453125, -29.08977693862319), (29.091796875, -28.936054482136658), (28.976440429687496, -28.90239722855847), (28.916015625, -28.762843805266016), (28.800659179687496, -28.772474183943018), (28.789672851562496, -28.6905876542507), (28.7017822265625, -28.656851034203406), (28.652343749999996, -28.584521719370393)))})


@pytest.fixture
def mpoly():
    return geometry.shape({'type': 'MultiPolygon', 'coordinates': [(((-155.60651896977458, 20.13795556629634), (-155.16804273408488, 19.946827215003964), (-154.81406356568098, 19.50657921146143), (-155.67475562357313, 18.906117143691233), (-155.9039060717078, 19.069459067981597), (-156.0601639283226, 19.73122055328588), (-155.83545761767488, 19.975703442260055), (-155.88048255092895, 20.252020575289293), (-155.60651896977458, 20.13795556629634)),), (((-156.91373752666547, 20.73472409144364), (-156.96228010324413, 20.73238773010962), (-157.05521360182624, 20.911371030348732), (-156.81633843277243, 20.841704170311175), (-156.91373752666547, 20.73472409144364)),), (((-156.53412841109724, 20.531787476211036), (-156.6792613032665, 20.504712931856318), (-156.7005618241688, 20.525426565083876), (-156.5826214116488, 20.59995670154052), (-156.53412841109724, 20.531787476211036)),), (((-156.5895997046626, 21.027738813695294), (-156.24290930851774, 20.941555080502553), (-155.98469586911904, 20.717591061278426), (-156.40765319493894, 20.587206654063834), (-156.68490668409615, 20.881887778698), (-156.5895997046626, 21.027738813695294)),), (((-157.24884316468027, 21.22171060725873), (-156.96576900873274, 21.213324286186833), (-156.70572493545737, 21.15654296368683), (-157.2730606762092, 21.087347723418702), (-157.24884316468027, 21.22171060725873)),), (((-157.89376363688228, 21.598381702453594), (-157.72570752668096, 21.45898509818369), (-157.69321165049723, 21.262742044309903), (-157.9609268868663, 21.388820705311275), (-158.0988663403093, 21.29539622635474), (-158.27893301424717, 21.575264710198212), (-157.98264568694884, 21.7098504289541), (-157.89376363688228, 21.598381702453594)),), (((-161.9451798172947, 23.03986237235057), (-161.94477291633697, 23.04621002837007), (-161.94041907528006, 23.045599677383166), (-161.94090735588972, 23.041978257690403), (-161.9451798172947, 23.03986237235057)),), (((-164.7043350900923, 23.5793317732427), (-164.69908606656867, 23.570542710577627), (-164.70848548112002, 23.574530341402124), (-164.7043350900923, 23.5793317732427)),), (((-167.99616451697884, 25.004339911058025), (-168.00279700357882, 25.014797268279267), (-167.99986731722288, 25.01642487211012), (-167.99555416599193, 25.011664130095483), (-167.99616451697884, 25.004339911058025)),), (((-171.72280839828892, 25.773016669183903), (-171.72935950433762, 25.7519391954375), (-171.7390844392954, 25.756293036494412), (-171.74067135330029, 25.769029039258726), (-171.72280839828892, 25.773016669183903)),), (((-173.9591772130579, 26.059637762073066), (-173.96564693855532, 26.05857982030244), (-173.96499589774245, 26.07135651199343), (-173.96051998630827, 26.063137111388585), (-173.9591772130579, 26.059637762073066)),), (((-178.2983970579778, 28.387372162295435), (-178.3043661632678, 28.387912197090202), (-178.29038113887842, 28.401678575605786), (-178.28790478098082, 28.39298946089491), (-178.2983970579778, 28.387372162295435)),), (((-160.198240306345, 21.783883779013195), (-160.23442352432616, 21.874455639016503), (-160.05996362062456, 22.000562970404758), (-160.07221432223315, 21.910834052149767), (-160.198240306345, 21.783883779013195)),), (((-159.38818451870054, 22.228789014401457), (-159.29470434293106, 22.107627229413083), (-159.43731532294376, 21.868769246403588), (-159.78721108632254, 22.019270121718705), (-159.38818451870054, 22.228789014401457)),)]})

    
def test_cover_geometry_empty_geoms(tiler):
    """Empty geometries should return empty iterators."""
    assert not cover_geometry(tiler, geometry.Point(), 0) == True
    assert not cover_geometry(tiler, geometry.MultiPoint(), 0) == True
    assert not cover_geometry(tiler, geometry.LineString(), 0) == True
    assert not cover_geometry(tiler, geometry.MultiLineString(), 0) == True
    assert not cover_geometry(tiler, geometry.Polygon(), 0) == True
    assert not cover_geometry(tiler, geometry.MultiPolygon(), 0) == True
    assert not cover_geometry(tiler, geometry.GeometryCollection(), 0) == True


def test_cover_geometry_nonshapely_geom(tiler):
    """Only accept shapely geometries."""
    with pytest.raises(ValueError):
        for tile in cover_geometry(tiler, None, 0):
            pass

        
def test_cover_geometry_point1(tiler, pt):
    """A Point geometry."""
    tiles = [tile for tile in cover_geometry(tiler, pt, 4)]
    assert len(tiles) == 1
    assert set(tiles) == {(3, 4, 4)}


def test_cover_geometry_point2(tiler, pt):
    """A Point geometry."""
    tiles = [tile for tile in cover_geometry(tiler, pt, 12)]
    assert len(tiles) == 4
    assert set(tiles) == {(973, 1204, 12), (973, 1205, 12), (974, 1204, 12), (974, 1205, 12)}


def test_cover_geometry_multipoint1(tiler, mpt):
    """A MultiPoint geometry."""    
    tiles = [tile for tile in cover_geometry(tiler, mpt, 4)]
    assert len(tiles) == 1


def test_cover_geometry_multipoint2(tiler, mpt):
    """A MultiPoint geometry."""    
    tiles = [tile for tile in cover_geometry(tiler, mpt, 12)]
    assert len(tiles) == 9
    assert set(tiles) == {(973, 1203, 12), (974, 1203, 12), (975, 1203, 12),
                          (973, 1204, 12), (973, 1205, 12), (974, 1204, 12),
                          (975, 1204, 12), (974, 1205, 12), (975, 1205, 12)}
                          
                           
def test_cover_geometry_linestring1(tiler, ls):
    """A LineString geometry."""
    tiles = [tile for tile in cover_geometry(tiler, ls, 4)]
    assert len(tiles) == 2
    assert set(tiles) == {(2, 5, 4), (2, 6, 4)}


def test_cover_geometry_linestring2(tiler, ls):
    """A LineString geometry."""
    tiles = [tile for tile in cover_geometry(tiler, ls, 11)]
    assert len(tiles) == 30
    assert set(tiles) == {(322, 768, 11), (322, 769, 11), (322, 770, 11), (323, 768, 11),
                          (323, 769, 11), (323, 770, 11), (323, 771, 11), (323, 772, 11),
                          (324, 767, 11), (324, 768, 11), (324, 769, 11), (324, 770, 11),
                          (324, 771, 11), (325, 768, 11), (325, 769, 11), (325, 770, 11),
                          (325, 771, 11), (325, 772, 11), (326, 767, 11), (326, 768, 11),
                          (326, 769, 11), (326, 770, 11), (326, 771, 11), (326, 772, 11),
                          (327, 768, 11), (327, 769, 11), (327, 770, 11), (327, 771, 11),
                          (328, 768, 11), (328, 769, 11)}


def test_cover_geometry_multilinestring1(tiler, mls):
    """A MultiLineString geometry."""
    tiles = [tile for tile in cover_geometry(tiler, mls, 8)]
    assert len(tiles) == 4
    assert set(tiles) == {(127, 88, 8), (127, 89, 8), (128, 88, 8), (128, 89, 8)}


def test_cover_geometry_multilinestring2(tiler, mls):
    """A MultiLineString geometry."""
    tiles = [tile for tile in cover_geometry(tiler, mls, 12)]
    assert len(tiles) == 47
    assert set(tiles) == {(2036, 1420, 12), (2036, 1421, 12), (2036, 1422, 12), (2036, 1423, 12),
                          (2036, 1424, 12), (2037, 1421, 12), (2037, 1422, 12), (2038, 1420, 12),
                          (2038, 1421, 12), (2038, 1422, 12), (2038, 1423, 12), (2038, 1424, 12),
                          (2039, 1420, 12), (2039, 1421, 12), (2039, 1422, 12), (2039, 1423, 12),
                          (2039, 1424, 12), (2040, 1420, 12), (2040, 1422, 12), (2040, 1424, 12),
                          (2041, 1420, 12), (2041, 1422, 12), (2041, 1424, 12), (2042, 1420, 12),
                          (2042, 1421, 12), (2042, 1422, 12), (2042, 1423, 12), (2042, 1424, 12),
                          (2043, 1420, 12), (2044, 1420, 12), (2044, 1421, 12), (2044, 1422, 12),
                          (2044, 1423, 12), (2044, 1424, 12), (2045, 1420, 12), (2046, 1420, 12),
                          (2046, 1421, 12), (2046, 1422, 12), (2046, 1423, 12), (2047, 1420, 12),
                          (2047, 1423, 12), (2047, 1424, 12), (2048, 1420, 12), (2048, 1421, 12),
                          (2048, 1422, 12), (2048, 1423, 12), (2048, 1424, 12)}


    
def test_cover_geometry_poly1(tiler, poly):
    """A Polygon geometry."""
    tiles = [tile for tile in cover_geometry(tiler, poly, 7)]
    assert len(tiles) == 4
    assert set(tiles) == {(90, 47, 7), (90, 48, 7), (91, 48, 7), (92, 48, 7)}


def test_cover_geometry_poly2(tiler, poly):
    """A Polygon geometry."""
    tiles = [tile for tile in cover_geometry(tiler, poly, 7)]
    assert len(tiles) == 4
    assert set(tiles) == {( 90, 47, 7), (90, 48, 7), (91, 48, 7), (92, 48, 7)}


def test_cover_geometry_poly_w_hole1(tiler, poly_w_hole):
    """A Polygon geometry with a hole in it."""
    tiles = [tile for tile in cover_geometry(tiler, poly_w_hole, 7)]
    assert len(tiles) == 11
    assert set(tiles) == set([(72, 22, 7), (74, 21, 7), (75, 22, 7), (73, 20, 7), (74, 22, 7), (73, 22, 7), (74, 20, 7), (73, 21, 7), (75, 21, 7), (72, 21, 7), (72, 20, 7)])

    
def test_cover_geometry_poly_w_hole2(tiler, poly_w_hole):
    """A Polygon geometry with a hole in it."""
    tiles = [tile for tile in cover_geometry(tiler, poly_w_hole, 9)]
    assert len(tiles) == 77
    assert set(tiles) == set([(297, 82, 9), (301, 87, 9), (294, 87, 9), (299, 88, 9), (300, 85, 9), (292, 83, 9), (296, 83, 9), (298, 89, 9), (295, 82, 9), (290, 86, 9), (291, 87, 9), (297, 88, 9), (292, 87, 9), (298, 86, 9), (298, 84, 9), (294, 84, 9), (294, 88, 9), (299, 89, 9), (292, 85, 9), (300, 86, 9), (294, 82, 9), (290, 85, 9), (298, 82, 9), (295, 84, 9), (296, 87, 9), (293, 84, 9), (299, 85, 9), (291, 85, 9), (299, 86, 9), (296, 85, 9), (297, 85, 9), (296, 89, 9), (293, 89, 9), (292, 86, 9), (293, 87, 9), (291, 88, 9), (298, 88, 9), (298, 87, 9), (295, 87, 9), (296, 88, 9), (293, 83, 9), (301, 86, 9), (291, 86, 9), (297, 86, 9), (297, 89, 9), (292, 88, 9), (294, 86, 9), (294, 85, 9), (292, 82, 9), (300, 87, 9), (295, 89, 9), (290, 87, 9), (296, 82, 9), (298, 85, 9), (297, 83, 9), (291, 83, 9), (295, 83, 9), (300, 88, 9), (293, 86, 9), (299, 83, 9), (299, 84, 9), (297, 87, 9), (294, 83, 9), (297, 84, 9), (298, 83, 9), (293, 82, 9), (294, 89, 9), (296, 84, 9), (290, 84, 9), (293, 88, 9), (290, 83, 9), (295, 86, 9), (293, 85, 9), (295, 88, 9), (292, 84, 9), (291, 84, 9), (299, 87, 9)])
    

def test_cover_geometry_multipoly1(tiler, mpoly):
    """A MultiPolygon geometry."""
    tiles = [tile for tile in cover_geometry(tiler, mpoly, 7)]
    assert len(tiles) == 8
    assert set(tiles) == set([(8, 38, 7), (4, 40, 7), (2, 41, 7), (0, 42, 7), (5, 40, 7), (7, 39, 7), (8, 39, 7), (6, 40, 7)])


def test_cover_geometry_multipoly2(tiler, mpoly):
    """A MultiPolygon geometry."""
    tiles = [tile for tile in cover_geometry(tiler, mpoly, 10)]
    assert len(tiles) == 44
    assert set(tiles) == set([(23, 329, 10), (56, 318, 10), (70, 310, 10), (64, 315, 10), (67, 315, 10), (68, 310, 10), (63, 316, 10), (62, 316, 10), (71, 311, 10), (65, 314, 10), (68, 311, 10), (57, 318, 10), (70, 313, 10), (62, 317, 10), (4, 336, 10), (67, 314, 10), (64, 316, 10), (69, 310, 10), (66, 314, 10), (69, 313, 10), (68, 312, 10), (17, 330, 10), (63, 317, 10), (69, 312, 10), (58, 319, 10), (71, 312, 10), (68, 313, 10), (70, 311, 10), (69, 309, 10), (51, 321, 10), (70, 312, 10), (56, 317, 10), (61, 317, 10), (65, 315, 10), (65, 316, 10), (43, 323, 10), (68, 309, 10), (58, 318, 10), (34, 327, 10), (68, 314, 10), (66, 315, 10), (69, 311, 10), (68, 315, 10), (66, 316, 10)])
    