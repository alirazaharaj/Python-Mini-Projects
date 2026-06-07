import random

comp=['apple','banana']
word=random.choice(comp)
guess=['_']*len(word)
i=1
while(i<12):
    user=input('Enter a word: ').lower()
    if len(user)!=1:
        print('Enter Only one word')
    elif user in word:
        for i, compw in enumerate(word):
            if user==compw:
                guess[i]=user
    else:
        print(f'Wrong! You try {i} times')
        i+=1
    if '_' not in guess:
        break
if '_' not in guess:
        print(guess)
        print(word)
        print('You won the Game ...........')
else:
    print('Sorry try again.............')
