# use this link:
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=problem_world3.json&url=user_world%3Aproblem_world3.json
def turn_right():
    for _ in range(3):
        turn_left()


def jump():
    while not front_is_clear():
        if wall_in_front() and wall_on_right():
            turn_left()
        elif wall_in_front() and not wall_on_right():
            turn_right()
    move()


while not at_goal():
    if front_is_clear() and right_is_clear():
        move()
    else:
        jump()