def draw_a_square(length, angle=90):
    forward(length)
    right(angle)
    forward(length)
    right(angle)
    forward(length)
    rigth(angle)
    forward(length)
    right(angle)

def fly_turtle_fly():
    up()
    right(90)
    forward(150)
    down()

def draw_circle():
    begin_fill()
    fillcolor('red')
    pencolor('green')
    width(10)
    circle(180)
    end_fill()

def draw_star():
    for i in range(5):
        forward(100)
        right(144)

