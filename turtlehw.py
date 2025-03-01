from turtle import *
import random

title("turtle hw") # customize the title of your turtle sketch window
shape('turtle')
speed(0)
pensize(2)
colormode(255)
bgcolor("lightblue")
pencolor('blue')


#Canvas Size:
width=300
height=300
#Size of a tile:
size = 50

def drawSquare(x, y, size):
    penup()
    goto(x - size / 2 + randomise(), y - size / 2 + randomise())
    pendown()
    goto(x + size / 2 + randomise(), y - size / 2 + randomise())
    goto(x + size / 2 + randomise(), y + size / 2 + randomise())
    goto(x - size / 2 + randomise(), y + size / 2 + randomise())
    goto(x - size / 2 + randomise(), y - size / 2 + randomise())

def drawTile(x, y, size):
  for i in range(0,9):
    drawSquare(x, y, size)
    size -= random.randint(0,10)

def randomise(): 
  return (random.randint(0,10)/10 -0.5) * 6

def draw():
  for x in range(0,width + size, size):
    for y in range(0,height + size, size):
      drawTile(x-150, y-150, size * 0.95)
      
      
draw()      

mainloop()