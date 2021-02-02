#RPS GAME

import tkinter as tk
from random import choice

root = tk.Tk()
root.title("Rock Paper Scissors Game")


game_options = ["rock","paper","scissor"]

your_score=0
computer_score=0

game_logic = {
  "rock":"scissor",
  "paper":"rock",
  "scissor":"paper"
}

def play_game(user1_choice,user2_choice):
  global your_score,computer_score
  if (game_logic[user1_choice] == user2_choice):
    your_score += 1
  elif (game_logic[user2_choice] == user1_choice):
    computer_score += 1

def getScore(user1_choice,user2_choice):
  global your_score,computer_score
  result = ""
  result += "Your choice: " + user1_choice
  result += "\nComputer's choice: " + user2_choice
  result += "\nYour score: " + str(your_score)
  result += "\nComputer's score: " + str(computer_score) + "\n\n"

  return result

def button_action(user1_choice,user2_choice):
  play_game(user1_choice,user2_choice)
  text_screen.insert(tk.END, getScore(user1_choice,user2_choice))

rock_button = tk.Button(
                        text = "R O C K",
                        bg = "#87C5DE",
                        fg = "#ff8c00",
                        width = 12,
                        height = 2,
                        command=lambda:button_action("rock",choice(game_options))
)
rock_button.pack()

paper_button = tk.Button(
                        text = "P A P E R",
                        bg = "#FACAEC",
                        fg = "#0d00ff",
                        width = 12,
                        height = 2,
                        command=lambda:button_action("paper",choice(game_options))
)
paper_button.pack()

scissor_button = tk.Button(
                        text = "S C I S S O R",
                        bg = "#9BF2A4",
                        fg = "#ff0000",
                        width = 12,
                        height = 2,
                        command=lambda:button_action("scissor",choice(game_options))
)
scissor_button.pack()

text_screen = tk.Text(
                      root,
                      width=35,
                      height=15,
                      bg="#F0F786"
)
text_screen.pack()

root.mainloop()
