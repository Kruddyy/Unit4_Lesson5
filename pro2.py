from turtle import *

MAMAMIA = Turtle()

MAMAMIA.color('orange')
MAMAMIA.pensize()
MAMAMIA.speed(3)
MAMAMIA.shape('turtle')
MAMAMIA.turtlesize(2,2,2)

def drawTriangle():
	for x in range(3):
		MAMAMIA.forward(80)
		MAMAMIA.left(120)

for x in range(12):
	drawTriangle()
	MAMAMIA.left(30)

	

mainloop()