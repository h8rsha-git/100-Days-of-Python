# Problem link : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json


def turn_right():
    for i in range(0,3):
        turn_left()

def forward_left():
    move()
    turn_left()


def forward_right():
    move()
    turn_right()

def special_move():
    forward_left()
    forward_right()
    forward_right()
    forward_left()


def path_finder():
    for i in range(0,6):
        special_move()

path_finder()