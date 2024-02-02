#Library
#@GaelHF
import turtle
import pyautogui
from boxes import boxes

#Variables
t = turtle.Turtle(shape="classic")
screen = turtle.Screen()
screen.bgcolor('gray')
screen.setup(350, 350)
screen.title("Tic-Tac-Toe")
t.pencolor('white')
t.speed(-1)
TURNS = 1
X_COLOR="RED"
O_COLOR="BLUE"

#Functions
def goto_with_out_draw(tu, cx, cy):
    tu.penup()
    tu.goto(cx, cy)
    tu.pendown()

def draw_board():
    LENGHT = 100
    HEIGHT = -150
    goto_with_out_draw(tu=t, cx=-150, cy=HEIGHT)

    for i in range(3):
        for i in range(3):
            for i in range(4):
                t.forward(LENGHT)
                t.left(90)
            t.forward(LENGHT)
        HEIGHT += LENGHT
        goto_with_out_draw(tu=t, cx=-150, cy=HEIGHT)

def draw_x():
    t.width(10)
    t.pencolor(X_COLOR)
    t.left(45)
    t.forward(50)
    t.backward(100)
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.backward(100)
    t.forward(100)
    t.width(1)
    t.pencolor("white")

def draw_o():
    t.width(10)
    t.pencolor(O_COLOR)
    t.circle(50)
    t.width(1)
    t.pencolor("white")

def on_click(x, y):
    print(f"You clicked {x}, {y}")
    draw_o()

draw_board()

#Events
screen.onclick(on_click)

input()
