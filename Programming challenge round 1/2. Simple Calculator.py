'''
2. Simple Calculator
'''

strInput=input('Input the first number: ')
first= float(strInput)
strInput=input('Input the operation: ')
operax=strInput
strInput=input('Input the second number: ')
second= float(strInput)

if operax=="+":
    ans=first+second
    print('the answer is',ans)

elif operax=="-":
    ans=first-second
    print('the answer is',ans)

elif operax=="x":
    ans=first*second
    print('the answer is',ans)

elif operax=="/":
    if second==0:
        print('The answer is undefined')
    else:
        ans=first/second
        print('The answer is',ans)
