rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
options = list(("rock1", "paper1", "scissors1"))
Player = input("rock, paper, or scissors?")
CPU = random.choice(options)
if CPU == "rock1":
  print(rock)
  if Player == "rock":
    print("Tie!")
  elif Player == "scissors":
    print("Your opponent choose Rock! YOU LOSE")
  elif Player == "paper":
    print("Your opponent choose Rock! YOU WIN")

if CPU == "paper1":
  print(paper)
  if Player == "rock":
      print("Your opponent choose paper! YOU LOSE")
  elif Player == "scissors":
    print("Your opponent choose paper! YOU WIN!")
  elif Player == "paper":
    print("tie!")
    
if CPU == "scissors1":
  print(scissors)
  if Player == "rock":
      print("Your opponent choose scissors! YOU WIN!")
  elif Player == "scissors":
    print("Tie!")
  elif Player == "paper":
    print("Your opponent choose paper! YOU LOSE")
else:
  ("ok")