# Module 4 Lab-4
# Jessie Perez
# 9/18/2024
# this code determines the bonus a store and empoyees will recive based on monthly sales amount and increase in sales percentage

# declare local variables
monthlySales = 0  
storeAmount = 0  
empAmount = 0  
salesIncrease = 0  
prompt = 'enter monthly sales $'

    

# This code gets the monthly sales
monthlySales = float(input('enter monthly sales $'))

# This code determines the store bonus

if monthlySales >= 110000:
	storeAmount = 6000
elif monthlySales >= 100000:
	storeAmount = 5000
elif monthlySales >= 90000:
	storeAmount = 4000
elif monthlySales >= 80000:
	storeAmount = 3000
else:
	storeAmount = 0
	



# This code gets the percent of increase in sales
salesIncrease = float(input('enter percent of increase sales:'))
salesIncrease = salesIncrease / 100


# This code determines the employee bonus
if salesIncrease >= 0.05:
	empAmount = 75
elif salesIncrease >= 0.04:
	empAmount = 50
elif salesIncrease >= 0.03:
	empAmount = 40
else:
	empAmount = 0

# This code prints the bonus information
print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)
if (storeAmount == 6000 )and(empAmount == 75):
	print('Congrats! You have reached the highest bonus amounts possible! ')