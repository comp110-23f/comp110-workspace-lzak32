"""Christmas vibes."""
from turtle import Turtle, colormode, done, bgcolor, Screen, tracer, update
from random import randint
"""I satisfy the above and beyond - breaks up complex functions by breaking up the snowman. 
function on line 80 with other functions, like initialize, make_circle, eyes, and triangle and also by using a loop.
I satisfy the above and beyond - try something fun! because I used turtle functions we did not use in class
(onclick, Screen, circle) and because, when the user clicks the screen, I use a loop to generate a symmetrical snowflake
with a random amount of branches. This function can be seen on line 129, and its onclick function handler is written 
on line 121 and implemented on line 33
"""
__author__ = "730679428"

donatello: Turtle = Turtle()


def main() -> None:
    """The entrypoint of my scene."""
    # declare vars, call procedures
    # default window dimensions are 400pix wide by 300 high
    colormode(255)
    scr = Screen()
    bgcolor(181, 233, 234)
    tracer(0, 0)
    rectangle(donatello, [-400.0, -200.0], 800, 200, "white")
    rectangle(donatello, [-300.0, 100.0], 50, 300, 'burlywood4')
    triangle(donatello, [-390.0, 100.0], 240, 120, "green")
    snowman(donatello, [0.0, -200.0], 80, 'white')
    rectangle(donatello, [-150.0, 55.0], 100, 10, 'burlywood4')
    rectangle(donatello, [50.0, 55.0], 100, 10, 'burlywood4')
    hat(donatello, [-40.0, 185.0], 'black')
    update()
    tracer(1, 25)
    scr.onclick(go_to)
    done()


def initialize(turt: Turtle, start: list[float], color: str) -> None:
    """Initializes turtle."""
    turt.speed(0)
    turt.color(color)
    turt.penup()
    turt.goto(start[0], start[1])
    turt.pendown()


def rectangle(turt: Turtle, start: list[float], width: int, height: int, color: str) -> None:
    """Makes a rectangle starting from the top right."""
    initialize(turt, start, color)
    turt.fillcolor(color)
    turt.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            turt.forward(width)
        else: 
            turt.forward(height)
        turt.right(90)
    turt.end_fill()


def triangle(turt: Turtle, start: list[float], side_length: int, angle: int, color: str) -> None:
    """Makes a triangle starting from bottom right vertex."""
    initialize(turt, start, color)
    turt.fillcolor(color)
    turt.begin_fill()
    for i in range(3):
        turt.forward(side_length)
        turt.left(120)
    turt.end_fill()


def make_circle(turt: Turtle, start: list[float], radius: int, color: str) -> None:
    """Makes a circle."""
    initialize(turt, start, color)
    turt.fillcolor(color)
    turt.begin_fill()
    turt.circle(radius)
    turt.end_fill()


def snowman(turt: Turtle, start: list[float], big_radius: int, color: str) -> None:
    """Function to create body, nose, eyes of snowman."""
    initialize(turt, start, color)
    make_circle(turt, start, big_radius, color)
    r: int = big_radius
    for i in range(2):
        turt.left(90)
        turt.forward(r * 2)
        turt.right(90)
        if i % 2 == 0:
            r -= 20
        else: 
            r -= 10
        make_circle(turt, [turt.position()[0], turt.position()[1]], r, color)
    turt.left(90)
    turt.forward(big_radius - 30)
    # uses a triangle to create the nose
    turt.left(180)
    triangle(turt, [turt.position()[0], turt.position()[1]], 20, 120, 'orange')
    # creates first eye of the snowman
    eyes(turt, [turt.position()[0], turt.position()[1]], 5, 'black', big_radius)


def eyes(turt: Turtle, start: list[float], eye_r: int, color: str, snow_rad: int) -> None:
    """Creates the eyes of the snowman."""
    turt.left(180)
    turt.penup()
    turt.forward((snow_rad - 30) / 4)
    turt.left(90)
    turt.forward((snow_rad - 30) / 4)
    make_circle(turt, [turt.position()[0], turt.position()[1]], eye_r, color)
    turt.left(180)
    # creates second eye of the snowman
    turt.penup()
    turt.right(90)
    turt.forward(10)
    turt.left(90)
    turt.forward(2 * ((snow_rad - 30) / 4))
    make_circle(turt, [turt.position()[0], turt.position()[1]], 5, 'black')


def go_to(x: float, y: float) -> None:
    """Click event handler. This function allows snowflakes to be generated where the user clicks."""
    donatello.penup()
    donatello.goto(x, y)
    donatello.pendown()
    random_snowflake(donatello, [x, y], 25, 'white')


def random_snowflake(turt: Turtle, start: list[float], size: int, color: str) -> None:
    """Generates a symmetrical snowflake with a random number of branches."""
    branches: int = randint(3, 12)
    initialize(turt, start, color)
    for i in range(branches):
        turt.forward(size)
        turt.left(180)
        turt.forward(size)
        turt.left(180)
        turt.left(360 / branches)


def hat(turt: Turtle, start: list[float], color: str) -> None:
    """Creates the hat of the snowman."""
    rectangle(turt, start, 80, 10, color)
    rectangle(turt, [start[0] + 10.0, start[1] + 80.0], 60, 80, color)


if __name__ == "__main__":
    main()