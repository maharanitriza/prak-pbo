import tkinter as tk
import random
from tkinter import messagebox

def angka_acak():
    return random.randint(1, 20)

def check_alphabet(string):
    for char in string:
        if char.isalpha():
            return True
    return False

def tebak_angka():
    try:
        check = guess_entry.get()
        if not check:
            raise ValueError("Masukkan tebakan dahulu")
        else:
            abjad = check_alphabet(check)
            if abjad:
                raise ValueError("Hanya dapat masukkan bilangan!")
            else:
                if int(guess_entry.get()) == target_number:
                    result_label.config(text="Tebakan benar!")
                elif int(guess_entry.get()) < target_number:
                    result_label.config(text="Tebakan anda lebih rendah!")
                else:
                    result_label.config(text="Tebakan anda lebih tinggi!")
    except ValueError as err:
        messagebox.showerror("Error",str(err))

def reset_game():
    global target_number
    target_number = angka_acak()
    result_label.config(text="")
    guess_entry.delete(0, tk.END)

target_number = angka_acak()

root = tk.Tk()
root.title("GAME TEBAK ANGKA")
root.geometry("400x280")

title_label = tk.Label(root, text="TEBAK ANGKA", font=("Verdana", 16, "bold"))
title_label.pack(pady=20)

guess_label = tk.Label(root, text="Masukkan Tebakan:", font=("Verdana", 10, "bold"))
guess_label.pack()

guess_entry = tk.Entry(root, font=("Verdana", 14))
guess_entry.pack(pady=5)

buttonframe1 = tk.Frame(root)
buttonframe2 = tk.Frame(root)

check_button = tk.Button(buttonframe1, text="CEK", font=("Verdana", 10, "bold"), bg="silver", command=tebak_angka)
check_button.grid(row=1, column=0)
buttonframe1.pack(pady=10)

result_label = tk.Label(root, text="", font=("Verdana", 12, "bold"))
result_label.pack(pady=10)

reset_button = tk.Button(buttonframe2, text="ULANG GAME", font=("Verdana", 10, "bold"), bg="silver", command=reset_game)
reset_button.grid(row=3, column=0)
buttonframe2.pack(pady=10)


root.mainloop()
