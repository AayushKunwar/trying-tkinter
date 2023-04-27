import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("combo and spin")

# Combobox
items = ("Ice cream", "Pizza", "Broccoli")
food_string = tk.StringVar(value=items[0])
combo = ttk.Combobox(window, textvariable=food_string)
combo["values"] = items
# same thing
# combo.config(values=items)
combo.pack()

# events
# special event for combo
combo.bind(
    "<<ComboboxSelected>>",
    lambda event: combo_label.config(text=f"selected value: {food_string.get()}"),
)

# label
combo_label = ttk.Label(window, text="a label")
combo_label.pack()

# SpinBox
spin_int = tk.IntVar()
spinbox = ttk.Spinbox(
    window,
    from_=3,
    to=20,
    increment=3,
    command=lambda: print(spin_int.get()),
    textvariable=spin_int,
)
# spinbox["value"] = (1,2,3,4,5)
# has two types of special events
spinbox.bind("<<Increment>>", lambda event: print("up"))
spinbox.bind("<<Decrement>>", lambda event: print("down"))
spinbox.pack()

# exercise
exer_text = tk.StringVar(value="A")
exer_spin = tk.Spinbox(window, textvariable=exer_text)
exer_spin["values"] = ("A", "B", "C", "D", "E")
exer_spin.pack()
exer_spin.bind("<<Increment>>", lambda event: print("what?"))

exercise_letters = ("A", "B", "C", "D", "E")
exercise_string = tk.StringVar(value=exercise_letters[0])
exercise_spin = tk.Spinbox(
    window, textvariable=exercise_string, values=exercise_letters
)
exercise_spin.pack()
exercise_spin.bind("<<Decrement>>", lambda event: print(exercise_string.get()))

window.mainloop()
