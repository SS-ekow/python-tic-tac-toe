import tkinter as tk
from tkinter import messagebox, simpledialog

def button_click():
    print("I was clicked!")
    

    

my_window = tk.Tk()  # Creating a window.
my_entry = tk.Entry()

def submit():
    print(my_entry.get())
    
my_label = tk.Label( text="Tic-Tac-Toe game",
                    background='black',
                    foreground='yellow',
                    font=('Papyrus', 25))  # Creating a label.

# messagebox.showinfo("Information","Welcome to Tic-Tac-Toe game")
# messagebox.showwarning("Warning","You are about to play Tic-Tac-Toe game")
# messagebox.showerror("Error","You have made a mistake")

# likes_game = messagebox.askyesno("Question","Do you like Tic-Tac-Toe game?")

# if likes_game == True:
#     messagebox.showinfo("Information","Great! Let's play!")
    
# else:
#     print("That's too bad!")

# retry = messagebox.askretrycancel("Question","Do you want to try again?")

# if retry:
#     print("Let's try again!")

name = simpledialog.askstring("Input","What is your name?")
age = simpledialog.askinteger("Input","What is your age?")
weight = simpledialog.askfloat("Input","What is your weight?")

my_label.pack()  # Packing the label into the window.
 
my_button = tk.Button(text="submit", command=submit,
                      background='yellow',
                      foreground='blue')  # Creating a button.
my_entry.pack()
my_button.pack()  # Packing the button into the window.

my_window.mainloop()  