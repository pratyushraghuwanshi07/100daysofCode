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

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors"))
ai = random.randint(0,2)
if user == 0:
  print(f"You chose rock \n {rock} \n")
  if ai == 0:
    print(f"Computer chose rock \n {rock} \n. Its a draw.")
  elif ai == 1:
    print(f"Computer chose paper \n {paper} \n. Computer wins.")
  else:
    print(f"Computer chose scissors \n {scissors} \n. You win.")

if user == 1:
  print(f"You chose paper \n {paper} \n")
  if ai == 0:
    print(f"Computer chose rock \n {rock} \n. You win.")
  elif ai == 1:
    print(f"Computer chose paper \n {paper} \n. Its a draw.")
  else:
    print(f"Computer chose scissors \n {scissors} \n. Computer wins.")

if user == 2:
  print(f"You chose scissors \n {scissors} \n")
  if ai == 0:
    print(f"Computer chose rock \n {rock} \n. Computer Wins.")
  elif ai == 1:
    print(f"Computer chose paper \n {paper} \n. YTou win.")
  else:
    print(f"Computer chose scissors \n {scissors} \n. Its a draw.")
    