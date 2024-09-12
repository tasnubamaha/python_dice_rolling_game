
#Loop
 #Ask: roll the dice?
 # lower() is for lowercase letter string
 # If user enters y
 # Generate two random numbers
 # Print them
 # If user enters n
 # print thank you message
 # terminate
 # else
 # print invalid message

import random
while True:
  choice = input('Roll the dice?  (y/n): ').lower()
  if choice == 'y':
      dice1 = random.randint(1, 6)
      dice2 = random.randint(1, 6)
      print(f'({dice1} , {dice2})')
  elif choice == 'n':
      print('Thanks for playing!')
      break
  else:
      print('Invalid choice!')