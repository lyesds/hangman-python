class Car:
    def __init__(self):
        self.name = "Ferrari"

    def __init__(self, name, firstname):
        """Constructor our class"""
        self.name = name
        self.firstname = firstname
        self.age = 34
        self.place_residence = "Brussels"
        
        
class Hangman():
    """ Class defining my game 'Hangman', characterized by :
    - a list of possible words
    - the word to find
    - a number of lives
    - the list of correctly guessed letters
    - the list of wrongly guessed letters
    - turn_count : the number of times the player played
    - error_count: the number of errors made by the player player 
    - ...
    def __init__(self):
        self.name = "Ferrari"
