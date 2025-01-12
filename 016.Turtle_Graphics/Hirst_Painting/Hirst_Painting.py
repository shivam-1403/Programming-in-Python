# import colorgram
# file_path = r"D:\Python Code\Programming-in-Python\016.Turtle_Graphics\Hirst_Painting\hirst_spot_painting.jpg"

# rgb_colors = []
# colors = colorgram.extract(file_path, 30)

# for color in colors :
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)


# 👆👆 Above code is used to generate a list of colors, it is not of use now. 

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]

import turtle
from turtle import Screen
import random

tim = turtle.Turtle()
tim.shape("turtle")
tim.speed("fastest")
turtle.colormode(255)

tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.pendown()
number_of_dots = 100


for i in range(1, number_of_dots + 1) :
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()