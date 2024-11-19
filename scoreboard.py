from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal") # Global tuple. With this, we don't need to dig through the program to change font.


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white") # Got to change the color of the text so it's visible against a black background
        self.penup()  # Keeps it from drawing a line to the top of the screen
        self.goto(0, 270)  # Puts the scoreboard at the top of the screen. Do it before writing.
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)



    def increase_score(self):
        self.clear() # Clears the scoreboard so the numbers don't write over each other.
        self.score += 1
        self.update_scoreboard()



