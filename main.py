"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')
tiles = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')[:32] * 2 #Cambiar a letras
state = {'mark': None}
hide = [True] * 64
taps = 0


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def all_revealed():
    """Return True if all tiles are revealed."""
    return all(not hidden for hidden in hide)
def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    global taps 
    
    taps += 1
    
    goto(0,200)
    ontimer(write(f"Taps: {taps}", align= "right",font=('Arial', 30, 'normal')), 1000) # desplegar por un segundo
    goto(x,y)

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()
    

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']
    

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 15, y + 5) 
        color('black')
        
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)
    
    if all_revealed():  # Checa si todas las tiles se revelaron
        goto(0, -220)
        color('black')
        write("All tiles revealed!", align='center', font=('Arial', 30, 'bold'))
       



shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()