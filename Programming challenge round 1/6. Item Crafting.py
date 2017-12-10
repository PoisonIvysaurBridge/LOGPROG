'''
6. Item Crafting
'''

strInput=input('Number of pickaxes: ')
pickax=int(strInput)
strInput=input('Number of long swords: ')
longsw=int(strInput)
strInput=input('Number of rejuvenation beads: ')
reju=int(strInput)

rejbids=reju//2

if pickax < longsw and pickax < rejbids:
    Max=pickax

elif longsw < pickax and longsw < rejbids:
    Max=longsw

elif rejbids < pickax and rejbids < longsw:
    Max=rejbids

remainPA=pickax-Max
remainLS= longsw-Max
remainRB= (rejbids-Max)*2


print("\nMaximum number of Tiamat items you can craft: ",Max)
print("Remaining pickaxes: ",remainPA)
print("Remaining long swords: ",remainLS)
print("Remaining rejuvenation beads: ",remainRB)

