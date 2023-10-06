import tkinter as tk
from tkinter import messagebox

# Create a 3x3 grid for the game
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize variables
current_player = "X"
winner = None

# Create a list to store the buttons
buttons = [[None, None, None], [None, None, None], [None, None, None]]

# Function to check for a win
def check_win():
    global winner
    for i in range(3):
        # Check rows
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            winner = buttons[i][0]["text"]
            change_color(i, 0, i, 1, i, 2)
            return True
        # Check columns
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            winner = buttons[0][i]["text"]
            change_color(0, i, 1, i, 2, i)
            return True
    # Check diagonals
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        winner = buttons[0][0]["text"]
        change_color(0, 0, 1, 1, 2, 2)
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        winner = buttons[0][2]["text"]
        change_color(0, 2, 1, 1, 2, 0)
        return True
    return False

# Function to change the color of winning buttons
def change_color(x1, y1, x2, y2, x3, y3):
    buttons[x1][y1].config(bg="green")
    buttons[x2][y2].config(bg="green")
    buttons[x3][y3].config(bg="green")

# Function to handle button clicks
def button_click(x, y):
    global current_player
    if buttons[x][y]["text"] == "" and winner is None:
        buttons[x][y]["text"] = current_player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
        if check_win():
            messagebox.showinfo("Winner", f"Player {winner} wins!")
        elif all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
            messagebox.showinfo("Draw", "It's a draw!")
        else:
            return

# Create and configure buttons
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", width=10, height=2, command=lambda x=i, y=j: button_click(x, y))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()
