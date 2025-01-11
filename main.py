import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
score=0
start_time=time.time()# start timer

# Main turtle setup
main_turtle = turtle.Turtle()
main_turtle.shape("turtle")
main_turtle.shapesize(2, 2, 2)
main_turtle.fillcolor("black")
main_turtle.color("red")
main_turtle.hideturtle()  # Hide the main turtle


#turtle list
turtle_list=[]

# Score turtle setup
score_turtle = turtle.Turtle()
FONT = ('Cebri', 15, 'normal')

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("black")
    score_turtle.penup()
    score_turtle.hideturtle()
    top_height = screen.window_height() / 2
    y = top_height * 0.8
    score_turtle.setpos(0, y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)

grid_size=11
def make_turtle(x,y):
    t=turtle.Turtle()

    def handle_click(x, y): #I used this fonction for detect on turtle
        #print(x, y)
        global score
        score+=1
        score_turtle.clear()
        score_turtle.write(arg=f"Score:{score}", move=False, align="center", font=FONT) # I used 'f' to enter data.


    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2, 2)
    t.fillcolor("black")
    t.color("red")
    t.goto(x*grid_size,y*grid_size)
    turtle_list.append(t)

x_coordinates=[-20,-10,0,10,20]
y_coordinates=[20,10,0,-10,-20]
def random_turtles():

    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x,y)
def hide_turtles():
    for t in turtle_list:
        t.hideturtle()

#recursive function
def show_turtles_rondomly():
    hide_turtles()    #We have a lot of turtles right now ,but I need only one that's why we can use hide_turtles function.
    random.choice(turtle_list).showturtle()
    elapsed_time=time.time()-start_time
    if score==10 or elapsed_time>=30:
        print("level up")
        return

    screen.ontimer(show_turtles_rondomly, 1000)

turtle.tracer(0)
setup_score_turtle()
random_turtles()
hide_turtles()
show_turtles_rondomly()
turtle.tracer(1)
turtle.mainloop()
