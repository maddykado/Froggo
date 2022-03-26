from pygame import *

init()

screen = display.set_mode((500, 650))
display.set_caption("Froggo")

endProgram = False

while not endProgram:
	
	for e in event.get():
		if e.type == QUIT:
			endProgram = True
			
	screen.fill((210, 42, 42))
	
	draw.rect(screen,(55,16,4), (0,506,500,144))
	draw.rect(screen,(55,16,4), (0,362,500,72))
	draw.rect(screen,(55,16,4), (0,74,500,72))
	
	
	display.update()
