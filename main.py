import tkinter as tk
import random


window = tk.Tk()
window.title("Tic-Tac-Toe")

def button_pressed(row, col):
    global count
    if played_list[row][col] == "X" or played_list[row][col] == "O":
        return
    buttons[row][col]["text"] = "X"
    played_list[row][col] = "X"
    if check_winner("X"):
        print(f"X wins!")
        window.destroy()
        return
    count += 1
    if count < 9:
        still_space = True
    else:
        still_space = False
        print("Draw")
        window.destroy
        return
    x = random.randint(0,2)
    y = random.randint(0,2)
    while played_list[x][y] == "X" or played_list[x][y] == "O" and still_space == True:
        x = random.randint(0,2)
        y = random.randint(0,2)
    buttons[x][y]["text"] = "O"
    played_list[x][y] = "O"
    if check_winner("X"):
        print(f"X wins!")
        window.destroy()
        return
    count += 1
    if count < 9:
        still_space = True
    else:
        still_space = False
        print("Draw")
        window.destroy
        return

def check_winner(player):
    # Check rows
    for row in range(3):
        if all(played_list[row][col] == player for col in range(3)):
            return True

    # Check columns
    for col in range(3):
        if all(played_list[row][col] == player for row in range(3)):
            return True

    # Check main diagonal
    if all(played_list[i][i] == player for i in range(3)):
        return True

    # Check other diagonal
    if all(played_list[i][2 - i] == player for i in range(3)):
        return True

    return False
    

buttons = []
played_list: list[str] = []
still_space: bool = True
count: int = 0

for row in range(3):
    button_row = []
    played_list_row: list[str] = []

    for col in range(3):
        button = tk.Button(
            window,
            width=10,
            height=5,
            command=lambda r=row, c=col: button_pressed(r, c)
        )

        button.grid(row=row, column=col)
        button_row.append(button)
        played_list_row.append("")

    buttons.append(button_row)
    played_list.append(played_list_row)
window.mainloop()