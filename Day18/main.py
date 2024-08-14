from turtle import Turtle, Screen
import heroes

tim = Turtle()
tim.shape('turtle')
tim.pencolor(0.2, 0.8, 0.55)


for i in range(5):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()



my_screen = Screen()
my_screen.exitonclick()