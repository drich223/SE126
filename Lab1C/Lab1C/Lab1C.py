#Dylan Rich Lab 1C 1/13/20
def capacity():
    cap=int(input("How many people can fit in the room?"))
    return cap
def attendees():
    people=int(input("How many people are going to attend?"))
    return people
def register(x,y):
    difference=x-y
    return difference
def another():
    answer1=input("Would you like to enter a new room?")
    return answer1


answer=another()
while answer !="Y" and answer !="y" and answer !="n" and answer !="N":
    another()



