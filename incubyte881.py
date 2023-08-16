#!/usr/bin/env python
# coding: utf-8

# In[15]:


class Spacecraft:
    def __init__(self, initial_position, initial_direction):
        self.position = initial_position
        if(initial_direction in ["Up","Down"]):
            self.vdirection = initial_direction
            self.hdirection="N"
        else:
            self.hdirection = initial_direction
            self.vdirection="Up"
        
        self.main_direction=initial_direction

    def move_forward(self):
        if self.main_direction == "N":
            self.position[1] += 1
        elif self.main_direction == "S":
            self.position[1] -= 1
        elif self.main_direction == "E":
            self.position[0] += 1
        elif self.main_direction == "W":
            self.position[0] -= 1
        elif self.main_directionn == "Up":
            self.position[2] += 1
        elif self.main_direction == "Down":
            self.position[2] -= 1

    def move_backward(self):
        if self.main_direction == "N":
            self.position[1] -= 1
        elif self.main_direction == "S":
            self.position[1] += 1
        elif self.main_direction == "E":
            self.position[0] -= 1
        elif self.main_direction == "W":
            self.position[0] += 1
        elif self.main_direction == "Up":
            self.position[2] -= 1
        elif self.main_direction == "Down":
            self.position[2] += 1

    def turn_left(self):
        if self.hdirection == "N":
            self.hdirection = "W"
            self.main_direction="W"
        elif self.hdirection == "S":
            self.hdirection = "E"
            self.main_direction="E"
        elif self.hdirection == "E":
            self.hdirection = "N"
            self.main_direction="N"
        elif self.hdirection == "W":
            self.hdirection = "S"
            self.main_direction="S"

    def turn_right(self):
        if self.hdirection == "N":
            self.hdirection = "E"
            self.main_direction="E"
        elif self.hdirection == "S":
            self.hdirection = "W"
            self.main_direction="W"
        elif self.hdirection == "E":
            self.hdirection = "S"
            self.main_direction="S"
        elif self.hdirection == "W":
            self.hdirection = "N"
            self.main_direction="N"

    def rotate_up(self):
        self.vdirection = "Up"
        self.main_direction = "Up"

    def rotate_down(self):
        self.vdirection = "Down"
        self.main_direction = "Down"


# In[16]:


def execute_commands(commands, initial_position, initial_direction):
    spacecraft = Spacecraft(initial_position, initial_direction)
    
    for command in commands:
        if command == "f":
            spacecraft.move_forward()
        elif command == "b":
            spacecraft.move_backward()
        elif command == "l":
            spacecraft.turn_left()
        elif command == "r":
            spacecraft.turn_right()
        elif command == "u":
            spacecraft.rotate_up()
        elif command == "d":
            spacecraft.rotate_down()
    
    return spacecraft.position, spacecraft.main_direction


# In[20]:


initial_position = [0, 0, 0]
initial_direction = input("Enter initial direction (N/S/E/W): ")
commands = input("Enter commands (f/r/u/b/l without spaces): ")
final_position, final_direction = execute_commands(commands, initial_position, initial_direction)
print("Final Position:", final_position)
print("Final Direction:", final_direction)

