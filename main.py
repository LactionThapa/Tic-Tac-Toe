import tkinter as tk
import random


main_menu = tk.Tk()
main_menu.title("Main Menu")
count: int = 0

def open_game():
    main_menu.withdraw()
    game = tk.Toplevel(main_menu)

    game.title("Tic-Tac-Toe")
    game.resizable(False, False)
    
    buttons = []
    played_list: list[str] = []
    still_space: bool = True
    

    for row in range(3):
        button_row = []
        played_list_row: list[str] = []

        for col in range(3):
            button = tk.Button(
                game,
                width=10,
                height=5,
                command=lambda r=row, c=col: button_pressed(r, c))

            button.grid(row=row, column=col)
            button_row.append(button)
            played_list_row.append("")

        buttons.append(button_row)
        played_list.append(played_list_row)

    def button_pressed(row, col):

        player(row,col)
        if check_winner("X"):
            print(f"X wins!")
            reset()
            end_game("X")
            game.destroy()
            return
        
        if count < 9:
            still_space = True
        else:
            still_space = False
            print("Draw")
            reset()
            end_game("Draw")
            game.destroy()
            return

        computer()
        if check_winner("O"):
            print(f"O wins!")
            reset()
            end_game("O")
            game.destroy()
            return
        if count < 9:
            still_space = True
        else:
            still_space = False
            print("Draw")
            reset()
            end_game("Draw")
            game.destroy()
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

    def computer():
        global count
        x = random.randint(0,2)
        y = random.randint(0,2)
        while played_list[x][y] == "X" or played_list[x][y] == "O" and still_space == True:
            x = random.randint(0,2)
            y = random.randint(0,2)
        buttons[x][y]["text"] = "O"
        played_list[x][y] = "O"
        count += 1

    def player(row,col):
        global count
        if played_list[row][col] == "X" or played_list[row][col] == "O":
            return
        buttons[row][col]["text"] = "X"
        played_list[row][col] = "X"
        count += 1

    def reset():
        global count
        count = 0
        for i in range(3):
            for j in range(3):
                played_list[i][j] = ""

def end_game(player):
    end = tk.Toplevel(main_menu)
    end.title("Game Over")
    if player == "Draw":
        tk.Label(end, text="It'/s a draw").pack()
    else:
        tk.Label(end, text=f"{player} wins!").pack()

    def play_again():
        end.destroy()
        open_game()

    def quit():
        end.destroy()
        main_menu.destroy()

    tk.Button(end, text="Play Again!", command=play_again).pack()
    tk.Button(end, text="Quit", command=quit).pack()
tk.Label(main_menu, text="Welcome to Tic-Tac-Toe").pack()
tk.Button(main_menu, text="Start Game", command=open_game).pack()
tk.Button(main_menu, text="Quit", command=main_menu.destroy).pack()

main_menu.mainloop()