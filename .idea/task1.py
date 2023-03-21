from tkinter import *
from tkfontchooser import askfont
from tkinter import colorchooser
from tkinter import messagebox

fon = ('Times', 14)
color = 'green'
size1 = "30"
def triangle():
    canvas.coords(r, (0, 0, 0, 0))
    canvas.coords(c, (0, 0, 0, 0))
    canvas.itemconfig(t, fill=color, outline='white',width=size1)
    canvas.coords(t, (50, 200, 340, 200, 110, 60))
    text.delete(1.0, END)
    text.insert(1.0, 'Зображення трикутника')
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=fon, foreground='blue')

def rectangle():
    canvas.coords(t, (0, 0, 0, 0, 0, 0))
    canvas.coords(c, (0, 0, 0, 0))
    canvas.itemconfig(r, fill='blue', outline='white')
    canvas.coords(r, (80, 50, 320, 200))
    text.delete(1.0, END)
    text.insert(1.0, 'Зображення прямокутника')
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=fonr, foreground='black')


def oval():
    canvas.coords(r, (0, 0, 0, 0))
    canvas.coords(t, (0, 0, 0, 0, 0, 0))
    canvas.itemconfig(c, fill = 'red', outline = 'black')
    canvas.coords(c, (300, 40, 100, 240))
    text.delete(1.0, END)
    text.insert(1.0, 'Зображення кола')
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=fonr, foreground='black')

def cleaning():
    canvas.coords(r, (0, 0, 0, 0))
    canvas.coords(t, (0, 0, 0, 0, 0, 0))
    canvas.coords(c, (0, 0, 0, 0))
    text.delete(1.0, END)
    text.insert(1.0, 'Очищення полотна')
    text.tag_add('title', '1.0', '1.end')
    text.tag_config('title', font=fonr, foreground='black')

def Color():
    (rgb, hg) = colorchooser.askcolor()
    global color
    color = hg

#def Size():giD:\prog\LB7\.idea\task1.py


def Font():
    font = askfont(win)
    if font:
        font['family'] = font['family'].replace(' ', '\ ')
        font_str = "%(family)s %(size)i %(weight)s %(slant)s" % font
        if font['underline']:
            font_str += ' underline'
        if font['overstrike']:
            font_str += ' overstrike'
        text.tag_add('title', '1.0', '1.end')
        text.tag_config('title', font=font_str)
        global fonr
        fonr = font_str


win = Tk()
main_menu = Menu()

file_menu = Menu(tearoff=0)

file_menu1 = Menu(tearoff=0)
file_menu1.add_command(label="Налаштуваня зображень", command=Color) #and Size)
file_menu1.add_command(label="Налаштування тексту", command=Font)
file_menu.add_cascade(label="Налаштування", menu=file_menu1)
file_menu.add_separator()
file_menu.add_command(label="Вийти", command = exit)

main_menu.add_cascade(label="Меню", menu=file_menu)

win.config(menu=main_menu)

b_triangle = Button(text = "Трикутник", width = 15, command = triangle)
b_rectangle = Button(text = "Прямокутник", width = 15, command = rectangle)
b_oval = Button(text = "Коло", width=15, command = oval)
b_cleaning = Button(text = "Очищення полотна", width=15, command = cleaning)

canvas = Canvas(width=400, height=300, bg='#fff')
text = Text(width=55, height=5, bg='#fff', wrap=WORD)

t = canvas.create_polygon(0, 0, 0, 0, 0, 0)
r = canvas.create_rectangle(0, 0, 0, 0)
c = canvas.create_oval(0, 0, 0, 0)


b_triangle.grid(row=0, column=0)
b_rectangle.grid(row=1, column=0)
b_oval.grid(row=2, column=0)
b_cleaning.grid(row=3, column=0)


canvas.grid(row=0, column=1, rowspan=10)
text.grid(row=11, column=1, rowspan=3)
win.mainloop()

b_triangle.grid(row=0, column=0)
b_rectangle.grid(row=1, column=0)
b_oval.grid(row=2, column=0)
b_cleaning.grid(row=3, column=0)


canvas.grid(row=0, column=1, rowspan=10)
text.grid(row=11, column=1, rowspan=3)
win.mainloop()


