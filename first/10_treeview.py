import tkinter as tk
from tkinter import ttk
from random import choice

window = tk.Tk()
window.geometry("600x400")
window.title("Treeview")

first_names = ["bob", "maria", "alex", "james"]
last_names = ["smith", "brown", "wilson", "thomson"]

table = ttk.Treeview(window, columns=("first", "last", "email"), show="headings")
table.heading("first", text="First name")
table.heading("last", text="Surname")
table.heading("email", text="Email")
table.pack(fill="both", expand=True)

# insert values into a table
# table.insert(parent="", index=0, values=("john", "doe", "jogndow@email.com"))

# add random values in table
for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f"{first[0]}{last}@email.com"
    data = (first, last, email)
    table.insert(parent="", index=0, values=data)

table.insert(parent="", index=2, values=("XXXXX", "YYYYYY", "ZZZZZ"))
# to add to end of table -> use index=tk.END


# events
def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)["values"])


table.bind("<<TreeviewSelect>>", item_select)
# each item has an id


def delete_items(_):
    print("delete")
    for i in table.selection():
        table.delete(i)


table.bind("<Delete>", delete_items)

# tables can get more complicated

window.mainloop()
