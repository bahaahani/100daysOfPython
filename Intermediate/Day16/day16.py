# day16
from turtle import Turtle, Screen
from prettytable import PrettyTable

# timmy = Turtle()
# print(timmy)
# myscreen = Screen()

# print(myscreen.canvheight)
# timmy.shape("turtle")
# timmy.color("coral")


# for i in range(0, 10):
#     timmy.forward(100)
#     timmy.right(90)
#     timmy.backward(169)

# myscreen.exitonclick()

x = PrettyTable()
x.field_names = ["Pokemon Name", "Type"]
x.add_row(["Pikachu", "Electric"])
x.add_row(["Squirtle", "Water"])
x.add_row(["Charmander", "Fire"])
print(x)

y = PrettyTable()
y.field_names = ["femboy Name", "type"]
y.add_row(["kyte", "meow"])
y.add_row(["mouse", "bitch"])
y.align = "l"
print(y)
z = PrettyTable()
z.add_column("Pockemon Name", ["bekatchu", "squirtle", "charmander"])
z.add_column("type", ["electric", "water", "fire"])
z.align = 'r'
print(z)
