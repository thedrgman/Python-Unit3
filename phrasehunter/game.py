from phrasehunter.phrase import Phrase
import random


class Game:
    def __init__(self):
        self.missed = 0
        self.phrase = [
            Phrase("do not stop believing"),
            Phrase("trust in Jesus"),
            Phrase("eyes are the window to the soul"),
            Phrase("united we stand"),
            Phrase("do not stop the music")
        ]
        self.active_phrase = None
        self.guesses = [" ",]
        self.lives = 5
        
        
    def get_random_phrase(self):
        self.active_phrase = random.choice(self.phrase)
        
        
    def welcome(self):
        print(""" Welcome to the Phase Hunter Game
        +++++++++++++++++++++++++++++++++++++++++++
        A random phrase is chosen and you 
        will have {} chances in getting it
        right. You are only able to choose 
        1 letter at a time and your guess
        cannot include any number, spaces,
        or other characters.
        Have fun.
        """.format(self.lives))
        
        
    def get_guess(self):
        user_input = input("\nGuess a letter. ")
        return user_input.lower()
    
    
    def game_over(self):
        if self.active_phrase.check_complete(self.guesses) == True:
            print("You have won the game")
        else:
            print("You ran out of guesses. The phrase was '{}'.".format(self.active_phrase))
        new_game = input("Would you like to play again? Type Y/N")
        if new_game.lower() == 'y':
            self.guesses = [" ",]
            self.start()
        else:
            print("Thank you for playing. See you next time!!!")
        
        
    def start(self):
        self.welcome()
        self.missed = 0
        self.get_random_phrase()
        while self.missed < self.lives:
            print("\n")
            display = self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            error = True
            while error == True:
                if user_guess == "quit":
                    break
                if user_guess.isalpha():
                    if len(user_guess) == 1:
                        break
                    else:
                        print("Your guess cannot have more than 1 letter. Please try again.")
                        user_guess = self.get_guess()
                        continue
                else:
                    print("Your guess can only contain a letter, spaces and any other character is invalid.\n Please try again.")
                    user_guess = self.get_guess()
                    continue
                    
            if user_guess in self.guesses:
                print("You already guessed that letter, pick another letter")
            else:
                self.guesses.append(user_guess)
                if self.active_phrase.check_letter(user_guess):
                    display
                else:
                    print("You have guessed an incorrect letter. Try again.")
                    self.missed += 1
                    print("You have {} out of {} lives remaining!".format((self.lives - self.missed), self.lives))
            display
            if self.active_phrase.check_complete(self.guesses):
                break
        self.game_over()
