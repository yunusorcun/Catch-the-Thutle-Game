import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")

# Main turtle setup
main_turtle = turtle.Turtle()
main_turtle.shape("turtle")
main_turtle.shapesize(2, 2, 2)
main_turtle.fillcolor("black")
main_turtle.color("red")
main_turtle.hideturtle()  # Hide the main turtle

# Score turtle setup
score_turtle = turtle.Turtle()
FONT = ('Cebri', 15, 'normal')

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("black")
    score_turtle.penup()

    top_height = screen.window_height() / 2
    y = top_height * 0.8
    score_turtle.setpos(0, y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)

setup_score_turtle()

turtle.mainloop()
