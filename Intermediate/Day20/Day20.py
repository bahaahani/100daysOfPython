from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

segments = []
starting_position = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_position:
    segment = Turtle(shape="square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    segments.append(segment)



game_is_on = True
while game_is_on:
    screen.update()
    for segno in range(len(segments) - 1, 0, -1):
        new_x = segments[segno - 1].xcor()
        new_y = segments[segno - 1].ycor()
        segments[segno].goto(new_x, new_y)
    segments[0].forward(20)






screen.exitonclick()