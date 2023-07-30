from random import randint
from tkinter import Canvas, Tk

GAME_HEIGHT = 500
GAME_WIDTH = 500
GRID_SIZE = 20
BACKGROUND_COLOR = '#073b4c'
FOOD_COLOR='#ef476f'


class Food:
    def __init__(self):
        x = randint(0, (GAME_WIDTH / GRID_SIZE) - 1) * GRID_SIZE
        y = randint(0, (GAME_HEIGHT / GRID_SIZE) - 1) * GRID_SIZE
        self.coordinates = [x, y]
        canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=FOOD_COLOR, tags='food', width=0)


window = Tk()
window.title('Snake')
window.resizable(False, False)

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

food = Food()

if __name__ == '__main__':
    window.mainloop()
