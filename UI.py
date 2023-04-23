import tkinter as tk
import chordGen

# Basic settings
root = tk.Tk()
root.title("Random Chord Generator")
root.geometry("450x185")

# label to present the chord
output_label = tk.Label(root, text="", font='Arial 75')
output_label.pack()

# 'Use Seventh' checkbox
seventh_checker = tk.IntVar()
seventh_checkbox = tk.Checkbutton(root, text='Use Seventh Chords', variable=seventh_checker)
seventh_checkbox.pack(anchor='sw', padx=5)

# 'Simplify' checkbox
simplify_checker = tk.IntVar()
simplify_checkbox = tk.Checkbutton(root, text='Simplify Chords', variable=simplify_checker)
simplify_checkbox.pack(anchor='sw', padx=5)


def run_program():
    label_text = chordGen.build_chord(simplify_checker.get(), seventh_checker.get())
    output_label.config(text=label_text)


# creating a 'Run' button
button = tk.Button(root, text="Run", font='Helvetica 20', command=run_program)
button.pack(pady=5)
