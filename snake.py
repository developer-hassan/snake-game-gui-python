# Required import for generating and extending a snake
from turtle import Turtle

# Some constants for a consistent behavior
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """
    Deals with the snake generation and all its movement and extension.
    """

    def __init__(self):
        # Initialize the snake object with specific properties and behaviors
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("triangle")
        self.special_diet = 0

    def create_snake(self):
        """
        Creates a snake with three turtle segments at starting positions
        """
        for position in STARTING_POSITIONS:
            # Create a 20by20 pixels square turtle three times at specified position
            self.add_segment(position)

    def move(self):
        """
        Modify the position of each segment of a snake from last to first. Then moves the head of the snake 20 paces forward
        """
        # Start from the tail (last segment) of the snake
        for seg_number in range(len(self.segments) - 1, 0, -1):
            # get the position of previous segment
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            # Update the position of current segment to be at the position of previous segment
            self.segments[seg_number].setposition(new_x, new_y)

        # Move the first segment forward 20 paces once all segments positions are updated
        self.head.forward(20)

    def up(self):
        """
        Move the snake direction to Up side if it is not facing Down already
        """
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        """
        Move the snake direction to Down side if it is not facing Up already
        """
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        """
        Move the snake direction to Left side if it is not facing Right already
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        """
        Move the snake direction to Right side if it is not facing Left already
        """
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def add_segment(self, position):
        """
        Adds a new turtle to the current segments each time the snake eats food.

        Args:
            position (tuple): A position at which the snake segment is to be created
        """
        # Create a new turtle (snake segment) with specific properties and behaviors
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        # Add the segment to the current segments list each time a new segment is created
        self.segments.append(new_segment)

    def extend(self):
        """
        Calls the add_segment method with the position of last segment of snake
        """
        self.add_segment(self.segments[-1].position())

    def reset_state(self):
        """
        Deletes the existing turtle from the screen and initialize the snake again.
        """
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("triangle")
        self.special_diet = 0
