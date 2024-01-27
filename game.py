import random
import time


PLAYER_WINS = [7, 11]
CASINO_WINS = [2, 3, 12]
result = None
goal_number = 0

print("Hi there, let's start the game. Roll the dices!")
time.sleep(2)   
def roll():
  """ The function generates two random integers for two dices per each roll. And returns the sum of two dices. """
  roll_1 = random.randint(1, 6)
  roll_2 = random.randint(1, 6)
  _sum = roll_1 + roll_2
  print(f"The sum of the roll is {_sum}.")
  time.sleep(2) 
  return _sum


output_1 = roll()  



if output_1 in PLAYER_WINS:
  result = "Congratulations, You won!"
elif output_1 in CASINO_WINS:
  result = "Unfortunalty, You lost"
else:
  goal_number = output_1
  print(f"So far you neither win nor lost, now your goal number is {goal_number}. Roll the dices.")
  time.sleep(2) 

  while result is None: 
    output = roll() 
    if output == 7:
      result = "Unfortunalty, You lost"
    elif output == goal_number:
      result = "Congratulations, You won!"

print(result)
