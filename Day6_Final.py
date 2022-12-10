def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
while not at_goal(): 
    if wall_in_front():
        if wall_on_right():
            turn_left()
        elif right_is_clear():
            turn_right()
            move()
    elif not wall_in_front() and not wall_on_right():
        turn_right()
        move()
    elif wall_in_front() and not wall_on_right():
        turn_right()
        move()
    elif wall_on_right():
        move()