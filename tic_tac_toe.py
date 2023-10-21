from glob import glob
from tkinter import *
import random


def next_turn(row, col):
    global player
    if game_btns[row][col]['text'] == "" and check_winner() == False:
        if player == players[0]:
            # Puting player 1 sympol
            game_btns[row][col]['text'] = player

            if check_winner() == False:
                # switching players
                player = players[1]
                label.config(text=(players[1] + " turn"))

            elif check_winner() == True:
                label.config(text=(players[0] + " wins^^"))

            elif check_winner() == 'tie':
                label.config(text=("No Winner^^!)"))

        elif player == players[1]:
            # Putting player 2 sympol
            game_btns[row][col]['text'] = player

            if check_winner() == False:
                # switching players
                player = players[0]
                label.config(text=(players[0] + " turn"))

            elif check_winner() == True:
                label.config(text=(players[1] + " wins^^"))

            elif check_winner() == 'tie':
                label.config(text=(" No Winner ^ ^!)"))


def check_winner():
    # test all three horizontals
    for row in range(3):
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] != "":
            game_btns[row][0].config(bg="pink")
            game_btns[row][1].config(bg="pink")
            game_btns[row][2].config(bg="pink")
            return True

    # test all three verticals 
    for col in range(3):
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] != "":
            game_btns[0][col].config(bg="pink")
            game_btns[1][col].config(bg="pink")
            game_btns[2][col].config(bg="pink")
            return True

    # test the diagonals 
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] != "":
        game_btns[0][0].config(bg="pink")
        game_btns[1][1].config(bg="pink")
        game_btns[2][2].config(bg="pink")
        return True
    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] != "":
        game_btns[0][2].config(bg="pink")
        game_btns[1][1].config(bg="pink")
        game_btns[2][0].config(bg="pink")
        return True

    # if there are no empty spaces left
    if check_empty_spaces() == False:
        for row in range(3):
            for col in range(3):
                game_btns[row][col].config(bg='yellow')

        return 'tie'

    else:
        return False


def check_empty_spaces():
    spaces = 9

    for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def start_new_game():
    global player
    player = random.choice(players)

    label.config(text=(player + " turn"))

    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text="", bg="#F0F0F0") #back to original color which is white


window = Tk()
window.title("Tic-Tac-Toe")

players = ["x", "o"]
player = random.choice(players)

game_btns = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

label = Label(text=(player + " turn"), font=('underline', 40))
label.pack(side="top")

restart_btn = Button(text="restart", font=(
    'underline', 20), command=start_new_game)
restart_btn.pack(side="top")

btns_frame = Frame(window)
btns_frame.pack()

for row in range(3):
    for col in range(3):
        game_btns[row][col] = Button(btns_frame, text="", font=('underline', 50), width=4, height=1,
                                     command=lambda row=row, col=col: next_turn(row, col))
        game_btns[row][col].grid(row=row, column=col)

window.mainloop()
