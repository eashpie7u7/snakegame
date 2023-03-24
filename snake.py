from turtle import *
from random import randrange
from freegames import square, vector
from  random import randrange, choice, randint

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    
    for body in snake:
        square(body.x, body.y, 9, cuerpo)

    square(food.x, food.y, 9, comida)
    update()
    if randrange(10)==0:
        if (food.x<200):
        #se genera un numero random entre 0 y 10
            food.x+=10
            #si sale 0 se mueve hacia la derecha 
    elif randrange(100)==1:
        if (food.x>0):
            food.x-=10
            #si sale 1 se mueve hacia la izquierda 
    elif randrange(10)==2:
        if (food.y<200):
            #se colocaron limites para evitar que se saliera la comida
            #de la pantalla
            food.y+=10
            #si sale 3 se mueve hacia arriba 
    elif randrange(100)==3:
        if (food.y>0):
        #para disminuir la probabilidad, se eligió 100
            food.y-=10
            #si sale 3 se mueve hacia abajo 
    ontimer(move, 100)
colores= ['fuchsia', 'orange', 'mediumslateblue', 'deepskyblue', 'chartreuse']
#se inició una lista de colores
n1 = randint(0, 4)
#se leigió un entero random que corresponde al index 
col_cuerpo=colores[n1]
removed_element = colores.pop(n1)
#con pop se eliminó el color que ya elegí para el cuerpo
n2=randint(0, 3)
#ya que tengo una opción menos en la lista
col_comida=colores[n2]
#se eligió un color para la comida
cuerpo=str(col_cuerpo)
comida=str(col_comida)
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()