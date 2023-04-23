import tkinter as tk

# from tkinter import ttk
import ttkbootstrap as ttk


# functionality
def convert():
    # this no good
    # print(entry.get())

    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)


# window
# this is the styling part
window = ttk.Window(themename="journal")
window.title("Demo")
window.geometry("300x150")

# title
title_label = ttk.Label(
    master=window, text="Miles to kilometers", font="Calibri 24 bold"
)
title_label.pack()

# input field
# these are the widgets
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="convert", command=convert)
# layouts
entry.pack(side="left", padx=10)
button.pack(side="left")
input_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window, text="Output", font="calibri 24", textvariable=output_string
)
output_label.pack(pady=5)

# run
window.mainloop()
