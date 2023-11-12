import turtle
import time
import random
import tkinter as tk

delay = 0.1
score = 0
poison_spawn_rate = 0.05  # Initial spawn rate for poisonous apples

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turns off the screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "Up"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Poisonous apple
poison = turtle.Turtle()
poison.speed(0)
poison.shape("circle")
poison.color("purple")
poison.penup()
poison.goto(0, -100)
poison.hideturtle()  # Hide the poisonous apple initially

# Snake body
segments = []

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def go_up():
    if head.direction != "Down":
        head.direction = "Up"

def go_down():
    if head.direction != "Up":
        head.direction = "Down"

def go_left():
    if head.direction != "Right":
        head.direction = "Left"

def go_right():
    if head.direction != "Left":
        head.direction = "Right"

def move():
    if head.direction == "Up":
        y = head.ycor()
        head.sety(y + 20)

    elif head.direction == "Down":
        y = head.ycor()
        head.sety(y - 20)

    elif head.direction == "Left":
        x = head.xcor()
        head.setx(x - 20)

    elif head.direction == "Right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# Main game loop
while True:
    wn.update()

    # Check for a collision with the border
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Up"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0
        score_display.clear()
        score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random location
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Add a segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("light green")
        new_segment.penup()
        segments.append(new_segment)

        # Update the score
        score += 1
        score_display.clear()
        score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

        # Adjust the spawn rate of poisonous apples
        poison_spawn_rate -= 0.001
        if poison_spawn_rate < 0.01:
            poison_spawn_rate = 0.01

    # Check for a collision with the poisonous apple
    if head.distance(poison) < 20:
        # Move the poisonous apple to a random location
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        poison.goto(x, y)

        # Decrease the score
        score -= 1
        score_display.clear()
        score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Move the end segments first in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move the first segment to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Move the snake
    move()

    # Check for head collisions with body segments
    for segment in segments:
        if head.distance(segment) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Up"

            # Hide the segments
            for seg in segments:
                seg.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0
            score_display.clear()
            score_display.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

    # Spawn a poisonous apple with a probability based on the spawn rate
    if random.random() < poison_spawn_rate:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        poison.goto(x, y)
        poison.showturtle()

    time.sleep(delay)
    
