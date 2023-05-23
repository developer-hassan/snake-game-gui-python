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
        self.update()

    def update(self):
        """
        Clears the previous drawings of a turtle and write the updated score on screen. Then increments the score.
        """
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1

    def game_over(self):
        """
        Displays the Game Over string at the center of the screen.
        """
        self.setposition(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT)

    def special_update(self):
        """
        Updates the score by increment of 5.
        """
        self.score += 4
        self.update()
