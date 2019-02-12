
from turtle import *
import random

omg = Turtle()

omg.color('orange')
omg.pensize()
omg.speed(3)
omg.shape('turtle')
omg.turtlesize(2,2,2)

def drawHexagon():
	for x in range(6):
		omg.forward(50)
		omg.left(60)

for x in range(10):
	drawHexagon()
	omg.forward(54)
	





	

mainloop()