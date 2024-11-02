import turtle
import math

def pifagor_tree(t, order, size):
    if order == 0:
        return
    # основна гілка 
    t.forward(size)
    
    # позиція перед входом в розгалудження
    position = t.position()
    heading = t.heading()
    new_size = size * (1 / math.sqrt(2)) # нова довжина

    # малюємо ліву гілку
    t.left(45)
    pifagor_tree(t, order - 1, new_size)
    
    # повернення перед розгалудженням
    t.setposition(position)
    t.setheading(heading)

    # малюємо праву гілку
    t.right(45)
    pifagor_tree(t, order - 1, new_size)
    
    # повернення перед розгалудженням
    t.setposition(position)
    t.setheading(heading)
    t.backward(size)  # Повертаємося назад
    

def draw(order, size=100):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.left(90)
    pifagor_tree(t, order, size)
    turtle.done()

# Виклик функції
draw(6)