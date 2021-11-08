from ..midicontroller import linear_interpolation, setup_controller


def set_triangles(attribute, value):
    for triangle in triangles:
        setattr(triangle, attribute, value)


def set_triangles_ponderated(attribute, value):
    for triangle in triangles:
        setattr(triangle, attribute, value * triangle.id)


def set_rows(x):
    global rows, triangles
    global delta_height, height

    introws = int(linear_interpolation(0, 127, 1, 13)(x))
    if introws % 2 == 0:
        introws += 1
    rows = introws
    delta_height = height / (rows + 1)
    for triangle in triangles:
        triangle.recalc_y()
    for triangle in triangles:
        triangle.recalc_y()


def set_cols(x):
    global cols, triangles
    global delta_width, width

    intcols = int(linear_interpolation(0, 127, 1, 29)(x))
    if intcols % 2 == 0:
        intcols += 1
    cols = intcols
    delta_width = width / (cols + 1)
    for triangle in triangles:
        triangle.recalc_x()
    for triangle in triangles:
        triangle.recalc_x()


def set_background_opacity(x):
    global background_opacity
    if x < 40:
        background_opacity = linear_interpolation(0, 39, 0.1, 2)(x)
    elif x < 70:
        background_opacity = linear_interpolation(40, 69, 2.01, 5)(x)
    else:
        background_opacity = linear_interpolation(70, 127, 5.01, 15)(x)


controller_schema = {
    16: lambda x: set_triangles("size", linear_interpolation(0, 127, 150, 800)(x)),
    16: lambda x: set_triangles("size", linear_interpolation(0, 127, 150, 800)(x)),
    18: lambda x: set_triangles(
        "inner_opacity", linear_interpolation(0, 127, 3, 100)(x)
    ),
    0: lambda x: set_triangles("x_spin_change", linear_interpolation(0, 127, 0, 1)(x)),
    1: lambda x: set_triangles("y_spin_change", linear_interpolation(0, 127, 0, 1)(x)),
    2: lambda x: set_triangles("z_spin_change", linear_interpolation(0, 127, 0, 1)(x)),
    3: lambda x: set_triangles_ponderated(
        "new_spin_offset", linear_interpolation(0, 127, 0, 1)(x)
    ),
    4: lambda x: set_triangles_ponderated(
        "new_hue_offset", linear_interpolation(0, 127, 0, 4.5)(x)
    ),
}

setup_controller(controller_schema)
