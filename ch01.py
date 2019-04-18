from shapely.geometry import Point, LineString, Polygon

point1 = Point(2.2, 4.2)
point2 = Point(7.2, -25.1)
point3 = Point(9.26, -2.456)
point3D = Point(9.26, -2.456, 0.57)
point_type = type(point1)

print(point1)
print(point3D)
print(type(point1))

point_coords = point1.coords

type(point_coords)

xy = point_coords.xy
x = point1.x
y = point1.y
print(xy)
print(x)
print(y)

point_dist = point1.distance(point2)
print("Distance between the points is {0:.2f} decimal degrees".format(point_dist))

line = LineString([point1, point2, point3])
line2 = LineString([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])
print(line)
print(line2)

type(line)

lxy = line.xy
print(lxy)

line_x = lxy[0]
line_y = line.xy[1]
print(line_x)
print(line_y)

l_length = line.length
l_centroid = line.centroid
centroid_type = type(l_centroid)
print("Length of our line: {0: 2f}".format(l_length))
print("Centroid of our line:", l_centroid)
print("Type of the centroid:", centroid_type)

poly = Polygon([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])
poly2 = Polygon([[p.x, p.y] for p in [point1, point2, point3]])
poly_type = poly.geom_type
poly_type2 = type(poly)
print(poly)
print(poly2)
print("Geometry type as text:", poly_type)
print("Geometry how Python shows it:", poly_type2)

# Help on Polygon in module shapely.geometry.polygon object:


world_exterior = [(-180, 90), (-180, -90), (180, -90), (180, 90)]
hole = [[(-170, 80), (-170, -80), (170, -80), (170, 80)]]  # double parentheses
world = Polygon(shell=world_exterior)
world_has_a_hole = Polygon(shell=world_exterior, holes=hole)
print(world)
print(world_has_a_hole)
type(world_has_a_hole)
# The first one represents the outerior and the second one represents the hole inside of the Polygon.

# Polygon attributes and functions
world_centroid = world.centroid
world_area = world.area
world_bbox = world.bounds
world_ext = world.exterior
world_ext_length = world_ext.length
print("Poly centroid: ", world_centroid)
print("Poly Exterior: ", world_ext)
print("Poly Exterior Length: ", world_ext_length)

# Geometry collections
from shapely.geometry import MultiPoint, MultiLineString, MultiPolygon, box
multi_point = MultiPoint([point1, point2, point3])
multi_point2 = MultiPoint([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])
line1 = LineString([point1, point2])
line2 = LineString([point2, point3])
multi_line = MultiLineString([line1, line2])
# MultiPolygon can be done in a similar manner
# Let's divide our world into western and eastern hemispheres with a hole on the western hemisphere
# --------------------------------------------------------------------------------------------------
# Let's create the exterior of the western part of the world
west_exterior = [(-180, 90), (-180, -90), (0,-90), (0, 90)]
west_hole = [[(-170,80), (-170, -80), (-10, -80), (-10, 80)]]
west_poly = Polygon(shell=west_exterior, holes=west_hole)
min_x, min_y = 0, -90
max_x, max_y = 180, 90
east_poly_box = box(minx=min_x, miny=min_y, maxx=max_x, maxy=max_y)
multi_poly = MultiPolygon([west_poly, east_poly_box])

print("MultiPoint:", multi_point)
print("Multiline: ", multi_line)
print("Bounding box: ", east_poly_box)
print("MultiPoly: ", multi_poly)


convex = multi_point.convex_hull
lines_count = len(multi_line)
multi_poly_area = multi_poly.area
west_area = multi_poly[0].area
valid = multi_poly.is_valid

print("Convex hull of the points: ", convex)
print("Number of lines in MultiLineString:", lines_count)
print("Area of our Multi=Polygon: ", multi_poly_area)
print("Area of our Western Hemisphere polygon: ", west_area)
print("Is polygon valid?: ", valid)

# From the above we can see that MultiPolygons have exactly the same attributes available as single geometric objects
# but now the information such as area calculates the area of ALL of the individual -objects combined. There are also
# some extra features available such as is_valid attribute that tells if the polygons or lines intersect with
# each other.


import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt
from descartes import PolygonPatch

fig = plt.figure(1, figsize=(10, 10), dpi=90)
ax = fig.add_subplot(111)
ring_patch = Polygon(world_has_a_hole)
# ax.add_patch(ring_patch)
ax.add_patch(world_has_a_hole)