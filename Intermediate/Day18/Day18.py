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

colorss = colorgram.extract("image.jpg", 30)
print(colorss)








screen = Screen()
screen.exitonclick()
