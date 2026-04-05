"""
File: PotholeFilling.py
Name: TODO:戴詠晨
--------------------------
This program demonstrates how Karel fills multiple potholes
by using decomposition.

In this program, we will guide Karel to fix three potholes
on the road. Instead of writing all the commands in one place,
we will practice breaking a big task into smaller, reusable
functions to make the program clearer and easier to manage.
"""

from karel.stanfordkarel import *

def go_in():
    move()
    rightward_turn()
    move()
def put_beeper99():
    for i in range(99):
        put_beeper()
def go_out():
    turn_left()
    turn_left()
    move()
    rightward_turn()
    move()
def rightward_turn():
    turn_left()
    turn_left()
    turn_left()
def main():
    """
    TODO:戴詠晨
    """
    for i in range(3):
        go_in()
        put_beeper99()
        go_out()





# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
