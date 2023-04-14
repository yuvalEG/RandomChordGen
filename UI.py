import tkinter as tk
import chordGen

# basic settings
root = tk.Tk()
root.title("Random Chord Generator")
root.geometry("450x150")


def run_program():
    label_text = chordGen.random_simple_chord()
    output_label.config(text=label_text)


# creating a button
button = tk.Button(root, text="Run", font= 'Helvetica 20', command=run_program)
button.pack(pady=5)

# creating a chord label
output_label = tk.Label(root, text="", font='Arial 75')
output_label.pack()
