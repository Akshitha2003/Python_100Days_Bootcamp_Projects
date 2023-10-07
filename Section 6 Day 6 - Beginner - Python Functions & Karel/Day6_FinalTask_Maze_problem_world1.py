# Maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_back():
    turn_left()
    turn_left()

i = 0
while not at_goal():
    if not wall_on_right() and i == 4:
        turn_back()
        move()
        i = 0
    elif not wall_on_right():
        turn_right()
        move()
        i += 1
    elif not wall_in_front():
        move()
    else:
        turn_left()
        
#def turn_right():
#    turn_left()
#    turn_left()
#    turn_left()
#
#while front_is_clear:
#    move()
#turn_left()
#
#while not at_goal():
#    if not wall_on_right():
#        turn_right()
#        move()
#    elif not wall_in_front():
#        move()
#    else:
#        turn_left()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
