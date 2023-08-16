# Incubyte Chandrayaan 3 TDD Assessment
<h3>Name : Nilabhro Roy</h3>
<h3>Roll Number : 2005881</h3>

<h1>Problem Statement</h1>
Chandrayaan 3 Lunar Craft: Galactic Space Craft Control

<h2>Description</h2>
As a scientist at ISRO controlling the latest lunar spacecraft Chandrayaan 3, your task is to develop a program that translates commands sent from Earth into instructions understood by the spacecraft. The spacecraft navigates through the galaxy using galactic coordinates, represented by x, y, z coordinates (x for east or west location, y for north or south location, and z for distance above or below the galactic plane).

<h2>Requirements</h2>
You will be given the initial starting point (x, y, z) of the spacecraft and the direction it is facing (N, S, E, W, Up, Down). The spacecraft receives a character array of commands, and you are required to implement the following functionalities:
<ul>
  <li>Move the spacecraft forward/backward (f, b): The spacecraft moves one step forward or backward based on its current direction.</li>
  <li>Turn the spacecraft left/right (l, r): The spacecraft rotates 90 degrees to the left or right, changing its facing direction.</li>
  <li>Turn the spacecraft up/down (u, d): The spacecraft changes its angle, rotating upwards or downwards.</li>
</ul>

Note:
<ul>
  <li>The spacecraft’s initial direction (N, S, E, W, Up, Down) represents the reference frame for movement and rotation.</li>
  <li>The spacecraft cannot move or rotate diagonally; it can only move in the direction it is currently facing.</li>
  <li>Assume that the spacecraft’s movement and rotations are rigid, and it cannot move beyond the galactic boundaries.</li>
</ul>

<h2>Example</h2>
Given the starting point (0, 0, 0) following (x, y, z) and initial direction N, the following commands should result in the indicated final position and direction:

Commands: [“f”, “r”, “u”, “b”, “l”]

Starting Position: (0, 0, 0)

Initial Direction: N

<ul>
  <li>“f” - (0, 1, 0) - N</li>
  <li>“r” - (0, 1, 0) - E</li>
  <li>“u” - (0, 1, 0) - U</li>
  <li>“b” - (0, 1, -1) - U</li>
  <li>“l” - (0, 1, -1) - N</li>
</ul>

Final Position: (0, 1, -1)

Final Direction: N
