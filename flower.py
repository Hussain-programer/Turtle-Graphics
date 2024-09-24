import turtle as trt
import colorsys as cs
trt.setup(800,800)
trt.speed(0.5)
trt.width(2)
trt.title("Flower using Python Turtle Graphics")
trt.bgcolor("black")
trt.pensize(3)
for i in range(25):
    for j in range(15):
        trt.color(cs.rgb_to_hsv(i/25,i/15,1))
        trt.right(90)
        trt.circle(200-i*4,90)
        trt.left(90)
        trt.circle(200-i*4,90)
        trt.right(180)
        trt.circle(50,24)
trt.hideturtle()
trt.done()      