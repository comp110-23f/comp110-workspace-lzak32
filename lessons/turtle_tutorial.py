from turtle import onclick, Turtle, done, Screen
# from turtle import Turtle, colormode, done, circle
# colormode(255)
# leo: Turtle = Turtle()
# leo.color(105,38,149)
# leo.speed(30)
# leo.hideturtle()

# side_length: int = 300
# i: int = 0
# leo.penup()
# leo.goto(-140,-60)
# leo.pendown()
# leo.begin_fill()
# while i < 3:
#     leo.forward(side_length)
#     leo.left(120)
#     i += 1
# leo.end_fill()
bob: Turtle = Turtle()
# bob.color(0,0,0)
# bob.speed(100)

# bob.penup()
# bob.goto(-140,-60)
# bob.pendown()
# ind: int = 0
# while ind < 18:
#     bob.forward(side_length)
#     bob.left(125)
#     ind += 1
#     side_length *= .96

# def make(turt: Turtle, radius: int, color: str) -> None:
#     turt.fillcolor(color)
#     turt.begin_fill()
#     circle(radius)
#     turt.end_fill()

# make(bob,100,'magenta')

# bob.fillcolor('red')
# bob.begin_fill()
# circle(150)
# bob.end_fill()
# bob.fillcolor("red")

# bob.begin_fill()
# circle(100)
# bob.end_fill()

# print(bob.position())


  
  
# method to action 
turt = Turtle()
def fxn(x,y):  
    turt.penup() 
    turt.goto(x,y)
    turt.pendown()
    turt.forward(10)
  
# turtle speed to slowest 
turt.speed(1) 
  
# motion 
# turt.fd(100) 
  
# allow user to click  
# for some action 

print(bob.position())
print(bob.position()[0])

done()