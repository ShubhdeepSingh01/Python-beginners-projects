import random

words = ["apple", "apricot", "avocado", "banana", "blackberry", "blackcurrant", "blueberry", "boysenberry",
    "cherry", "coconut", "cranberry", "cucumber", "currant", "date", "dragonfruit", "durian", 
    "elderberry", "fig", "goji berry", "gooseberry", "grape", "grapefruit", "guava", "honeydew", 
    "jackfruit", "kiwi", "kumquat", "lemon", "lime", "lychee", "mango", "mulberry", "nectarine", 
    "orange", "papaya", "passionfruit", "peach", "pear", "persimmon", "pineapple", "plum", "pomegranate", 
    "raspberry", "redcurrant", "rhubarb", "starfruit", "strawberry", "tangerine", "watermelon"
]

word = random.choice(words)

hidden_word = [word[0]] + ['_']*(len(word)-2) + [word[-1]]
def display_word():
    print(' '.join(hidden_word))
def main():
    chances = len(word) + 2
    guessed_letters = []
    display_word()
    print("Let's guess name of the fruit")
    flag = True
    while flag:
        try:
            n = input("\nEnter the character you want to guess: ")
        except len(n)>1:
            print("Please enter a single character!")
        if n in guessed_letters:
            print("You have already guessed this letter")
        guessed_letters.append(n)
        if n in word[1:-1]:
            print('Your guess was right!\nThe word now looks as follows.')
            for i in range(1, len(word) - 1):
                 if word[i] == n:
                     hidden_word[i] = n
        else:
            chances -= 1
            print("Uhh! You got it wrong this time!\nTry again!")
            print(f"\nYour remaining chances are {chances}")

        display_word()       
        if '_' not in hidden_word:
            print('Congratulations, You guessed the word!')
            break
        elif chances == 0:
            print(f"You ran out of chances. The word was {word}")
            flag = False
main()


