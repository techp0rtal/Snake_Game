# from turtle import Turtle
# #This is the snake class, which will be 1 of 3 classes used for this project.
# STARTING_POSITION = starting_positions = [(0, 0), (-20, 0), (-40, 0)]
# MOVE_DISTANCE = 20
# UP = 90
# DOWN = 180
# LEFT = 270
# RIGHT = 0
#
# class Snake:
#
#     def __init__(self):
#         self.segments = []
#         self.create_snake()
#         self.head = self.segments[0] # This will be the head of the snake
#
#     def create_snake(self):
#         for position in starting_positions:
#             new_segment = Turtle("square")
#             new_segment.color("white")
#             new_segment.penup()
#             new_segment.goto(position)
#             self.segments.append(new_segment)
#
#     def move(self):
#         for seg_num in range(len(self.segments) - 1, 0, -1):
#             new_x = self.segments[seg_num - 1].xcor()
#             new_y = self.segments[seg_num - 1].ycor()
#             self.segments[seg_num].goto(new_x, new_y)
#         self.head.forward(MOVE_DISTANCE)
#
#### WHY IS THIS STUPID PART BUGGED?! LEFT IS DOWN???
#     def up(self):
#         if self.head.heading() != DOWN: # This keeps the snake from going back on itself. if it's alrady going up, then it's not allowed to go back down
#             self.head.setheading(UP)
#
#     def down(self):
#         if self.head.heading() != UP:  # This keeps the snake from going back on itself
#             self.head.setheading(DOWN)
#
#     def left(self):
#         if self.head.heading() != RIGHT:  # This keeps the snake from going back on itself
#             self.head.setheading(LEFT)
#
#
#     def right(self):
#         if self.head.heading() != LEFT:  # This keeps the snake from going back on itself
#             self.head.setheading(RIGHT)
#


from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] # This will be the head of the snake

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self): # This keeps the snake from going back on itself
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
