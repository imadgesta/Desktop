import turtle
import random                               # случайные числа
# код в императивном стиле(последовательное выполнение каждой строки)
window = turtle.Screen()
window.setup(1200 + 3, 800 + 3)
window.bgcolor("blue")
window.screensize(1200, 800)


def airplane(y):                                 # функция
    pen = turtle.Turtle()
    if y < 0:
        pen.color("red")
    else:
        pen.color("yellow")
    # pen.color("yellow")
    # pen.shape("turtle")                          # фигура черепашки
    # pen.shape("circle")                            # фигура круг
    for current_x in [-200, 0, 200]:  # for - для (цикл)
        pen.penup()                              # penup - движение без следа
        # pen.hideturtle()                         # hide - скрыть черепашку
        pen.setpos(x=current_x, y=y)
        pen.pendown()                             # оставляет след
        pen.circle(radius=random.randint(50, 200))
        pen.forward(100)
        # pen.circle(radius=100)


airplane(y=100)
airplane(y=-100)

window.mainloop()