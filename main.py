from random import randint
from tkinter import Canvas, Tk

GAME_HEIGHT = 500
GAME_WIDTH = 500
GRID_SIZE = 20
BACKGROUND_COLOR = '#073b4c'
FOOD_COLOR='#ef476f'
BODY_PARTS = 3
SNAKE_COLOR = '#06d6a0'
REFRESH_IN_MS = 150

direction = 'down'


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


def check_collisions(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():
    pass


def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == 'up':
        y -= GRID_SIZE
    elif direction == 'down':
        y += GRID_SIZE
    elif direction == 'left':
        x -= GRID_SIZE
    elif direction == 'right':
        x += GRID_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=SNAKE_COLOR, width=0)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        canvas.delete('food')
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(REFRESH_IN_MS, next_turn, snake, food)


def change_direction(new_direction):
    global direction

    if  new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction


window = Tk()
window.title('Snake')
window.resizable(False, False)

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

food = Food()
snake = Snake()

next_turn(snake, food)

if __name__ == '__main__':
    window.mainloop()
