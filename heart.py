from turtle import *
s=Screen()
s.setup(width=1.0,height=1.0)
speed(20)
colormode(255)
pencolor(255,0,0)
pensize(1)


pixel=20

l=left
r=right
def f():
    for a in range(5):
        forward(pixel)
        l(90)
        forward(pixel)
        r(90)

    forward(pixel)
    l(90)
    forward(pixel*3)
    l(90)

    for b in range(2):
        forward(pixel)
        r(90)
        forward(pixel)
        l(90)

    forward(pixel*2)
    l(90)

    for c in range(2):
        forward(pixel)
        r(90)
        forward(pixel)
        l(90)

fillcolor('red')

begin_fill()
f()


r(90)
penup()
goto(20,0)
pendown()

r=left
l=right


f()
goto(0,160)
goto(20,0)
end_fill()

color('black')
fillcolor('black')

def s():
    for sr in range(4):
        forward(pixel)
        right(90)


for c in range(7):
    begin_fill()
    penup()
    goto(20*c+20,20*c)
    pendown()
    s()
    end_fill()

for d in range(2):
    begin_fill()
    penup()
    goto(140,140+20*d)
    pendown()
    s()
    end_fill()

for e in range(3):
    begin_fill()
    penup()
    goto(120-e*20,180+e*20)
    pendown()
    s()
    end_fill()

for g in range(3):
    begin_fill()
    penup()
    goto(60-g*20,220-g*20)
    pendown()
    s()
    end_fill()

for i in range(2):
    begin_fill()
    penup()
    goto(0-i*20,200+i*20)    
    pendown()
    s()
    end_fill()

for j in range(4):
    begin_fill()
    penup()
    goto(-40-j*20,220-j*20)
    pendown()
    s()
    end_fill()

for k in range(2):
    begin_fill()
    penup()
    goto(-100,160-(k+1)*20)
    pendown()
    s()
    end_fill()

for o in range(5):
    begin_fill()
    penup()
    goto(-80+o*20,100-o*20)
    pendown()
    s()
    end_fill()

pencolor('white')
fillcolor('white')
for z in range(2):
    begin_fill()
    penup()
    goto(-20-z*20,180)
    pendown()
    s()
    end_fill()

begin_fill()
penup()
goto(-40,160)
pendown()
s()
end_fill()


done()