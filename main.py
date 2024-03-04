from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import colorchooser
from turtle import *
from math import sqrt, atan, degrees

#functions
def showvalueerror():
    messagebox.showerror('Error', 'Faqat sonli qiymatlar kiriting')

def hover(btn):
    btn['bg'] = 'aqua'

def leave(btn):
    btn['bg'] = '#F0F0F0'

def taking_pen():
    pen.penup()

def putting_pen():
    pen.pendown()

def clear():
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.clear()

def pen_goto():
    try:
        x = int(entry_x.get())
        y = int(entry_y.get())
        size = int(pen_size.get())
        pen.width(size)
        pen.goto(x, y)
    except ValueError:
        showvalueerror()

def shapes(shape):
    match shape:
        case 'Rectangle':
            rectangle_frame.place(x=root_width * 0.745, y=10)
            triangle_frame.place_forget()
            circle_frame.place_forget()
        case 'Triangle':
            triangle_frame.place(x=root_width * 0.745, y=10)
            rectangle_frame.place_forget()
            circle_frame.place_forget()
        case 'Circle':
            circle_frame.place(x=root_width * 0.745, y=10)
            triangle_frame.place_forget()
            rectangle_frame.place_forget()

def draw(shape):
    match shape:
        case 1:
            try:
                width = int(rectangle_width.get())
                height = int(rectangle_height.get())
                for _ in range(2):
                    pen.forward(width)
                    pen.right(90)
                    pen.forward(height)
                    pen.right(90)
            except ValueError:
                showvalueerror()
        case 2:
            try:
                width = int(triangle_width.get())
                height = int(triangle_height.get())
                side = sqrt(pow(width/2, 2) + pow(height, 2))
                degree = degrees(atan(height/(width/2)))
                pen.forward(width)
                pen.left(180-degree)
                pen.forward(side)
                pen.left(180-(180-2*degree))
                pen.forward(side)
                pen.left(180-degree)
            except ValueError:
                showvalueerror()
        case 3:
            try:
                radius = int(circle_radius.get())
                pen.circle(radius)
            except ValueError:
                showvalueerror()

def colorchoose():
    color = colorchooser.askcolor(title='Choose color')
    if color[1]:
        pen.color(color[1])

#creating window
root_width = 1000
root_height = 670
root = Tk()
root.title('Paint 1.0')
root.iconbitmap('images/logo.ico')
root.geometry(f'{root_width}x{root_height}+200+60')
root.resizable(False, False)

#main program
canvas_width = root_width
canvas_height = root_height - 70
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.place(x=root_width-canvas_width, y=root_height-canvas_height)

turtleScreen = TurtleScreen(canvas)
pen = RawTurtle(turtleScreen)

#drawing coordinate axises
coordinate_pen = RawTurtle(turtleScreen)
coordinate_pen.hideturtle()
coordinate_pen.speed(0)
coordinate_pen.write('(0, 0)')
coordinate_pen.goto(x=0, y=canvas_height//2-12)
coordinate_pen.write(f'(0, {canvas_height//2})')
coordinate_pen.goto(x=0, y=-(canvas_height//2))
coordinate_pen.write(f'(0, -{canvas_height//2})')
coordinate_pen.goto(x=0, y=0)
coordinate_pen.goto(x=-(canvas_width//2), y=0)
coordinate_pen.write(f'({-(canvas_width//2)}, 0)')
coordinate_pen.goto(x=canvas_width//2-40, y=0)
coordinate_pen.write(f'({canvas_width//2}, 0)')

#widgets
#pen_up and pen_down
pen_btns_size = (root_width//20, root_height//12)
pen_up_image = PhotoImage(file='images/pen_up.gif')
btn_pen_up = Button(width=pen_btns_size[0], height=pen_btns_size[1], image=pen_up_image, command=taking_pen, relief='flat')
btn_pen_up.place(x=10, y=10)
btn_pen_up.bind('<Enter>', lambda event: hover(btn_pen_up))
btn_pen_up.bind('<Leave>', lambda event: leave(btn_pen_up))

pen_down_image = PhotoImage(file='images/pen_down.gif')
btn_pen_down = Button(width=pen_btns_size[0], height=pen_btns_size[1], image=pen_down_image, command=putting_pen, relief='flat')
btn_pen_down.place(x=10 + pen_btns_size[0] + 10, y=10)
btn_pen_down.bind('<Enter>', lambda event: hover(btn_pen_down))
btn_pen_down.bind('<Leave>', lambda event: leave(btn_pen_down))

#goto
font_size = root_height//24
goto_label = Label(text='Go to(x, y):', font=('Verdana', font_size))
goto_label.place(x=root_width*0.13, y=10)

entry_x = Entry(font=('Verdana', font_size), width=3)
entry_x.insert(END, '0')
entry_x.place(x=root_width*0.35, y=12)

entry_y = Entry(font=('Verdana', font_size), width=3)
entry_y.insert(END, '0')
entry_y.place(x=root_width*0.43, y=12)

ok_image = PhotoImage(file='images/ok_button.gif')
btn_ok = Button(width=pen_btns_size[0]-5, height=pen_btns_size[1]-6, image=ok_image, relief='flat', command=pen_goto)
btn_ok.place(x=root_width*0.51, y=7)

#pen size
pen_size = Spinbox(from_=1, to=10, font=('Verdana', font_size), width=2)
pen_size.place(x=root_width*0.57, y=10)

#shapes
shape_options = ['Rectangle', 'Triangle', 'Circle']
selected_shape = StringVar()
selected_shape.set('Shape')

shape_option_menu = OptionMenu(root, selected_shape, *shape_options, command=lambda shape: shapes(shape))
shape_option_menu.place(x=root_width*0.65, y=20)

#rectangle
rectangle_frame = Frame()

label_rectangle_width = Label(rectangle_frame, text='width:')
label_rectangle_width.grid(row=0, column=1)
rectangle_width = ttk.Entry(rectangle_frame, width=6)
rectangle_width.grid(row=0, column=2)

label_rectangle_height = Label(rectangle_frame, text='height:')
label_rectangle_height.grid(row=1, column=1)
rectangle_height = ttk.Entry(rectangle_frame, width=6)
rectangle_height.grid(row=1, column=2)

btn_rectangle_ok = Button(rectangle_frame, width=pen_btns_size[0]-5, height=pen_btns_size[1]-6, image=ok_image, relief='flat', command=lambda: draw(1))
btn_rectangle_ok.grid(row=0, column=3, rowspan=2)

#triangle
triangle_frame = Frame()

label_triangle_width = Label(triangle_frame, text='width:')
label_triangle_width.grid(row=0, column=1)
triangle_width = ttk.Entry(triangle_frame, width=6)
triangle_width.grid(row=0, column=2)

label_triangle_height = Label(triangle_frame, text='height:')
label_triangle_height.grid(row=1, column=1)
triangle_height = ttk.Entry(triangle_frame, width=6)
triangle_height.grid(row=1, column=2)

btn_triangle_ok = Button(triangle_frame, width=pen_btns_size[0]-5, height=pen_btns_size[1]-6, image=ok_image, relief='flat', command=lambda: draw(2))
btn_triangle_ok.grid(row=0, column=3, rowspan=2)

#circle
circle_frame = Frame()

label_circle_radius = Label(circle_frame, text='radius:')
label_circle_radius.grid(row=0, column=1, rowspan=2)
circle_radius = ttk.Entry(circle_frame, width=6)
circle_radius.grid(row=0, column=2, rowspan=2)

btn_circle_ok = Button(circle_frame, width=pen_btns_size[0]-5, height=pen_btns_size[1]-6, image=ok_image, relief='flat', command=lambda: draw(3))
btn_circle_ok.grid(row=0, column=3, rowspan=2)

#clear button
clear_image = PhotoImage(file='images/rubbish.gif')
btn_clear = Button(image=clear_image, width=pen_btns_size[0], height=pen_btns_size[1], relief='flat', command=clear)
btn_clear.place(x=root_width-pen_btns_size[0]-10, y=10)

#changing color
color_chooser_image = PhotoImage(file='images/color_chooser.gif')
btn_color_chooser = Button(image=color_chooser_image, width=pen_btns_size[0], height=pen_btns_size[1], relief='flat', command=colorchoose)
btn_color_chooser.place(x=root_width-pen_btns_size[0]-65, y=10)

root.mainloop()
