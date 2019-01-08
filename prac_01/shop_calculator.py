num = int(input('enter number of items '))
while num < 0:
    print("please try again")
    num = int(input('enter number of items '))
total=0.0
for i in range(0,num):
    price=float(input('enter price of items'))
    total+=price
    print('price= ',price,'total= ',total)

if (total >= 100):
    total = 0.9 * total
print('total price is',total)
