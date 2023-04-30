import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("Frames and parenting")

# frame
frame1 = ttk.Frame(window, width=200, height=200, borderwidth=10, relief=tk.GROOVE)
# size of frame set by child, to make it not
frame1.pack_propagate(False)
frame1.pack(side="left")

# master setting
label1 = ttk.Label(frame1, text="Label in frame")
label1.pack()

button = ttk.Button(frame1, text="Button in frame")
button.pack()

label2 = ttk.Label(window, text="Label in Frame2")
label2.pack(side="left")

# exercise
exercise_frame = ttk.Frame(window)
ttk.Label(exercise_frame, text="exercise label").pack()
ttk.Button(exercise_frame, text="button ").pack()
ttk.Entry(exercise_frame).pack()
exercise_frame.pack(side="left")

window.mainloop()
