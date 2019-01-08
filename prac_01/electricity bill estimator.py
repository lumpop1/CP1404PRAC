num = int(input('enter cents per kWh'))
num_Dailyuse = float(input('enter daily use in kWh'))
num_Day = int(input('enter the unmber of days'))

total = (num * num_Dailyuse * num_Day)/100

print('Electricity bill estimator')
print('Enter cents per kWh: ',num)
print('Enter daily use in kWh:',num_Dailyuse)
print('Enter number of billing days:',num_Day)
print('Estimated bill: $',total)