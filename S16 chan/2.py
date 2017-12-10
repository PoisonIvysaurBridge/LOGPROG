ascore = int(input("What did the first team score after the 4th quarter? "))
bscore = int(input("What did the second team score after the 4th quarter? "))

if ascore > bscore:
    print("The first team won!")
elif ascore < bscore:
    print("The second team won!")
else:
    print("It's a tie!")
