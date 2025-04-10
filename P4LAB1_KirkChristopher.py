#Christopher Kirk
#04/04/2025
#P4LAB1
#Use turtle and  loops to draw shapes



import turtle


win = turtle.Screen()
pen = turtle.Turtle()


pen.pensize(5)
pen.color("red")
pen.shape('arrow')


for side in range(4):
    pen.forward(300)
    pen.left(90)


sides = 3
while sides > 0:
    pen.forward(200)
    pen.right(120)
    sides = sides - 1


win.mainloop()
    
