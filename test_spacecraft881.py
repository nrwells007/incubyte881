#!/usr/bin/env python
# coding: utf-8

# In[60]:


import unittest
from incubyte881 import Spacecraft, execute_commands

class TestSpacecraft(unittest.TestCase):

    def test_movement(self):
        spacecraft = Spacecraft([0, 0, 0], "N")
        
        spacecraft.move_forward()
        self.assertEqual(spacecraft.position, [0, 1, 0])
        
        spacecraft.move_backward()
        self.assertEqual(spacecraft.position, [0, 0, 0])

    def test_rotation(self):
        spacecraft = Spacecraft([0, 0, 0], "N")
        
        spacecraft.turn_left()
        self.assertEqual(spacecraft.main_direction, "W")
        
        spacecraft.turn_right()
        self.assertEqual(spacecraft.main_direction, "N")

    def test_rotation_vertical(self):
        spacecraft = Spacecraft([0, 0, 0], "N")
        
        spacecraft.rotate_up()
        self.assertEqual(spacecraft.main_direction, "Up")
        
        spacecraft.rotate_down()
        self.assertEqual(spacecraft.main_direction, "Down")

    def test_execute_commands(self):
        initial_position = [0, 0, 0]
        print("\nFor Unit Testing")
        initial_direction = input("Enter initial direction (N/S/E/W): ")
        commands = input("Enter commands (f/r/u/b/l without spaces): ")
        final_position, final_direction = execute_commands(commands, initial_position, initial_direction)
        self.assertEqual(final_position, [0, 1, -1])
        self.assertEqual(final_direction, "N")

if __name__ == '__main__':
    unittest.main()

