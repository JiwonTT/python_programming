# MIT Open Course Ware
## Introduction to Computer Science and Programming in Python
6.0001 Fall 2016
Problem Set 2




Game Rules:
1. The user starts with 3 warnings.
2. If the user inputs anything besides an alphabet (symbols, numbers), tell the user that they can only input an alphabet.
    a. If the user has one or more warning left, the user should lose one warning. Tell the user the number of remaining warnings.
    b. If the user has no remaining warnings, they should lose one guess.
3. If the user inputs a letter that has already been guessed, print a message telling the user the letter has already been guessed before.
    a. If the user has one or more warning left, the user should lose one warning. Tell the user the number of remaining warnings.
    b. If the user has no warnings, they should lose one guess.
4. If the user inputs a letter that hasn’t been guessed before and the letter is in the secret word, the user loses no guesses.
5. Consonants: If the user inputs a consonant that hasn’t been guessed and the consonant is not in the secret word, the user loses one guess if it’s a consonant.
6. Vowels: If the vowel hasn’t been guessed and the vowel is not in the secret word, the user loses two guesses. Vowels are a, e, i , o, and u. y does not count as a vowel.

Game Score:
guesses_remaining* number unique letters in secret_word

links: https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/
