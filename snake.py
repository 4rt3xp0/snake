import turtle,time,random,os

d = 0.1
score = 0
high_score = 0
snake_color = "darkblue"
snake_shape = ""

s = turtle.Screen()
s.title("Snake")
s.bgcolor("#654321")
s.setup(width=660, height=660)
s.tracer(0)
draw = turtle.Turtle()
draw.color("#013208","#013208")
draw.begin_fill()
draw.hideturtle()
draw.penup()
draw.goto(-330,330)
draw.pendown()
for i in range(4):
    draw.forward(660)
    draw.right(90)
draw.end_fill()
draw.color("green","green")
draw.begin_fill()
draw.hideturtle()
draw.penup()
draw.goto(-310,310)
draw.pendown()
for i in range(4):
    draw.forward(620)
    draw.right(90)
draw.end_fill()

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

def up():
    if not segments:
        head.direction = "up"
        return
    if segments[0].xcor()!=head.xcor():
        head.direction = "up"

def down():
    if not segments:
        head.direction = "down"
        return
    if segments[0].xcor()!=head.xcor():
        head.direction = "down"

def left():
    if not segments:
        head.direction = "left"
        return
    if segments[0].ycor()!=head.ycor():
        head.direction = "left"

def right():
    if not segments:
        head.direction = "right"
        return
    if segments[0].ycor()!=head.ycor():
        head.direction = "right"

def Quit():
    os._exit(0)

def pause():
    try:
        lst = list(s.textinput("GAME PAUSED","Press Enter to continue").split())
    except:
        s.listen()
        return
    
    if len(lst) == 1:
        if lst[0]=="exit" or lst[0]=="quit" or lst[0]=="q":
            os._exit(0)
        if lst[0]=="n" or lst[0]=="new":
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            d = 0.1
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
    if len(lst) == 2:
        if lst[0]=="color" or lst[0]=="c":
            try:
                for i in range(len(segments)):
                    segments[i].color(lst[1])
                draw.color(lst[1])
                global snake_color
                snake_color = lst[1]
            except:
                s.listen()
                return
        if lst[0]=="headcolor" or lst[0]=="hc":
            try:
                head.color(lst[1])
            except:
                s.listen()
                return
        if lst[0]=="background" or lst[0]=="bg":
            try:
                s.bgcolor(lst[1])
            except:
                s.listen()
                return
        if lst[0]=="foodcolor" or lst[0]=="fc":
            try:
                food.color(lst[1])
            except:
                s.listen()
                return
                
    s.listen()
        
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

s.listen()
s.onkeypress(up, "w")
s.onkeypress(down, "s")
s.onkeypress(left, "a")
s.onkeypress(right, "d")
s.onkeypress(up, "Up")
s.onkeypress(down, "Down")
s.onkeypress(left, "Left")
s.onkeypress(right, "Right")
s.onkeypress(Quit, "q")
s.onkeypress(pause, "e")

while True:
    s.update()

    if head.xcor()>310 or head.xcor()<-310 or head.ycor()>310 or head.ycor()<-310:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        d = 0.1
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 230)
        food.goto(x,y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color(snake_color)
        new_segment.penup()
        segments.append(new_segment)

        d -= 0.001
        score += 1
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            score = 0
            d = 0.1
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(d)

s.mainloop()
#by: 4rt3xp0