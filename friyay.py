from turtle import *

def center_turtle():
  up()
  forward(50)
  left(90)
  forward(50)
  left(270)

  down()

# def draw_a_square(length, angle=90):
def draw_a_square():
  forward(100)
  right(90)
  forward(100)
  right(90)
  forward(100)
  right(90)
  forward(100)

  # forward(length)
  # right(angle)
  # forward(length)
  # right(angle)
  # forward(length)
  # right(angle)
  # forward(length)

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

def main():
  center_turtle()
  # draw_star()
  draw_circle()

  # draw_a_square()
  # fly_turtle_fly()

  # draw_a_square()
  # fly_turtle_fly()

  # draw_a_square()

  mainloop()

main()