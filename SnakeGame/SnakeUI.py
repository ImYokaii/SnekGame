from SnekGame import SnakeGame
import tkinter as tk
from tkinter import *
import os

class SnakeUi:

    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg="#2596be")
        self.root.geometry("500x300")
        self.root.resizable(False,False)
        self.root.title("Isnek")
        #font=('Tahoma', 12) bg="#2596be", fg="white"
        self.label = tk.Label(self.root, text=" Welcome to Isnek " ,font=('Comic Sans MS', 12),background = "blue", foreground = "orange")
        self.label.place(x= 180,y=15)

        self.label = tk.Label(self.root, text=" Controls: Arrow Keys to Move Isnek ")
        self.label.place(x= 150,y=50)

        self.label = tk.Label(self.root, text=" Please Select your Desired Difficulty ")
        self.label.place(x= 150,y=80)

        self.label = tk.Label(self.root, text=" No Walls ")
        self.label.place(x= 220, y = 110)
        self.button = tk.Button(self.root, text="Easy", command=self.NoWallsEasy)
        self.button.place(x= 150, y=135)
        self.button = tk.Button(self.root, text="Normal", command=self.NoWallsMedium)
        self.button.place(x= 225, y=135)
        self.button = tk.Button(self.root, text="Hard", command=self.NoWallsHard)
        self.button.place(x= 315, y=135)

        self.label = tk.Label(self.root, text=" With Walls ")
        self.label.place(x= 215, y = 210)
        self.button = tk.Button(self.root, text="Easy", command=self.WalledEasy)
        self.button.place(x= 150, y=235)
        self.button = tk.Button(self.root, text="Normal", command=self.WalledNormal)
        self.button.place(x= 225, y=235)
        self.button = tk.Button(self.root, text="Hard", command=self.WalledHard)
        self.button.place(x= 315, y=235)


        self.root.mainloop()

    def NoWallsEasy(self):
        if(__name__ == "__main__"):
            snake=SnakeGame()
            snake.setplayers([])
            snake.start(10) #Level of Speed

    def NoWallsMedium(self):
        if(__name__ == "__main__"):
            snake=SnakeGame()
            snake.setplayers([])
            snake.start(15) #Level of Speed
    def NoWallsHard(self):
        if(__name__ == "__main__"):
            snake=SnakeGame()
            snake.setplayers([])
            snake.start(20) #Level of Speed
    def WalledEasy(self):
        if(__name__ == "__main__"):
            snake=SnakeGame()
            snake.SetObstacles(5) #level of obstacles 
            snake.setplayers([])
            snake.start(10) #Level of Speed
    def WalledNormal(self):
        if(__name__ == "__main__"):
            snake=SnakeGame()
            snake.SetObstacles(7) #level of obstacles 
            snake.setplayers([])
            snake.start(15) #Level of Speed
    def WalledHard(self):
        if(__name__ == "__main__"):
            snake=SnakeGame()
            snake.SetObstacles(12) #level of obstacles 
            snake.setplayers([])
            snake.start(20) #Level of Speed


SnakeUi()
