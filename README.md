# hangman-python
Coding the Hangman game in Python, 1st solo project

---

## -What
This is the firt solo project of the BeCode's AI bootcamp using Python. We are asked to 
code the [Hangman game](https://en.wikipedia.org/wiki/Hangman_(game)).
![hangman_pic](https://camo.githubusercontent.com/6b01d4f999e7351a4c62597fd64843e4f08339ad36eceb68fc77a514af9c3e51/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f7468756d622f662f66342f48616e676d616e5f67616d652e6a70672f38303070782d48616e676d616e5f67616d652e6a7067)
---
## -Why
This project will allow to test our comprehension of the new material we learned during the firs two weeks of the training.

---
## -How
The code should be clean and use the concepts of class, attributes and methods,
 but also typing and regular expression.
I imported the random and re packages.
I created a Hangman class.
Inside the class, I created attributes (the word to discover, the number of tries, the number of lives (remaining),...).
Methods are also created as advised: design the play, start the plays and finish it either a game over or a well played game.
---

## -Who
Lyes Rouabah

---
## -When
Started May 20th 2021.
Deadline is May 21st at 4:30 pm.

---
## Feedback
1. Not a good practice to define attributes at the class level itself.
   It is recommended to define attributes in the __init__ part.
2. Apply flake8 to the script.
3. Simplify "^[a-zA-Z]$" by using "^[a-Z]$". 