from tkinter import Button, Label
from tkinter import font
import settings
import random
import ctypes
import sys


class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_obj = None
        self.is_mine_candidate = False
        self.x = x
        self.y = y
        self.is_revealed = False

        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            master=location,
            width=6,
            height=2,
            font=font.Font(weight="bold"),
        )
        btn.bind("<Button-1>", self.left_click_action)
        btn.bind("<Button-3>", self.right_click_action)
        self.cell_btn_obj = btn

    def left_click_action(self, event):
        if self.is_mine_candidate:
            return
        if self.is_mine:
            self.show_mine()
            print("oopsie")
        else:
            self.show_cell()

        # cancle left and right clikc events if cell is already opened
        self.cell_btn_obj.unbind("<Button-1>")
        self.cell_btn_obj.unbind("<Button-3>")

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    # use get_cell_by_axis and filter that
    # can filter with filter func or list comprehension
    def get_bomb_count(self):
        bomb_count = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                newx = self.x + x
                newy = self.y + y
                if newx < 0 or newx >= settings.GRID_SIZE:
                    continue
                if newy < 0 or newy >= settings.GRID_SIZE:
                    continue
                if self.get_cell_by_axis(x=newx, y=newy).is_mine:
                    bomb_count += 1
        return bomb_count

    def show_cell(self):
        if self.is_revealed:
            return
        Cell.cell_count -= 1
        bomb_count = self.get_bomb_count()
        # change the cell count label
        if Cell.cell_count_label_object:
            Cell.cell_count_label_object.configure(text=f"Cells left:{Cell.cell_count}")

        self.cell_btn_obj.configure(text=bomb_count)
        # handle for 0 bomb cell
        if bomb_count == 0 and not self.is_revealed:
            self.is_revealed = True
            nbour = []
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    newx = self.x + x
                    newy = self.y + y
                    nbour.append(self.get_cell_by_axis(newx, newy))
            nbour = [n for n in nbour if n is not None]
            for cell in nbour:
                cell.show_cell()

        # win condition
        if Cell.cell_count == settings.MINES_COUNT:
            ctypes.windll.user32.MessageBoxW(
                0, "Congralutation, you win", "game over", 0
            )

        # mark the cell as opened
        self.is_revealed = True

    def show_mine(self):
        self.cell_btn_obj.configure(bg="red")
        ctypes.windll.user32.MessageBoxW(0, "you clicked a mine", "game over", 0)
        sys.exit()

    def right_click_action(self, event):
        if self.is_revealed:
            return
        if not self.is_mine_candidate:
            self.cell_btn_obj.configure(bg="orange")
            self.is_mine_candidate = True
        else:
            self.cell_btn_obj.configure(bg="SystemButtonFace")
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            text=f"Cells left:{Cell.cell_count}",
            width=12,
            height=4,
            bg="black",
            fg="white",
            font=("", 15),
        )
        Cell.cell_count_label_object = lbl

    def __repr__(self):
        return f"Cell({self.x},{self.y})"
