#Dylan Rich Lab1B 1/13/20
answer=input("Would you like to check a room?(y/n): ")
while answer !="Y" and answer !="y" and answer !="n" and answer !="N":
    answer = input("Would you like to check a room?(y/n): ")
while answer == "y" or answer == "Y":
    capacity = int(input("How many people can fit in the room?: "))
    planned = int(input("How many people are attending?: "))
    difference = capacity-planned
    difference2 = difference * -1
    if capacity<planned:
      print("You have too many people, you need to remove",difference2,"people.")
    else:
      print("You have enough room, you may also add",difference,"people.")
answer = input("Would you like to enter another room?(y/n): ")
while answer !="Y" and answer !="y" and answer !="n" and answer !="N":
    answer = input("Would you like to enter another room?(y/n): ")
