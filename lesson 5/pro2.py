from turtle import *

lol = Turtle()

lol.color('orange')
lol.pensize()
lol.speed(3)
lol.shape('turtle')
lol.turtlesize(2,2,2)

def drawTriangle():
	for x in range(3):
		lol.forward(80)
		lol.left(120)

for x in range(12):
	drawTriangle()
	lol.left(30)

	

mainloop()