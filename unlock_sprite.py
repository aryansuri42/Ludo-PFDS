import interface
import pygame
import sys
def unlock(turn):
    if turn=='player2':
        while interface.click:
            a = interface.player2_a
            b = interface.player2_b
            c = interface.player2_c
            d = interface.player2_d
            
            ev = pygame.event.get()   
            for event in ev:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if pos[0]>=a.x and pos[0]<=a.x+39 and pos[1]>=a.y and pos[1]<=a.y+64 and a.unlock is False:
                        a.unlocked_yellow()
                        a.unlock = True
                        interface.click = False
                        
                    elif pos[0]>=a.x and pos[0]<=a.x+39 and pos[1]>=a.y and pos[1]<=a.y+64 and a.unlock is True:
                        if pos[0]>=a.x and pos[0]<=a.x+39 and pos[1]>=a.y and pos[1]<=a.y+64:
                            a.map_yellow(interface.number)
                            interface.click = False
                            
                    elif pos[0]>=b.x and pos[0]<=b.x+39 and pos[1]>=b.y and pos[1]<=b.y+64 and b.unlock is False:
                        b.unlocked_yellow()
                        b.unlock = True
                        interface.click = False
                        
                    elif pos[0]>=b.x and pos[0]<=b.x+39 and pos[1]>=b.y and pos[1]<=b.y+64 and b.unlock is True:
                        if pos[0]>=b.x and pos[0]<=b.x+39 and pos[1]>=b.y and pos[1]<=b.y+64:
                            b.map_yellow(interface.number)
                            interface.click = False
                            
                            
                    elif pos[0]>=c.x and pos[0]<=c.x+39 and pos[1]>=c.y and pos[1]<=c.y+64 and c.unlock is False:
                        c.unlocked_yellow()
                        c.unlock = True
                        interface.click = False
                        
                    elif pos[0]>=c.x and pos[0]<=c.x+39 and pos[1]>=c.y and pos[1]<=c.y+64 and c.unlock is True:
                        if pos[0]>=c.x and pos[0]<=c.x+39 and pos[1]>=c.y and pos[1]<=c.y+64:
                            c.map_yellow(interface.number)
                            interface.click = False
                            
                    elif pos[0]>=d.x and pos[0]<=d.x+39 and pos[1]>=d.y and pos[1]<=d.y+64 and d.unlock is False:
                        d.unlocked_yellow()
                        d.unlock = True
                        interface.click = False
                        
                    elif pos[0]>=d.x and pos[0]<=d.x+39 and pos[1]>=d.y and pos[1]<=d.y+64 and d.unlock is True:
                        if pos[0]>=d.x and pos[0]<=d.x+39 and pos[1]>=d.y and pos[1]<=d.y+64:
                            d.map_yellow(interface.number)
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
            
            ev = pygame.event.get()   
            for event in ev:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if pos[0]>=a.x and pos[0]<=a.x+39 and pos[1]>=a.y and pos[1]<=a.y+64 and a.unlock is False:
                        a.unlocked_blue()
                        a.unlock = True
                        interface.click = False
                        
                    elif pos[0]>=a.x and pos[0]<=a.x+39 and pos[1]>=a.y and pos[1]<=a.y+64 and a.unlock is True:
                        if pos[0]>=a.x and pos[0]<=a.x+39 and pos[1]>=a.y and pos[1]<=a.y+64:
                            a.map_blue(interface.number)
                            interface.click = False
                            
                    elif pos[0]>=b.x and pos[0]<=b.x+39 and pos[1]>=b.y and pos[1]<=b.y+64 and b.unlock is False:
                        b.unlocked_blue()
                        b.unlock = True
                        interface.click = False
                        
                    elif pos[0]>=b.x and pos[0]<=b.x+39 and pos[1]>=b.y and pos[1]<=b.y+64 and b.unlock is True:
                        if pos[0]>=b.x and pos[0]<=b.x+39 and pos[1]>=b.y and pos[1]<=b.y+64:
                            b.map_blue(interface.number)
                            interface.click = False
                            
                            
                    elif pos[0]>=c.x and pos[0]<=c.x+39 and pos[1]>=c.y and pos[1]<=c.y+64 and c.unlock is False:
                        c.unlocked_blue()
                        c.unlock = True
                        interface.click = False
                        
                    elif pos[0]>=c.x and pos[0]<=c.x+39 and pos[1]>=c.y and pos[1]<=c.y+64 and c.unlock is True:
                        if pos[0]>=c.x and pos[0]<=c.x+39 and pos[1]>=c.y and pos[1]<=c.y+64:
                            c.map_blue(interface.number)
                            interface.click = False
                            
                    elif pos[0]>=d.x and pos[0]<=d.x+39 and pos[1]>=d.y and pos[1]<=d.y+64 and d.unlock is False:
                        d.unlocked_blue()
                        d.unlock = True
                        interface.click = False
                        
                    elif pos[0]>=d.x and pos[0]<=d.x+39 and pos[1]>=d.y and pos[1]<=d.y+64 and d.unlock is True:
                        if pos[0]>=d.x and pos[0]<=d.x+39 and pos[1]>=d.y and pos[1]<=d.y+64:
                            d.map_blue(interface.number)
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
            
            ev = pygame.event.get()   
            for event in ev:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if pos[0]>=a.x and pos[0]<=a.x+39 and pos[1]>=a.y and pos[1]<=a.y+64 and a.unlock is False:
                        a.unlocked_green()
                        a.unlock = True
                        interface.click = False
                        
                    elif pos[0]>=a.x and pos[0]<=a.x+39 and pos[1]>=a.y and pos[1]<=a.y+64 and a.unlock is True:
                        if pos[0]>=a.x and pos[0]<=a.x+39 and pos[1]>=a.y and pos[1]<=a.y+64:
                            a.map_green(interface.number)
                            interface.click = False
                            
                    elif pos[0]>=b.x and pos[0]<=b.x+39 and pos[1]>=b.y and pos[1]<=b.y+64 and b.unlock is False:
                        b.unlocked_green()
                        b.unlock = True
                        interface.click = False
                        
                    elif pos[0]>=b.x and pos[0]<=b.x+39 and pos[1]>=b.y and pos[1]<=b.y+64 and b.unlock is True:
                        if pos[0]>=b.x and pos[0]<=b.x+39 and pos[1]>=b.y and pos[1]<=b.y+64:
                            b.map_green(interface.number)
                            interface.click = False
                            
                            
                    elif pos[0]>=c.x and pos[0]<=c.x+39 and pos[1]>=c.y and pos[1]<=c.y+64 and c.unlock is False:
                        c.unlocked_green()
                        c.unlock = True
                        interface.click = False
                        
                    elif pos[0]>=c.x and pos[0]<=c.x+39 and pos[1]>=c.y and pos[1]<=c.y+64 and c.unlock is True:
                        if pos[0]>=c.x and pos[0]<=c.x+39 and pos[1]>=c.y and pos[1]<=c.y+64:
                            c.map_green(interface.number)
                            interface.click = False
                            
                    elif pos[0]>=d.x and pos[0]<=d.x+39 and pos[1]>=d.y and pos[1]<=d.y+64 and d.unlock is False:
                        d.unlocked_green()
                        d.unlock = True
                        interface.click = False
                        
                    elif pos[0]>=d.x and pos[0]<=d.x+39 and pos[1]>=d.y and pos[1]<=d.y+64 and d.unlock is True:
                        if pos[0]>=d.x and pos[0]<=d.x+39 and pos[1]>=d.y and pos[1]<=d.y+64:
                            d.map_green(interface.number)
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
            
            ev = pygame.event.get()   
            for event in ev:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if pos[0]>=a.x and pos[0]<=a.x+39 and pos[1]>=a.y and pos[1]<=a.y+64 and a.unlock is False:
                        a.unlocked_red()
                        a.unlock = True
                        interface.click = False
                        
                    elif pos[0]>=a.x and pos[0]<=a.x+39 and pos[1]>=a.y and pos[1]<=a.y+64 and a.unlock is True:
                        if pos[0]>=a.x and pos[0]<=a.x+39 and pos[1]>=a.y and pos[1]<=a.y+64:
                            a.map_red(interface.number)
                            interface.click = False
                            
                    elif pos[0]>=b.x and pos[0]<=b.x+39 and pos[1]>=b.y and pos[1]<=b.y+64 and b.unlock is False:
                        b.unlocked_red()
                        b.unlock = True
                        interface.click = False
                        
                    elif pos[0]>=b.x and pos[0]<=b.x+39 and pos[1]>=b.y and pos[1]<=b.y+64 and b.unlock is True:
                        if pos[0]>=b.x and pos[0]<=b.x+39 and pos[1]>=b.y and pos[1]<=b.y+64:
                            b.map_red(interface.number)
                            interface.click = False
                            
                            
                    elif pos[0]>=c.x and pos[0]<=c.x+39 and pos[1]>=c.y and pos[1]<=c.y+64 and c.unlock is False:
                        c.unlocked_red()
                        c.unlock = True
                        interface.click = False
                        
                    elif pos[0]>=c.x and pos[0]<=c.x+39 and pos[1]>=c.y and pos[1]<=c.y+64 and c.unlock is True:
                        if pos[0]>=c.x and pos[0]<=c.x+39 and pos[1]>=c.y and pos[1]<=c.y+64:
                            c.map_red(interface.number)
                            interface.click = False
                            
                    elif pos[0]>=d.x and pos[0]<=d.x+39 and pos[1]>=d.y and pos[1]<=d.y+64 and d.unlock is False:
                        d.unlocked_red()
                        d.unlock = True
                        interface.click = False
                        
                    elif pos[0]>=d.x and pos[0]<=d.x+39 and pos[1]>=d.y and pos[1]<=d.y+64 and d.unlock is True:
                        if pos[0]>=d.x and pos[0]<=d.x+39 and pos[1]>=d.y and pos[1]<=d.y+64:
                            d.map_red(interface.number)
                            interface.click = False
                            
                    else:
                        interface.click = True
                elif event.type == pygame.QUIT:
                        sys.exit()