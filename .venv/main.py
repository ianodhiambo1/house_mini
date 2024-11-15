import cairo
import math

# Define constants for the surface size
WIDTH, HEIGHT = 700, 500

# Helper function to set RGB colors using 0–255 values
def set_rgb_color(context, r, g, b):
    context.set_source_rgb(r / 255, g / 255, b / 255)

# Create a surface and context
surface = cairo.ImageSurface(cairo.FORMAT_RGB30, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Set the background color to white
context.set_source_rgb(1, 1, 1)  # White
context.paint()

# Draw the first polygon
context.move_to(100, 200)
context.line_to(100, 350)
context.line_to(270, 450)
context.line_to(272, 240)
context.line_to(200, 90)
context.close_path()

context.set_source_rgb(0, 0, 0)  # Black for stroke
context.set_line_width(4)
context.stroke_preserve()

set_rgb_color(context, 216, 165, 141)  # Fill color
context.fill()

# Draw the second polygon
context.move_to(500, 370)
context.line_to(500, 250)
context.line_to(560, 230)
context.line_to(560, 350)

context.close_path()

context.set_source_rgb(0, 0, 0)  # Black for stroke
context.set_line_width(4)
context.stroke_preserve()

set_rgb_color(context, 164, 106, 85)  # Fill color
context.fill()


# Draw the second polygon
context.move_to(270, 450)
context.line_to(500, 380)
context.line_to(500, 250)
context.line_to(560, 230)
context.line_to(560, 360)
context.line_to(600, 345)
context.line_to(600, 190)
context.line_to(272, 240)
context.close_path()

context.set_source_rgb(0, 0, 0)  # Black for stroke
context.set_line_width(4)
context.stroke_preserve()

set_rgb_color(context, 255, 230, 202)  # Fill color
context.fill()

# Draw the third polygon
context.move_to(90, 210)
context.line_to(200, 90)
context.line_to(290, 270)
context.line_to(610, 190)
context.line_to(612, 180)
context.line_to(540, 40)
context.line_to(200, 80)
context.line_to(90, 200)
context.close_path()

context.set_source_rgb(0, 0, 0)  # Black for stroke
context.set_line_width(4)
context.stroke_preserve()

set_rgb_color(context, 240, 93, 48)  # Fill color
context.fill()

# Draw the second polygon
context.move_to(560, 360)
context.line_to(552, 355)
context.line_to(550, 235)
context.line_to(558, 234)

context.close_path()

context.set_source_rgb(0, 0, 0)  # Black for stroke
context.set_line_width(4)
context.stroke_preserve()

set_rgb_color(context, 216, 165, 141)  # Fill color
context.fill()

# Draw a small circle
context.arc(540, 300, 5, 0, 2 * 3.14159)  # x=500, y=300, radius=10
context.set_source_rgb(1, 1, 0)  # Fill color: yellow
context.fill_preserve()
context.set_source_rgb(0, 0, 0)  # Stroke color: black
context.stroke()



context.move_to(90, 200)
context.line_to(200, 80)
context.line_to(205, 78)
context.line_to(295, 260)
context.line_to(290, 270)
context.line_to(200, 90)
context.line_to(90, 210)

context.set_source_rgb(0, 0, 0)  # Black for stroke
context.set_line_width(2)
context.stroke_preserve()

set_rgb_color(context, 185, 48, 17)  # Fill color
context.fill()

context.move_to(295, 260)
context.line_to(612, 182)
context.set_source_rgb(0, 0, 0)  # Black for stroke
context.set_line_width(2)
context.stroke_preserve()


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


# Draw the first window
draw_window(context, x_offset=0, y_offset=0, angle=-10)

# Reset transformation matrix for the next window
context.identity_matrix()

# Draw the second window 50 pixels next to the first one
draw_window(context, x_offset=100, y_offset=-20, angle=-10)

draw_window_side(context, x_offset=-250, y_offset=-300, angle=35)



# Save the result to a file
surface.write_to_png("output.png")
print("Drawing saved to output.png")
