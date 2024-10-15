# README

## Project Title: Scribble game

### Introduction

This repository contains a Python-based multiplayer drawing and guessing game, utilizing socket programming for real-time communication between a server and clients. The game is designed for two players, where one player draws a randomly assigned word on a canvas while the other player attempts to guess the word based on the drawing. Upon a correct guess, a victory window is displayed for both players, and the game resets for another round.

### Features

- Server and Client Architecture: The application employs a client-server model using Python's socket library to facilitate communication between players over a network.
  
- Real-Time Interaction: The game operates in real-time, allowing seamless interaction between the drawing player and the guessing player.

- Random Word Assignment: The server randomly assigns a word to the drawing player.

- Victory Display: Upon a successful guess, both players receive a notification of victory, enhancing engagement and excitement.

- Game Reset: The game automatically resets after each round.


### Usage

1. Start the Server:
   Run the server script to initialize the server:
   
   python server.py
   
   

2. Start the Clients:
   Once the server is running, start two instances of the client script. Each player should connect to the server using the specified IP address.
   
   python client.py
   
   

3. Game Play:
   - Player 1 (the drawer) will receive a random word to draw.
   - Player 2 (the guesser) will guess the word based on the drawing.
   - Upon a correct guess, both players will see a victory window, and the game will restart automatically.

### Technical Details

- Programming Language: Python
- Libraries Used:
  - socket: For implementing the client-server communication.
  - PyQt5: For creating the graphical user interface.
  
- Game Logic: The server manages game state and word assignments while ensuring communication between both clients. Upon a draw and subsequent guess, the server handles the validation and informs both players accordingly.
