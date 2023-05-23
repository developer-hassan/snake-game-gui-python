# Necessary imports for proper functionality
import random
from turtle import Turtle

# Define some colors of which the food will be generated each time
COLORS = ["orange", "yellow", "green", "blue", "purple"]

# This class deals with the food generation on the screen
class Food(Turtle):
    def __init__(self):
        # Initialize the food object with specific properties and behaviors
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()
        self.special_diet = self.generate_special_diet()

    def refresh(self):
        """
        Change the color of food to another random color from colors and places food at another random position.
        """ 
        self.color(random.choice(COLORS))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def generate_special_diet(self):
        special_diet = Turtle("circle")
        special_diet.penup()
        special_diet.color("red")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        special_diet.goto(random_x, random_y)
        special_diet.hideturtle()
        return special_diet
        
    def hide_special_diet(self):
        self.special_diet.hideturtle()

    def show_special_diet(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.special_diet.goto(random_x, random_y)
        self.special_diet.showturtle()