import turtle
import random

#set up screen
ws = turtle.Screen()
ws.bgcolor("#ffcccc")

#set up turtle
faith = turtle.Turtle()
faith.pensize(5)
faith.speed(0)
faith.shape("turtle")


#function to iterate through the colors list
def choose_color():
    colors = ["#ff6666", "#ff8c66", "#ffb366", "#ffd966", "#ffff66", "#d9ff66", "#b3ff66", "#8cff66", "#66ff66", "#66ff8c", "#66ffb3", "#66ffff"]
    for turtle_color in colors:
        yield turtle_color



lengths = [100, 60, 60, 100]
angles = [120, 90, 60, 90]

#function to draw 1 petal
def draw_petal(lengths, angles):

    for side, angle in zip(lengths, angles):
        
        faith.left(angle)
        faith.forward(side)


#function to draw a flower
def draw_flower(lengths, angles):

    color_generator = choose_color()

    for _ in range(12):  # Draw multiple petals around a circle

        faith.color(next(color_generator), "#ff6666")
        
        draw_petal(lengths, angles)  # Draw one petal
        
        faith.right(30)  # Rotate to position the next petal

        
#function to draw 5 flowers at random coordinates
def draw_flowers():
    for _ in range(5):
        faith.penup()
        faith.goto(random.randint(-300, 300), random.randint(-300, 300))
        faith.pendown()
        draw_flower(lengths, angles)


draw_flowers()

faith.hideturtle()

turtle.done()