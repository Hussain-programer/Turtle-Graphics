from turtle import*
import colorsys as cs
bgcolor("black")
pensize(2)
speed(0)
h = 0
def draw(int,t):
    circle(5+t,90)
    left(int)
    circle(5+t,60)
goto(-10,0)
for i in range(200):
    c = cs.rgb_to_hsv(h,1,1)
    h += 0.005
    color(c)
    up()
    draw(90,i/50)
    draw(180,i/2)
    down()
    fillcolor("black")
    begin_fill()
    draw(1/2,0)
    draw(180,i/2)
    draw(90,i/2)
    end_fill()
    draw(60,i)
done()
