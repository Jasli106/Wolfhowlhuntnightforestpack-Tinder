#INSTRUCTIONS: Press the big green run button at the top of the screen. If you get a message that says something like "Repl.it: Updating package configuration", wait for that process to finish. You can stop and rerun the program to get rid of whatever text pops up from that.

import random
import math
import replit

#Variables
words = ["wolf", "pack", "howl", "hunt", "night", "forest"]
names = []
tempRemove = []

#Functions
def generateString():
    numbers = random.sample([0, 1, 2, 3, 4, 5], 6)
    string = f"{words[numbers[0]]}{words[numbers[1]]}: {words[numbers[2]]}{words[numbers[3]]} of the {words[numbers[4]]}{words[numbers[5]]}"
    if string not in names:
        names.append(string)
        return

def prompt():
  choice = ""
  while (not choice == 'a') and (not choice == 'd'):
    choice = input("")
    if choice=='a':
      return 1
    elif choice=='d':
      return 2

def bracketTime():
  tempRemove = []
  for i in range(0, int(len(names)/2)):
    print("Press a for option 1, d for option 2\n")
    print(f"{names[i*2]}   OR   {names[i*2+1]}\n")
    choice = prompt()
    if choice == 1:
      tempRemove.append(names[i*2+1])
    elif choice == 2:
      tempRemove.append(names[i*2]) 
    replit.clear()
  for name in tempRemove:
    names.remove(name)


#Main program execution
while len(names) < math.factorial(len(words)):
    generateString()

while(len(names) > 1): 
  bracketTime()

print(f"\n{names[0]}")
