from SnakeLibrary import SnakeGame
import tkinter as tk
from tkinter import *


class SnakeUi:

    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg ="#eafe99")
        self.root.geometry("500x300")
        self.root.resizable(False,False)
        self.root.title("Isnek")
        uibg = PhotoImage(file = "UIBG.png")
        self.label = tk.Label(self.root, image = uibg)
        self.label.place(x= 0, y= 0)
        self.label = tk.Label(self.root, text=" WELCOME TO ISNEK " ,font=('Comic Sans MS', 18),background = "#135E46", foreground = "#F8F17F")
        self.label.place(x= 125,y=15)

        self.label = tk.Label(self.root, text=" Controls: Arrow Keys to Move Isnek ",font=('Arial Black', 12),background = "#478966", foreground = "#FFFFFF")
        self.label.place(x= 90,y=55)

        self.label = tk.Label(self.root, text=" Please Select your Desired Difficulty ", font=('Courier', 12),background = "#73A788", foreground = "#000000")
        self.label.place(x= 50,y=90)

        self.label = tk.Label(self.root, text=" No Walls ",font=('Verdana Bold', 12),background = "#592C15", foreground = "#EFDAA8")
        self.label.place(x= 200, y = 130)
        self.button = tk.Button(self.root, text="Easy", command=self.NoWallsEasy)
        self.button.place(x= 150, y=160)
        self.button = tk.Button(self.root, text="Normal", command=self.NoWallsMedium)
        self.button.place(x= 225, y=160)
        self.button = tk.Button(self.root, text="Hard", command=self.NoWallsHard)
        self.button.place(x= 315, y=160)

        self.label = tk.Label(self.root, text=" With Walls ",font=('Verdana Bold', 12),background = "#592C15", foreground = "#EFDAA8")
        self.label.place(x= 190, y = 220)
        self.button = tk.Button(self.root, text="Easy", command=self.WalledEasy)
        self.button.place(x= 150, y=250)
        self.button = tk.Button(self.root, text="Normal", command=self.WalledNormal)
        self.button.place(x= 225, y=250)
        self.button = tk.Button(self.root, text="Hard", command=self.WalledHard)
        self.button.place(x= 315, y=250)


        self.root.mainloop()

    def NoWallsEasy(self):
        if(__name__ == "__main__"):
            snake=SnakeGame()
            snake.setplayers([])
            snake.start(1) #Level of Speed

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
