import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("More on the window")
# window.geometry("600x400")
# use + to put window position left and top
# window.geometry("600x400+900+100")

# exercise:
# start window at the middle of the screen
window_width = 600
window_height = 400
display_width = window.winfo_screenwidth()
display_height = window.winfo_screenheight()

window_x = int((display_width - window_width) / 2)
window_y = int((display_height - window_height) / 2)
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

# to change the icon
# needs .ico file
# window.iconbitmap("python.ico")

# window sizes
window.minsize(200, 100)
# below not so used
# window.maxsize(800, 700)
# window.resizable(True, False)

# screen attributes
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# window attributes
# 1 for full visibility, 0 for transparent
window.attributes("-alpha", 1)
# window.attributes("-topmost", True)

# security event
window.bind("<Escape>", lambda event: window.quit())
# is can be problamatic with some attribures
# dont use this (scary)
# window.attributes("-disable", True)
# window.attributes("-fullscreen", True)


# title bar
# hides title bar, useful for styling
window.overrideredirect(True)
grip = ttk.Sizegrip(window)
# window starts from top left 0.0 to 1.0
# anchor sets the point in the rectangle
grip.place(relx=1.0, rely=1.0, anchor="se")

window.mainloop()
