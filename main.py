###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##

from turtle import *
import random
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append((new_color))

print(rgb_colors)

color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

drawing_pen = Turtle()
screen = Screen()
screen.colormode(255)
drawing_pen.pensize(25)
drawing_pen.penup()

start_x = -380
start_y = -280

drawing_pen.goto(start_x, start_y)
drawing_pen.pendown()

def paint_dot_row():
    for n in range(10):
        drawing_pen.color(random.choice(color_list))
        drawing_pen.forward(1)
        drawing_pen.penup()
        drawing_pen.forward(50)
        drawing_pen.down()

def move_up_row():
    global start_x
    global start_y
    start_y += 50
    drawing_pen.penup()
    drawing_pen.goto(start_x, start_y)
    drawing_pen.down()

def paint_rows_colum(row_count):
    for n in range(row_count):
        move_up_row()
        paint_dot_row()

paint_rows_colum(15)




screen.exitonclick()



