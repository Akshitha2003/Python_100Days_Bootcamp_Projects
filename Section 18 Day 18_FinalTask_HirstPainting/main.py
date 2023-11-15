# import colorgram
#
# colors = colorgram.extract('image.jpg', 25)
#
# rgb_colors = []
# rgb_colors_tuple = []
# for color in colors:
#     rgb_colors.append(color.rgb)
#     color_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_colors_tuple.append(color_tuple)
# print(rgb_colors)
# print(rgb_colors_tuple)

import turtle
import random

turtle.colormode(255)

# Got the below color_list from the above commented code
color_list = [(211, 210, 210), (189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (210, 212, 214), (208, 211, 208), (211, 209, 210), (64, 43, 43), (171, 183, 170), (136, 149, 69), (127, 160, 172), (101, 79, 89), (83, 133, 108), (108, 39, 44), (39, 61, 47), (45, 40, 41), (211, 196, 124), (174, 150, 152), (36, 71, 88), (179, 106, 80), (36, 67, 84), (207, 185, 181), (99, 140, 119), (184, 198, 181)]

tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
tim.speed("fastest")

x = -200
y = -200
tim.setx(x)
tim.sety(y)

for i in range(10):
    for j in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.setx(x)
    tim.sety(tim.position()[1] + 50)

screen = turtle.Screen()
screen.exitonclick()
