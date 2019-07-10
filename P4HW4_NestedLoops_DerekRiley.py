# Fun with squares 
# 07/10/19
# CTI 110 - P4HW4: Nested Loops
# Derek Riley 


#initialize turtle and random color 
import turtle
import random
win = turtle.Screen()

# make my turtle
t = turtle.Turtle()
t.shape("turtle")

#Choose color of Shape 
Colours = ['Purple', 'Blue']


for i in range(20):
    for i in range (2):
        t.color(random.choice(Colours))
        t.forward(180)
        t.right (90)
        t.forward (180)
        t.right (90)
    t.right (20)
        




# at the end, keep the window open until closed
win.mainloop()
