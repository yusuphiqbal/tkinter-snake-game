from random import randint
from tkinter import Canvas, Tk

GAME_HEIGHT = 500
GAME_WIDTH = 500
GRID_SIZE = 20
BACKGROUND_COLOR = '#073b4c'
FOOD_COLOR='#ef476f'
BODY_PARTS = 3
SNAKE_COLOR = '#06d6a0'


class Food:
    def __init__(self):
        x = randint(0, (GAME_WIDTH / GRID_SIZE) - 1) * GRID_SIZE
        y = randint(0, (GAME_HEIGHT / GRID_SIZE) - 1) * GRID_SIZE
        self.coordinates = [x, y]
        canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=FOOD_COLOR, tags='food', width=0)


class Snake:
    def __init__(self):
        self.size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])
        
        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=SNAKE_COLOR, tags='snake', width=0, )
            self.squares.append(square)


window = Tk()
window.title('Snake')
window.resizable(False, False)

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

food = Food()
snake = Snake()

if __name__ == '__main__':
    window.mainloop()
