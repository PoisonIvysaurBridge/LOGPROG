'''Exercise 3: Peso to Dollar converter
given exchange rate'''
Peso=input('Please enter amount in Peso(s): ')
Peso=float(Peso)
ExRate=input('Please enter exchange rate in decimal(not in percent): ')
ExRate=float(ExRate)
Dollar=Peso*ExRate
print(str(Peso),'Peso(s) to Dollar(s) is', Dollar,"Dollars")
