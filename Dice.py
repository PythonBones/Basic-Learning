#dice
import random
roll = 'Yes'
while roll == 'Yes':
    for x in range(1, 6):
        num = random.randint(1, 6)
    print(num)
    roll = input('Role again? Yes/No:  ')
