from tkinter import Button
from tkinter import font
import settings
import random


class Cell:
    all = []

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_obj = None
        self.x = x
        self.y = y

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
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

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
        bomb_count = self.get_bomb_count()
        self.cell_btn_obj.configure(text=bomb_count)

    def show_mine(self):
        self.cell_btn_obj.configure(bg="red")

    def right_click_action(self, event):
        print("right click")

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"
