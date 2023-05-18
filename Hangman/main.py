import random
from random_word import RandomWords

class Hangman:
    def fill10(word1,word2):
        for i in range(len(word1)):
            rand = random.randint(1,2)
            if rand == 1:
                word2 = word2[:i] + word1[i] + word2[i+1:]
        return word2
    def __init__(self,word:str):
        flag = 5
        word = word.upper()
        empty = "_"*len(word)
        doneindices = []
        empty = Hangman.fill10(word,empty)
        print(empty)
        while '_' in empty and flag>0:
            letter = (input('Letter: ')).upper()
            if len(letter)>1:print("Enter a letter not a word.");continue
            if letter not in word or (word.count(letter)==empty.count(letter)) : flag-=1
            for index,value in enumerate(word):
                if str(index) not in doneindices:
                    if letter==value:
                        doneindices.append(index)
                        empty = empty[:index]+letter+empty[index+1:]
            print(empty+" Tries: "+str(flag))
            if flag==0:
                print("The word was "+word+" lmaoo couldnt even get that.")
            if empty==word:
                print("Congrats, the word was "+word+".")


generator = RandomWords()
Hangman(generator.get_random_word())
