import random
import re


class Hangman:


    def __init__(self,wordlist):
        self.worldlist = wordlist
        self.attempts_remaining = 10
        self.current_letter = ""
        self.chosen_word = ""
        self.guessed_letters = []


    def choose_the_word(self):

        file = open(self.worldlist)
        words = file.read().split('\n')
        word_count = len(words)
        self.chosen_word = words[random.randrange(0, word_count)] 
        self.word_status = ['-' for i in range(len(self.chosen_word))]


    def fill_the_word_status(self):

        num_of_range = random.randrange(2,3)
        for i in range(num_of_range):
            position = random.randrange(0, len(self.chosen_word))
            self.word_status[position] = self.chosen_word[position]
    
    def guess_the_letter(self):

        letter = input('Guess the letter : ')
        if(letter in self.guessed_letters):
            print('You have already guessed that letter . Your guesses : {} '.format(','.join(self.guessed_letters)))
            return
        self.guessed_letters.append(letter)   
        occurences = []
        occurence = re.finditer(letter, self.chosen_word)

        for m in occurence:
            occurences.append(m.start())

        if(len(occurences) == 0):
            self.attempts_remaining -= 1
            print('Oops! Your guess was wrong . Attempts remaining is {}'.format(self.attempts_remaining))
            hangman.graphic()
        else:
            for position in occurences:
                self.word_status[position] = self.chosen_word[position]
                print("Correct Word!")
        
    def get_word_status(self):
        print("Current Status: {}\n".format(''.join(self.word_status)))
    
    def graphic(self):
        if(self.attempts_remaining == 9):
            print("------------------------------")
            print("|            O               |")
            print("|                            |")
            print("|                            |")
            print("|                            |")
            print("|                            |")
            print("|                            |")
            print("|            [Made By vivek] |")
            print("------------------------------")
        if(self.attempts_remaining == 8):
            print("------------------------------")
            print("|            O               |")
            print("|            |               |")
            print("|                            |")
            print("|                            |")
            print("|                            |")
            print("|                            |")
            print("|            [Made By vivek] |")
            print("------------------------------")
        if(self.attempts_remaining == 7):
            print("------------------------------")
            print("|           \O               |")
            print("|            |               |")
            print("|            |               |")
            print("|                            |")
            print("|                            |")
            print("|                            |")
            print("|            [Made By vivek] |")
            print("------------------------------")
        if(self.attempts_remaining == 6):
            print("------------------------------")
            print("|           \O/              |")
            print("|            |               |")
            print("|            |               |")
            print("|                            |")
            print("|                            |")
            print("|                            |")
            print("|            [Made By vivek] |")
            print("------------------------------")
        if(self.attempts_remaining == 5):
            print("------------------------------")
            print("|           \O/              |")
            print("|            |               |")
            print("|            |               |")
            print("|           / \              |")
            print("|                            |")
            print("|                            |")
            print("|            [Made By vivek] |")
            print("------------------------------")
        if(self.attempts_remaining == 4):
            print("------------------------------")
            print("|           \O_/             |")
            print("|            |               |")
            print("|            |               |")
            print("|           / \              |")
            print("|                            |")
            print("|                            |")
            print("|            [Made By vivek] |")
            print("------------------------------")
        if(self.attempts_remaining == 3):
            print("------------------------------")
            print("|           \O_/_            |")
            print("|            |               |")
            print("|            |               |")
            print("|           / \              |")
            print("|                            |")
            print("|                            |")
            print("|            [Made By vivek] |")
            print("------------------------------")
        if(self.attempts_remaining == 2):
            print("------------------------------")
            print("|           \O__             |")
            print("|            |\              |")
            print("|            |               |")
            print("|           / \              |")
            print("|                            |")
            print("|                            |")
            print("|            [Made By vivek] |")
            print("------------------------------")
        if(self.attempts_remaining == 1):
            print("------------------------------")
            print("|           \O_|             |")
            print("|            |\              |")
            print("|            |               |")
            print("|           / \              |")
            print("|                            |")
            print("|                            |")
            print("|            [Made By vivek] |")
            print("------------------------------")
        if(self.attempts_remaining == 0):
            print("------------------------------")
            print("|            O_|             |")
            print("|           /|\              |")
            print("|            |               |")
            print("|           / \              |")
            print("|                            |")
            print("|                            |")
            print("|            [Made By vivek] |")
            print("------------------------------")




# hangman = Hangman("E:\\pythonProjects\\1.Hangman\\wordslist.txt") #Enter wordlist PATH here
hangman = Hangman("/media/vivek/Study/pythonProjects/1.Hangman/wordslist.txt") #Enter wordlist PATH here
hangman.choose_the_word()
hangman.fill_the_word_status()

while True:
    hangman.get_word_status()
    hangman.guess_the_letter()
    if(hangman.attempts_remaining == 0):
        print("Out of Attempts. The Word was {}. Game Over Rip!\n".format(hangman.chosen_word))
        break
    elif (hangman.chosen_word == ''.join(hangman.word_status)):
        print("Hurray!! you Won The Game !\n")
        break




        

    