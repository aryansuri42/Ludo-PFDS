import interface
import pygame
import sys
def diceroll_step(number, turn):
    if turn == "player2":
        while interface.click:
            a = interface.player2_a
            b = interface.player2_b
            c = interface.player2_c
            d = interface.player2_d
            if a.unlock is False and b.unlock is False and c.unlock is False and d.unlock is False:
                interface.click = False
            else:               
                ev = pygame.event.get()
                for event in ev:
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        if pos[0]>=a.x and pos[0]<=a.x+39 and pos[1]>=a.y and pos[1]<=a.y+64 and a.unlock is True:
                            a.map_yellow(number)
                            
                            interface.click = False
                        elif pos[0]>=b.x and pos[0]<=b.x+39 and pos[1]>=b.y and pos[1]<=b.y+64 and b.unlock is True:
                            b.map_yellow(number)
                            
                            interface.click = False
                        elif pos[0]>=c.x and pos[0]<=c.x+39 and pos[1]>=c.y and pos[1]<=c.y+64 and c.unlock is True:
                            c.map_yellow(number)
                            
                            interface.click = False
                        elif pos[0]>=d.x and pos[0]<=d.x+39 and pos[1]>=d.y and pos[1]<=d.y+64 and d.unlock is True:
                            d.map_yellow(number)
                            
                            interface.click = False
                        elif a.unlock is False and b.unlock is False and c.unlock is False and d.unlock is False:
                            interface.click = False
                        else:
                            interface.click = True
                    elif event.type == pygame.QUIT:
                        sys.exit()
                        
    elif turn=="player1":
        while interface.click:
            a = interface.player1_a
            b = interface.player1_b
            c = interface.player1_c
            d = interface.player1_d
            if a.unlock is False and b.unlock is False and c.unlock is False and d.unlock is False:
                interface.click = False
            else:               
                ev = pygame.event.get()
                for event in ev:
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        if pos[0]>=a.x and pos[0]<=a.x+39 and pos[1]>=a.y and pos[1]<=a.y+64 and a.unlock is True:
                            a.map_blue(number)
                            
                            interface.click = False
                        elif pos[0]>=b.x and pos[0]<=b.x+39 and pos[1]>=b.y and pos[1]<=b.y+64 and b.unlock is True:
                            b.map_blue(number)
                            
                            interface.click = False
                        elif pos[0]>=c.x and pos[0]<=c.x+39 and pos[1]>=c.y and pos[1]<=c.y+64 and c.unlock is True:
                            c.map_blue(number)
                            
                            interface.click = False
                        elif pos[0]>=d.x and pos[0]<=d.x+39 and pos[1]>=d.y and pos[1]<=d.y+64 and d.unlock is True:
                            d.map_blue(number)
                            
                            interface.click = False
                        elif a.unlock is False and b.unlock is False and c.unlock is False and d.unlock is False:
                            interface.click = False
                        else:
                            interface.click = True
                    elif event.type == pygame.QUIT:
                        sys.exit()
    
    elif turn=="player3":
        while interface.click:
            a = interface.player4_a
            b = interface.player4_b
            c = interface.player4_c
            d = interface.player4_d
            if a.unlock is False and b.unlock is False and c.unlock is False and d.unlock is False:
                interface.click = False
            else:                
                ev = pygame.event.get()
                for event in ev:
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        if pos[0]>=a.x and pos[0]<=a.x+39 and pos[1]>=a.y and pos[1]<=a.y+64 and a.unlock is True:
                            a.map_green(number)
                            
                            interface.click = False
                        elif pos[0]>=b.x and pos[0]<=b.x+39 and pos[1]>=b.y and pos[1]<=b.y+64 and b.unlock is True:
                            b.map_green(number)
                            
                            interface.click = False
                        elif pos[0]>=c.x and pos[0]<=c.x+39 and pos[1]>=c.y and pos[1]<=c.y+64 and c.unlock is True:
                            c.map_green(number)
                            
                            interface.click = False
                        elif pos[0]>=d.x and pos[0]<=d.x+39 and pos[1]>=d.y and pos[1]<=d.y+64 and d.unlock is True:
                            d.map_green(number)
                            
                            interface.click = False
                        elif a.unlock is False and b.unlock is False and c.unlock is False and d.unlock is False:
                            interface.click = False
                        else:
                            interface.click = True
                    elif event.type == pygame.QUIT:
                        sys.exit()
    
    elif turn=="player4":
        while interface.click:
            a = interface.player3_a
            b = interface.player3_b
            c = interface.player3_c
            d = interface.player3_d
            if a.unlock is False and b.unlock is False and c.unlock is False and d.unlock is False:
                interface.click = False
            else:                
                ev = pygame.event.get()
                for event in ev:
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        if pos[0]>=a.x and pos[0]<=a.x+39 and pos[1]>=a.y and pos[1]<=a.y+64 and a.unlock is True:
                            a.map_red(number)
                            interface.click = False
                        elif pos[0]>=b.x and pos[0]<=b.x+39 and pos[1]>=b.y and pos[1]<=b.y+64 and b.unlock is True:
                            b.map_red(number)
                            interface.click = False
                        elif pos[0]>=c.x and pos[0]<=c.x+39 and pos[1]>=c.y and pos[1]<=c.y+64 and c.unlock is True:
                            c.map_red(number)
                            interface.click = False
                        elif pos[0]>=d.x and pos[0]<=d.x+39 and pos[1]>=d.y and pos[1]<=d.y+64 and d.unlock is True:
                            d.map_red(number)
                            interface.click = False
                        elif a.unlock is False and b.unlock is False and c.unlock is False and d.unlock is False:
                            interface.click = False
                        else:
                            interface.click = True
                    elif event.type == pygame.QUIT:
                        sys.exit()            

                
