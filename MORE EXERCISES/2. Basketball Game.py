'''
2. Basketball Game
'''

strInput=input("enter 1st team's score: ")
first=int(strInput)
strInput=input("enter 2nd team's score: ")
second=int(strInput)

if first > second:
    print('first team won!')

elif second > first:
    print('second team won!')

else:
    print("It's a tie!")
