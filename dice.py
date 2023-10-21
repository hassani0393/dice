# Using built-in random module for generating rolls
import random
import logging


class Dice:
    """simulates a dice for use in games.
    The class is capable of generating random dice rolls between 1 and value of dice_sides variable.
    Also keeps a history of rolls, and provides a reset feature to clear the roll history.
    """

    # Set the number of dice sides here
    dice_sides = 6

    # sets the maximum number of rolls possible
    max_rolls = 40

    possible_rolls = list(range(1, dice_sides))

    def __init__(self):
        self.current_num_of_roll = 0
        self.current_roll = 0
        self.roll_history = []

    def roll(self):
        """Generates a random roll from 1 to dice_sides and returns it
        and adds the roll value to roll_history list."""
        if self.current_num_of_roll <= Dice.max_rolls:
            self.current_roll = random.randint(1, Dice.dice_sides)
            self.roll_history.append(self.current_roll)
            self.current_num_of_roll += 1
            return self.current_roll
        else:
            raise ValueError("Number of rolls exceeds maximum rolls!")

    def get_current_roll(self):
        """Returns current roll. If no roll has been done yet, returns a message."""
        if self.current_num_of_roll == 0:
            raise ValueError("No roll yet. Please roll the dice first!")
        elif self.current_roll in Dice.possible_rolls:
            return self.current_roll
        else:
            raise ValueError(
                "Invalid Value for current roll, Something has gone horribly wrong!!"
            )

    def get_roll_history(self):
        return self.roll_history

    def reset(self):
        """Resets the current roll to initial value of 0 and clears roll history list."""
        self.current_roll = 0
        self.roll_history = []


dice1 = Dice()

dice1.get_current_roll()
