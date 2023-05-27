# Import the Turtle class to inherit its behaviors
from turtle import Turtle

# Defining some constants for consistent design
ALIGNMENT = "center"
FONT = ("Consolas", 18, "normal")


# Create a scoreboard class to deal with the score updation
class Scoreboard(Turtle):
    """
    Deals with the updating of scoreboard and displaying game over to the user when needed
    """

    def __init__(self):
        # Initializing a scoreboard object with specific properties and bheaviors
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.setposition(0, 250)
        try:
            with open("./data.txt") as f:
                self.high_score = int(f.read())
        except:
            self.high_score = 0
        self.update()

    def update(self):
        """
        Clears the previous drawings of a turtle and write the updated score on screen. Then increments the score.
        """
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increment_score(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        try:
            with open("./data.txt", mode="w") as f:
                f.write(str(self.high_score))
        except:
            pass
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)

    def reset_state(self):
        """
        Displays the Game Over string at the center of the screen.
        """
        self.setposition(0, 250)
        self.score = 0
        self.update()

    def special_update(self):
        """
        Updates the score by increment of 5.
        """
        self.score += 5
        self.update()
