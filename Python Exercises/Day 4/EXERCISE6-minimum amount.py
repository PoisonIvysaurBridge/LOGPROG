'''Exercise 6
Write a program that will display the minimum number of bills and coins
that is equivalent to the given amount. Assume that the given amount is
always a non-negative integer value.
Use the following denominations: 1000, 500, 100, 20, 5, 1.'''

amount=input('Please enter amount: ')
amount=int(amount)

#1000-bill
thousand=amount//1000
n1=amount%1000

#500-bill
Five100=n1//500
n2=n1%500

#100-bill
One100=n2//100
n3=n2%100

#20-bill
Twenty=n3//20
n4=n3%20

#5-coin
Five=n4//5
n5=n4%5

#1-coin
One=n5//1
decimal=n5%1

print(int(thousand),"1000-bill\n",int(Five100),"500-bill\n",int(One100),'100-bill\n',int(Twenty),"20-bill\n",int(Five),"5-coin\n",int(One),"1-coin")
