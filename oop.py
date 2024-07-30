# from turtle import Turtle
# from turtle import Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
#
# my_screen = Screen()
#
# print(my_screen.canvwidth)
# my_screen.exitonclick()
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtie","Charmander"])
table.add_column("Type", ["Electric","water","fire"])
table.align = "l"
print(table)