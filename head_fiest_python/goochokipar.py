# じゃんけんプログラム
import random


choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)

user_choice = ''
print('You chose', user_choice, 'and the computer chose', computer_choice)

while (user_choice != 'rock' and
       user_choice != 'paper' and
       user_choice != 'scissors'):
    user_choice = input('rock, paper or scissors? ')

winner = ''
if user_choice == computer_choice:
    winner = 'Tie'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'
else:
    winner = 'User'

if winner == 'Tie':#あいこなのでuser_hcoiceでもいい
    print('We both chose', computer_choice + 'pray again.')
else :
    print(winner, 'won, The computer chose', computer_choice, '.')


#count = 0
# while count < 3:
#    if pattern == computer:
