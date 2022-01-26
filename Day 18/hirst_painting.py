# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
#
# print(rgb_colors)

import turtle as t
import random as r


color_palette = [(199, 175, 117), (212, 222, 215), (125, 36, 24), (223, 224, 228), (167, 106, 56), (186, 159, 52),
                 (6, 57, 83), (108, 68, 85), (112, 161, 175), (21, 122, 174), (63, 153, 138), (39, 36, 35),
                 (76, 40, 48), (9, 68, 47), (90, 141, 52), (182, 96, 79), (131, 38, 41), (141, 171, 156),
                 (210, 200, 149), (179, 201, 186), (173, 153, 159), (212, 183, 176), (151, 114, 119), (177, 198, 203),
                 (206, 184, 190), (37, 73, 84), (45, 74, 63), (48, 66, 80)]


figure = t.Turtle()
figure.speed("fastest")
figure.penup()
figure.hideturtle()
screen = t.Screen()
screen.colormode(255)

figure.setheading(225)
figure.forward(300)
figure.setheading(0)
num_of_dots = 100


for dot_count in range(1, num_of_dots + 1):
    figure.dot(15, r.choices(color_palette)[0])
    figure.forward(50)

    if dot_count % 10 == 0:
        figure.setheading(90)
        figure.forward(50)
        figure.setheading(180)
        figure.forward(500)
        figure.setheading(0)


screen.exitonclick()




