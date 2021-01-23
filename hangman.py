class Word():
    def __init__(self, chosen_word):
        self.chosen_word = dict((k, False) for k in chosen_word)
        self.guesses = []
        self.guesses_remaining = 8
        self.gameover = False
        self.woord = chosen_word
 
    def check(self, input):
        if(self.guesses.count(input) > 0):
            print("you have guessed that letter")
            return
        self.guesses.append(input)
        result = self.chosen_word.get(input)
        if(result == False):
            self.chosen_word[input] = True
        else:
            self.guesses_remaining -= 1
        if self.guesses_remaining == 0:
            print("You are out of guesses, you lose")
            self.gameover = True
            return
        counter = 0
        for value in self.chosen_word.values():
            if value == True:
                counter += 1
        if counter == len(self.chosen_word.values()):
            self.gameover = True
            print("You won")

    def displayWord(self):
        for char in self.woord:
            if self.chosen_word[char] == False or not self.chosen_word[char]:
                print("_", end=" ")
            elif self.chosen_word[char] == True:
                print(char, end=" ")
        

chosen_word = Word("alabama")
print(chosen_word.chosen_word)
while True:
      if(chosen_word.gameover):
        print("bye!")
        break
      chosen_word.displayWord()
      print("Guess a letter", end=": ")
      user_input = input()
      chosen_word.check(user_input)