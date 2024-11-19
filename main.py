from turtle import Screen, Turtle
import time
from snake import Snake
import food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake() #calling the Snake class to generate our Snake
food = food.Food() #calling the Food class to generate our food
scoreboard = Scoreboard()

#The listen method will "listen" for key strokes that change direction of the snake.
screen.listen()
# Now we bind every change direction command to a key
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1) #wait .1 seconds before moving the head/body of the snake
    snake.move()

    # Now we detect the collision with food using a method from the turtle class called distance()
    if snake.head.distance(food) < 15: # We use 15 bc the food is 10 x10, so we add 5 for a little extra buffer
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    # Detect collision with the wall. We'll make the border 20 units shorter than the actual graph limit of 300.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail. If head collides with tail, trigger game_over.
    for segment in snake.segments[1:]: # This skips the first item/snake head segment, preventing an isntant game over when starting the game.
       if snake.head.distance(segment) < 10:
        game_is_on = False
        scoreboard.game_over()

    # This is old code that we used to
    #This was used before I learned about slicing and its ability to skip the first index in a list/tuple.
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass # This allows us to prevent the immediate game over that occurs when you start the game (bc the head's starting position is < 10)
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False


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
