#day18
import  turtle as t
from turtle import Screen
import random
timmy = t.Turtle()
timmy.shape("turtle")
#challenge 1
# for i in range(50):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
    
# isDone = True
# shapes = 0
# sides = 3
# while isDone:
#     angle = 360/sides
#     for _ in range(1,10):
#         timmy.forward(100)
#         timmy.right(angle)
#     shapes+=1
#     sides+=1        
#     if(shapes == 10):
#         isDone = False
colours = ["red","orange","yellow","green","blue","purple"]
directions = [0,90,180,270]
timmy.pensize(15)
timmy.speed("fastest")
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color
        # challenge 2
# def draw(sides):
#     angle = 360/sides
#     for _ in range(sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#challenge 3

# for shapeSides in range (3,11):
#     draw(shapeSides)
#     timmy.color(random.choices(colours))


# challenge 4
# for j in range(200):
#     # timmy.color(random.choice(colours))
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))
# # for _ in range(100):
#     timmy.color(random_color())
#     timmy.circle(100)
#     timmy.setheading(timmy.heading()+5)
    
# #challenge 5 
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         timmy.color(random_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading()+size_of_gap)

# draw_spirograph(5)



import colorgram

# colorss = colorgram.extract("image.png", 10)
# print(colorss)


import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)








screen = Screen()
screen.exitonclick()
