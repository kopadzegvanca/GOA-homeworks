import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle object
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(2)

# Function to draw a heart
def draw_heart():
    pen.color("red")
    pen.begin_fill()
    pen.left(50)
    pen.forward(133)
    pen.circle(50, 200)
    pen.right(140)
    pen.circle(50, 200)
    pen.forward(133)
    pen.end_fill()

# Move the pen to position
pen.up()
pen.setpos(0, -200)
pen.down()

# Draw the heart
draw_heart()

# Display "I love you"
pen.up()
pen.setpos(-90, 150)
pen.down()
pen.color("black")
pen.write("I love you", font=("Arial", 24, "bold"))

# Hide the turtle
pen.hideturtle()

# Keep the window open
turtle.done()