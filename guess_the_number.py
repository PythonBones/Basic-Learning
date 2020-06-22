# guess the number

import random
roll = 'Yes'
while roll == 'Yes':
    for x in range(1, 10):
        urnum = input('Guess the number  1 - 10:  ')
        num = random.randint(1, 10)
        if num == int(urnum):
            print(f'Correct! {urnum} was the right answer.')
            print()
        else:
            print(f'Wrong! The correct answer is {num}.')
            print()
        roll = input('Play again? Yes/No:  ')
        if roll != 'Yes':
            break
