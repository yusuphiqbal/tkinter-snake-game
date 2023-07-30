from tkinter import Canvas, Tk

GAME_HEIGHT = 500
GAME_WIDTH = 500
BACKGROUND_COLOR = '#073b4c'

window = Tk()
window.title('Snake')
window.resizable(False, False)

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

if __name__ == '__main__':
    window.mainloop()
