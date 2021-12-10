import turtle as t
import random as r

aImage = "4.gif"

wn = t.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(aImage)
wn.bgpic("background.gif")

l = ['A','B','C','D']

aList = []
aLetters = []

for i in range(5):
    aList.append(t.Turtle())
    aLetters.append(r.choice(l))

#functions
def drawApple(index):
    global appleLetter
    aList[index].pu()
    aList[index].shape(aImage)
    wn.tracer(False)
    aList[index].setx(r.randint(-175,175))
    aList[index].sety(r.randint(-175,175))
    aList[index].sety(aList[index].ycor()-35)
    aList[index].color("white")
    aList[index].write(aLetters[index], align="center",font=("Arial", 40, "bold"))
    aList[index].sety(aList[index].ycor()+35)
    aList[index].showturtle()
    wn.tracer(True)
    wn.update()

def dropApple(index):
    aList[index].pu()
    aList[index].clear()
    aList[index].sety(-150)
    aList[index].hideturtle()
    aLetters[index] = r.choice(l)
    drawApple(index)

def typedA():
    for i in range(5):
        if aLetters[i] == 'A':
            dropApple(i)

def typedB():
    for i in range(5):
        if aLetters[i] == 'B':
            dropApple(i)

def typedC():
    for i in range(5):
        if aLetters[i] == 'C':
            dropApple(i)

def typedD():
    for i in range(5):
        if aLetters[i] == 'D':
            dropApple(i)

#Calling the functions
for i in range(5):
    drawApple(i)
    wn.onkeypress(typedA, 'a')
    wn.onkeypress(typedB, 'b')
    wn.onkeypress(typedC, 'c')
    wn.onkeypress(typedD, 'd')

    wn.listen()
    wn.mainloop()
