class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()
                
        
    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses:
                print('{}'.format(letter), end=" ")
            else:
                print("_", end=" ")
        
    
    
    def check_letter(self, guess):
        if guess in self.phrase:
            return True
        else:
            return False
    
    
    def check_complete(self,guesses):
        for letter in self.phrase:
            if letter not in guessess:
                return False
        return True
