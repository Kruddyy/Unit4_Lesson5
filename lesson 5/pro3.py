from turtle import *
import random

lol = Turtle()

lol.color('orange')
lol.pensize()
lol.speed(3)
lol.shape('turtle')
lol.turtlesize(2,2,2)

def drawHexagon():
	for x in range(6):
		lol.forward(50)
		lol.left(60)

for x in range(10):
	drawHexagon()
	lol.forward(54)
	





	

mainloop()