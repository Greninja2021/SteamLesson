from turtle import *

drawing_area = Screen()
drawing_area.setup(width=750, height=500)

shape('square')
for i in range(88):
    right(22 + i)
    forward(8 + (i * 28 ))
    right(44 + i)

done()