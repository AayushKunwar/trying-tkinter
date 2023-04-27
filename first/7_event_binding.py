import tkinter as tk
from tkinter import ttk


def get_pos(event):
    # shows position of mouse
    print(f"x: {event.x} y:{event.y}")


window = tk.Tk()
window.title("Event binding")
window.geometry("500x500")

text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text="a button")
button.pack()

button.bind("<Alt-KeyPress-b>", lambda event: print(event))
# text.bind("<Motion>", get_pos)
# event
# bind method needs event and function
# event is <Modifier-type-detail

# window.bind("<Alt-KeyPress-a>", get_pos)
entry.bind("<FocusIn>", lambda event: print("Entry field was selected"))
# FocusOut also works

# window.bind("<KeyPress>", lambda event: print("a button was pressed"))

# checkout website
#  https://www.pythontutorial.net/tkinter/tkinter-event-binding/

text.bind("<Shift-MouseWheel>", lambda event: print("MouseWheel"))
window.mainloop()
