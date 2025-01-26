![image](https://github.com/user-attachments/assets/ed8b3891-c1a6-41ac-91e2-bf1c1609cd05)# README

## Scribble game

### Introduction

This repository contains a Python-based two-player drawing and guessing game, utilizing socket programming for real-time communication between a server and client.

### Game Play:
- Player 1 (the drawer) will receive a random word to draw.
- Player 2 (the guesser) will guess the word based on the drawing.
- Upon a correct guess, both players will see a victory window.
![guesser](https://github.com/user-attachments/assets/1bef2b9a-01d0-4f81-89a1-a2891a8da85c)
![player](https://github.com/user-attachments/assets/05111427-600f-4861-9fa2-6732ca53b171)

### Technical Details

- Programming Language: Python
- Libraries Used:
  - socket: For implementing the client-server communication.
  - pygame: For creating the graphical user interface.
  - random: For choosing random word.
  
- Game Logic: Painter client sends drawing coordinates, guesser sends words, while server ensure communication between both clients. Painter client checks guesses of second player and if guessed word is correct sends signal to guesser about end of the game.
