import interface
def lock_case(turn_player):
    l1 = [interface.player1_a, interface.player1_b, interface.player1_c, interface.player1_d]
    l2 = [interface.player2_a, interface.player2_b, interface.player2_c, interface.player2_d]
    l3 = [interface.player3_a, interface.player3_b, interface.player3_c, interface.player3_d]
    l4 = [interface.player4_a, interface.player4_b, interface.player4_c, interface.player4_d]
    if turn_player=='player1':
        for i in l1:
            for j in l2:
                if i.x==j.x and i.y==j.y:
                    j.unlock=False
                    j.locked()
                    break
                else:
                    continue
                
            for k in l3:
                if i.x==k.x and i.y==k.y:
                    k.unlock=False
                    k.locked()
                    break
                else:
                    continue
            for l in l4:
                if i.x==l.x and i.y==l.y:
                    l.unlock=False
                    l.locked()
                    break
                else:
                    continue
       
    elif turn_player=='player2':
        for i in l2:
            for j in l1:
                if i.x==j.x and i.y==j.y:
                    j.unlock=False
                    j.locked()
                    break
                else:
                    continue
            for k in l3:
                if i.x==k.x and i.y==k.y:
                    k.unlock=False
                    k.locked()
                    break
                else:
                    continue
            for l in l4:
                if i.x==l.x and i.y==l.y:
                    l.unlock=False
                    l.locked()
                    break
                else:
                    continue
    
    elif turn_player=='player4':
        for i in l3:
            for j in l1:
                if i.x==j.x and i.y==j.y:
                    j.unlock=False
                    j.locked()
                    break
                else:
                    continue
            for k in l2:
                if i.x==k.x and i.y==k.y:
                    k.unlock=False
                    k.locked()
                    break
                else:
                    continue
            for l in l4:
                if i.x==l.x and i.y==l.y:
                    l.unlock=False
                    l.locked()
                    break
                else:
                    continue
                      
    elif turn_player=='player3':
        for i in l4:
            for j in l1:
                if i.x==j.x and i.y==j.y:
                    j.unlock=False
                    j.locked()
                    break
                else:
                    continue
            for k in l2:
                if i.x==k.x and i.y==k.y:
                    k.unlock=False
                    k.locked()
                    break
                else:
                    continue
            for l in l3:
                if i.x==l.x and i.y==l.y:
                    l.unlock=False
                    l.locked()
                    break
                else:
                    continue