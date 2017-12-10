'''
10. Will You Marry Me?
'''

age1=input('enter age of 1st person: ')
age1=int(age1)
age2=input('enter age of 2nd person: ')
age2=int(age2)
sex1=input('enter sex of 1st person (M/F): ')
sex2=input('enter sex of 2nd person (M/F): ')
loc=input('enter location(USA/Phil): ')

if age1 >= 18 and age2 >= 18:
    if sex1==sex2 and loc=="USA" or sex1 !=sex2:
        print('eligible for marriage')
    else:
        print('not eligible')

else:
    print('not eligible')
    
