import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snow(order, size=500):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-size / 2, size / 2)
    t.pendown()

    for angle in [120, 120, 0]:
        koch_curve(t, order, size)
        t.right(angle)

    window.mainloop()

# Виклик функції
while True:
    try:
        depth = int(input('Enter depth: '))
        if depth >= 0:
            break
        else:
            print('Wrong format! Only integers >=0 allowed!')  
    except:
        print('Wrong format! Only integers >=0 allowed!')
        
draw_koch_snow(depth)