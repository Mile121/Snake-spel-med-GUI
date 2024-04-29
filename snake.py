from tkinter import *
import random


boardWidth = 30
boardHeight = 30
tilesize = 10

class Snake():

    def __init__(self):

        self.snakeX = [20, 20, 20]
        self.snakeY = [20, 21, 22]
        self.snakeLength = 3
        self.key = "w"
        self.points = 0

def move(self): 

        for i in range(self.snakeLength - 1, 0, -1):
                self.snakeX[i] = self.snakeX[i-1]
                self.snakeY[i] = self.snakeY[i-1]

        if self.key == "w":
            self.snakeY[0] = self.snakeY[0] - 1

        elif self.key == "s":
            self.snakeY[0] = self.snakeY[0] + 1

        elif self.key == "a":
            self.snakeX[0] = self.snakeX[0] - 1

        elif self.key == "d":
            self.snakeX[0] = self.snakeX[0] + 1

        self.eatApple()