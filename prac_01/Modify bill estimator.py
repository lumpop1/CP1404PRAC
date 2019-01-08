TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
chose_Tariff=input('Which tariff?11 or 31?')
daily_kWh=float(input('enter daily kWh'))
num_Days=float(input('enter number of billing days'))
while chose_Tariff != '11' and chose_Tariff != '31':
    print('error')
    chose_Tariff = input('Which tariff?11 or 31?')
else:
    if chose_Tariff != '11':
        chose_Tariff=0.136928
    else:
        chose_Tariff = 0.244618
total =(daily_kWh * num_Days) * chose_Tariff

print("Electricity bill estimator 2.0")
print('enter daily kWh',daily_kWh)
print('enter number of billing days',num_Days)
print('Estimated bill: $',total)
