import random
from turtle import Turtle, Screen


def run_game():
    is_race_on = False
    screen = Screen()
    screen.tracer(1)
    screen.title("Run Turtle Run")
    screen.setup(width=1200, height=600)
    screen.bgpic("run_path.png")
    finish_line = Turtle()
    finish_line.hideturtle()
    finish_line.penup()
    finish_line.setx(506)
    finish_line.sety(220)
    finish_line.pendown()
    finish_line.goto(506, -220)
    colors = ["orange", "black", "green", "blue", "cyan", "purple", "gray", "yellow", "pink", "red"]
    y_positions = [-215, -153, -93, -29, 32, 94, 155, 215]
    all_turtle = []

    for i in range(0, 8):
        turtle = Turtle(shape="turtle")
        turtle.penup()
        # turtle.circle(45)
        turtle.shapesize(1.5)
        turtle.color(colors[i])
        turtle.goto(x=-573, y=y_positions[i])
        all_turtle.append(turtle)
    bet = screen.textinput("Which Turtle Win?", "Pick a color")
    if bet:
        is_race_on = True
    while is_race_on:

        for x in all_turtle:
            screen.update()
            x.forward(random.randint(1, 20))
            print(f"{x.pencolor()}, {x.xcor()} cm")
            # print(f"{x.distance(finish_line)}")
            if x.distance(finish_line) < x.distance(finish_line):
                print(f"{x.distance(finish_line)}")
            if x.xcor() >= 489:
                is_race_on = False
                winning_color = x.pencolor()
                print(f"Kazanan Renk : {x.pencolor()}, {x.xcor()}")

                if winning_color == bet:
                    result = screen.textinput(f"{winning_color} wins!", f"Win! Play Again Y or N ").lower()
                    if result == "y":
                        screen.clearscreen()
                        run_game()
                    else:
                        screen.exitonclick()
                else:
                    result = screen.textinput(f"{winning_color} wins!", f"Fail! Play Again Y or N ").lower()
                    if result == "y":
                        screen.clearscreen()
                        run_game()
                    else:
                        screen.exitonclick()


run_game()
