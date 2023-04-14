import tkinter as tk
import chordGen

# basic settings
root = tk.Tk()
root.title("Random Chord Generator")
root.geometry("250x150")


def run_program():
    return chordGen.random_simple_chord()


label_text = run_program()

# creating a button
button = tk.Button(root, text="Run", command=run_program())
button.pack()

# creating a chord label
output_label = tk.Label(root, text=f'{label_text}')
output_label.pack()
