from pygame import *

init()

screen = display.set_mode((500, 650))
display.set_caption("Froggo")

endProgram = False

player_x = 160
player_y = 575
skeleton_x = 417
skeleton_y = 434

while not endProgram:
	
        for e in event.get():
                if e.type == QUIT:
                            endProgram = True
                if e.type == KEYDOWN:
                        if e.key == K_LEFT:
                                player_x = player_x - 83
                        if e.key == K_RIGHT:
                                player_x = player_x + 83
                        if e.key == K_UP:
                                player_y = player_y - 72
                        if e.key == K_DOWN:
                                player_y = player_y + 72



                    
			
        screen.fill((66, 4, 3))
	
        draw.rect(screen,(19,58,11), (0,506,500,144))
        draw.rect(screen,(19,58,11), (0,362,500,72))
        draw.rect(screen,(19,58,11), (0,74,500,72))

        if player_x <= 0:
            player_x = 0
        if player_x >= 417:
            player_x = 417
        if player_y >= 578:
            player_y = 578
        if player_y <= 0:
            player_y = 0


        frog = image.load("frog.png")
        frog = transform.scale(frog, (75,70))

        skeleton = image.load("skeletonman.png")
        skeleton = transform.scale(skeleton, (75,70))

        
        skeleton_x = skeleton_x - 0.5

        if skeleton_x <= - 83:
            skeleton_x = 417

        

        



        screen.blit(skeleton, (skeleton_x, skeleton_y))
        screen.blit(skeleton, (skeleton_x + 166, skeleton_y))
        screen.blit(skeleton, (skeleton_x + 332, skeleton_y))

        screen.blit(skeleton, (skeleton_x + 70, skeleton_y - 216))
        screen.blit(skeleton, (skeleton_x + 332 + 70, skeleton_y -216))
        
        screen.blit(frog, (player_x, player_y))
	
	
        display.update()
