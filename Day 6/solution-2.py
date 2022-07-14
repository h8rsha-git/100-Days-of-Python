# Problem link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json

def turn_right():
    for i in range(0,3):
        turn_left()
 
def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

def path_finder():
    while not at_goal():
        if wall_in_front():
            jump()
        else:
            move()

path_finder()