import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()
window.title("Slider")
window.geometry("600x400")

# tkinter has slider and progress bar
# slider
scale_float = tk.DoubleVar(value=15)
scale = ttk.Scale(
    window,
    command=lambda value: progress.stop(),
    from_=0,
    to=25,
    length=300,
    orient="horizontal",
    variable=scale_float,
)
scale.pack()

# progress bar
progress = ttk.Progressbar(
    window,
    variable=scale_float,
    maximum=25,
    orient="horizontal",
    mode="indeterminate",
    length=400,
)
progress.pack()

# be careful
progress.start()

# scrolled text
# text widget with slider
scrolled_text = scrolledtext.ScrolledText(window, width=100, height=5)
scrolled_text.pack()

# exercise
exercise_int = tk.IntVar()
exercise_progress = ttk.Progressbar(window, variable=exercise_int)
exercise_progress.pack()
exercise_slider = ttk.Scale(window, variable=exercise_int, from_=0, to=100)
exercise_slider.pack()
label = ttk.Label(window, textvariable=exercise_int)
label.pack()
exercise_progress.start()

window.mainloop()
