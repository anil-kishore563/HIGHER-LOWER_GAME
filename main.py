from replit import clear
import random
from art import logo,vs
from game_data import data
score=0
loop=True

def heighest(A,B):
  if data[n1]['follower_count']>data[n2]['follower_count']:
    return A
  else:
    return B 
n1=random.randint(0,49)     
s=0

while loop==True: 
  print(logo)
  print()
  if s!=0:
    print(f"yeah,that's correct answer.your score is {score}")
  s=1

  print(f"Compare A: {data[n1]['name']},{data[n1]['description']},{data[n1]['country']}")
  print()
  print(vs)
  print()
  n2=random.randint(0,49)
  print(f"Compare B: {data[n2]['name']},{data[n2]['description']},{data[n2]['country']}")

  your_guess=input("Who has more followers? Type 'A' or 'B':")
  your_guess=your_guess.upper()
  if heighest('A','B')==your_guess:
    clear()
    score+=1
    n1=n2
  else:
    loop=False
    clear()
    print(f"Sorry, that's wrong. Final score: {score}")  
