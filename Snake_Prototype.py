from os import system, name
import time
import keyboard

window_width = 34
gph = [" "]
result = []
top_bottom = "#"
sides = "#"
x_axis = [100000]
y_axis = [100000]
snake = "◘"
for xa in range(1, 35):
    x_axis.append(xa)
for ya in range(1, 1157, 34):
    y_axis.append(ya)
right_side = [x+33 for x in y_axis]

x = [16]
y = [16]


def clear():

    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')



def board():

    for spot in range(1, 1157):
        if len(gph) <= 34 or len(gph) >= 1123:  # draws top and bottom boarder lines
            gph.append(top_bottom)
        elif spot in y_axis:  # Draws the left side of the board
            gph.append(sides)
        elif spot in [x + 33 for x in y_axis]:  # Draw the right side of board
            gph.append(sides)
        else:
            gph.append(" ")


def display():

    position = (x_axis[x[0]] + y_axis[y[0]] - 1)
    gph[position] = snake
    for num in range(len(gph)):
        if num % window_width == 0:
            result.append(gph[num] + '\n')
        else:
            result.append(gph[num])
    print(*result)
    gph[position] = " "
    result.clear()


def on_press():
    
#   o = input()
	
   if keyboard.is_pressed('w'):
        y[0] -= 1
        clear()
        display()
   if keyboard.is_pressed('s'):
        y[0] += 1
        clear()
        display()
   if keyboard.is_pressed('a'):
        x[0] -= 1
        clear()
        display()
   if keyboard.is_pressed('d'):
        x[0] += 1
        clear()
        display()

board()
display()

while True:
	on_press()
	

