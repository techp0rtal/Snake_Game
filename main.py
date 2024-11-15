from turtle import Screen, Turtle
import time
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

#The listen method will "listen" for key strokes that change direction of the snake.
screen.listen()
# Now we bind every key to
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1) #wait .1 seconds before moving the head/body of the snake
    snake.move()




screen.exitonclick()

#This code works, but doesn't use OOP. Just keeping it for teaching purposes.
# from turtle import Screen, Turtle
# import time
#
# #This is the snake class, which will be 1 of 3 classes used for this project.
# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)
# starting_positions = [(0, 0), (-20, 0), (-40, 0)]
# segments = []
#
# #dont forget about tuples!
#
# for position in starting_positions:
#     new_segment = Turtle(shape="square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)
#
#
# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(.1)
#     for seg_num in range(len(segments)-1, 0, -1):
#         new_x = segments[seg_num -1].xcor()
#         new_y = segments[seg_num - 1].ycor()
#         segments[seg_num].goto(new_x, new_y)
#     segments[0].forward(20)
