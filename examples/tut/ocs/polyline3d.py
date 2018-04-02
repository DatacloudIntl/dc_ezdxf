# Copyright (c) 2018 Manfred Moitzi
# License: MIT License
# include-start
import math
import ezdxf
from ezdxf.algebra import UCS, Matrix44

dwg = ezdxf.new('R2010')
msp = dwg.modelspace()

# center point of the pentagon should be (0, 2, 2), and the shape is
# rotated around x-axis about 45 degree, to accomplish this I use an
# UCS with z-axis (0, 1, 1) and an x-axis parallel to WCS x-axis.

ucs = UCS(
    origin=(0, 2, 2),  # center of pentagon
    ux=(1, 0, 0),  # x-axis parallel to WCS x-axis
    uz=(0, 1, 1),  # z-axis
)
# calculating corner points in local (UCS) coordinates without Vector class
angle = math.radians(360/5)
corners_ucs = [(math.cos(angle*n), math.sin(angle*n), 0) for n in range(5)]

# let's do some transformations
tmatrix = Matrix44.chain(  # creating a transformation matrix
    Matrix44.z_rotate(math.radians(15)),   # 1. rotation around z-axis
    Matrix44.translate(0, .333, .333),  # 2. translation
)
transformed_corners_ucs = tmatrix.transform_vectors(corners_ucs)
corners_wcs = list(ucs.points_to_wcs(transformed_corners_ucs))
msp.add_polyline3d(
    points=corners_wcs,
    dxfattribs={
        'closed': True,
        'color': 2,
    })
center_wcs = ucs.ucs_to_wcs((0, .333, .333))
for corner in corners_wcs:
    msp.add_line(center_wcs, corner, dxfattribs={'color': 2})
# include-end

ucs.render_axis(msp)
dwg.saveas('ucs_polyline3d.dxf')