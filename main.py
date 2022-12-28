import tkinter
from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title('С новым годом!')
root.resizable(width=False, height=False)
postcardWidth = 900
postcardHeight = 500
root.resizable(0,0)
postcard = Canvas(root, width=postcardWidth, height=postcardHeight, bg='#4682B4')
postcard.pack()

canvas = tkinter.Canvas(root, height=400, width=700)
image = Image.open('../postcard/elka1.png')

elka = ImageTk.PhotoImage(image)
postcard.create_image(400, 30, anchor=NW, image=elka)


def create_text():
    text = 'Ох, пусть 2023 будет лучше,\nчем 2022!\n' \
           '\n' \
           'Поздравляшки!'
    postcard.create_text(postcardWidth * 1.5 / 5, postcardHeight * 2 / 5, text=text, fill='white', font='Times 24 bold')


def create_snow(t, n):
    for i in range(500):
        x = random.randint(1, postcardWidth)
        y = random.randint(-postcardHeight * n - 8, postcardHeight * (1 - n))
        w = random.randint(3, 8)
        postcard.create_oval(x, y, x + w, y + w, fill='white', tag=t)


def motion():
    global indicator, indicator_count
    postcard.move('tageOne', 0, 1)
    postcard.move('tageTwo', 0, 1)
    postcard.move(indicator, 0, 1)
    if postcard.coords(indicator)[1] < postcardHeight + 1:
        root.after(20, motion)
    else:
        postcard.move(indicator, 0, -postcardHeight - 5)
        root.after(20, motion)
        if indicator_count == 0:
            postcard.delete('tageOne')
            create_snow('tageOne', 1)
            indicator_count = 1
        else:
            postcard.delete('tageTwo')
            create_snow('tageTwo', 1)
            indicator_count = 0


def main():
    global indicator, indicator_count
    indicator = postcard.create_oval(23, -5, 28, 0, fill='white')
    indicator_count = 0

    create_snow('tageOne', 0)
    create_snow('tageOne', 1)
    create_text()

    motion()


main()
root.mainloop()
