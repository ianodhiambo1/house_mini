# drawing_functions.py

import cairo
import math

# Helper function to set RGB colors using 0–255 values
def set_rgb_color(context, r, g, b):
    context.set_source_rgb(r / 255, g / 255, b / 255)

# Define a function to draw a slanted window
def draw_window(context, x_offset, y_offset, angle):
    # Apply 10-degree slant transformation
    angle = math.radians(angle)
    matrix = cairo.Matrix(1, math.tan(angle), 0, 1, x_offset, y_offset)
    context.transform(matrix)

    # Draw the outer green rectangle
    context.rectangle(300, 345, 60, 90)  # x=300, y=345, width=60, height=90
    set_rgb_color(context, 0, 160, 93)  # Green fill
    context.fill_preserve()
    context.set_source_rgb(0, 0, 0)  # Black stroke
    context.stroke()

    # Draw the inner blue rectangle
    context.rectangle(310, 355, 40, 70)  # x=310, y=355, width=40, height=70
    set_rgb_color(context, 165, 239, 255)  # Blue fill
    context.fill_preserve()
    context.set_source_rgb(0, 0, 0)  # Black stroke
    context.stroke()

    # Draw the green horizontal rectangle (line) in the middle of the blue rectangle
    context.rectangle(310, 385, 40, 5)  # x=310, y=385, width=40, height=5
    set_rgb_color(context, 0, 160, 93)  # Green fill
    context.fill_preserve()
    context.set_source_rgb(0, 0, 0)  # Black stroke
    context.stroke()

# Define a function to draw a slanted window side
def draw_window_side(context, x_offset, y_offset, angle):
    # Apply 10-degree slant transformation
    angle = math.radians(angle)
    matrix = cairo.Matrix(1, math.tan(angle), 0, 1, x_offset, y_offset)
    context.transform(matrix)

    # Draw the outer green rectangle
    context.rectangle(300, 345, 60, 90)  # x=300, y=345, width=60, height=90
    set_rgb_color(context, 0, 160, 93)  # Green fill
    context.fill_preserve()
    context.set_source_rgb(0, 0, 0)  # Black stroke
    context.stroke()

    # Draw the inner blue rectangle
    context.rectangle(310, 355, 40, 70)  # x=310, y=355, width=40, height=70
    set_rgb_color(context, 165, 239, 255)  # Blue fill
    context.fill_preserve()
    context.set_source_rgb(0, 0, 0)  # Black stroke
    context.stroke()

    # Draw the green horizontal rectangle (line) in the middle of the blue rectangle
    context.rectangle(310, 385, 40, 5)  # x=310, y=385, width=40, height=5
    set_rgb_color(context, 0, 160, 93)  # Green fill
    context.fill_preserve()
    context.set_source_rgb(0, 0, 0)  # Black stroke
    context.stroke()

    # Draw the green vertical rectangle (line) in the middle of the blue rectangle
    context.rectangle(330, 355, 5, 70)  # x=330, y=355, width=5, height=70
    set_rgb_color(context, 0, 160, 93)  # Green fill
    context.fill_preserve()
    context.set_source_rgb(0, 0, 0)  # Black stroke
    context.stroke()
