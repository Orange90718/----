import turtle
import time
import random
import pygame

pygame.init()
speed = 9

#score
score = 0
high_score = 0
score_rate = 1

#set up the screen
window=turtle.Screen()
window.title("小精靈")
window.bgcolor("#000000")
window.setup(width=600,height=600)
window.tracer(0)#turn off the screen updates

#snack head
head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("#FFFFFF")
head.penup()
head.goto(0,0)
head.direction="stop"

#snack food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments=[]

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 Hight Score: 0",align="center",font=("Courier", 24, "normal"))
pen

#clock
clock = pygame.time.Clock()
time_passed = clock.tick()

#functions
def go_up():
    if head.direction !="down":
        head.direction="up"

def go_down():
    if head.direction !="up":
        head.direction="down"

def go_left():
    if head.direction !="right":
        head.direction="left"

def go_right():
    if head.direction !="left":
        head.direction="right"
    
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y + speed)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y - speed)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x - speed)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x + speed)

def create_hex():
    return str(hex(random.randint(0,15)))[2:]

def speedup():
    global speed
    global score_rate
    speed += 3
    score_rate += 0.5


#keyboard bindings
window.listen()
window.onkeypress(go_up,"w")
window.onkeypress(go_down,"s")
window.onkeypress(go_left,"a")
window.onkeypress(go_right,"d")
window.onkeypress(go_up,"W")
window.onkeypress(go_down,"S")
window.onkeypress(go_left,"A")
window.onkeypress(go_right,"D")
window.onkeypress(go_up,"Up")
window.onkeypress(go_down,"Down")
window.onkeypress(go_left,"Left")
window.onkeypress(go_right,"Right")
window.onkeypress(speedup,"space")

pygame.mixer.init()
pygame.mixer.music.load('final.mp3')
pygame.mixer.music.play(-1)

#main game loop
while True:
    window.update()
    
    #check for a collision with the border 
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"

        #hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        #clear the segments list
        segments.clear()

        #reset the score
        score = 0
        speed = 9
        score_rate = 1

        #update the score display
        pen.clear()
        pen.write("Score: {} High Score: {}".format(int(score), int(high_score)),align="center",font=("Courier",24,"normal"))
    #check for a collision with the food
    
    if head.distance(food) < 20:
        #move the food to a random spot
        x=random.randint(-270,270)
        y=random.randint(-270,270)
        food.goto(x,y)
        
        #add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        window.bgcolor("#0"
                       + create_hex() + create_hex() + create_hex() + create_hex() + create_hex())
        
        #increase the score
        score += 10 * score_rate

        if score > high_score:
            high_score = score
       
        pen.clear()
        pen.write("Score: {} High Score: {}".format(int(score), int(high_score)),align="center",font=("Courier",24,"normal"))
        
    #move the end segments in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    #move segment 0 to where the head is
    if len(segments) > 0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    
    move()

    #check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 1:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"

            #hide the segments
            for segment in segments:
                segment.goto(1000,1000)

            #clear the segments list
            segments.clear()

            #reset the score
            score = 0
            speed = 9
            score_rate = 1

            #update the score display
            pen.clear()
            pen.write("Score: {} High Score: {}".format(int(score), int(high_score)),align="center",font=("Courier",24,"normal")) 

            

    clock.tick(24)
    
window.mainloop()

pygmae.quit() 
