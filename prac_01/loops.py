for i in range(1, 21, 2):
 print(i, end=' ')
print()

for i in range(0, 101, 10):
 print(i, end=' ')
print()

for i in range(20, 0, -1):
 print(i, end=' ')
print()

for i in range(1, 10, 4):
    print(i, i * 2, end=" ")

try:
    x = int("zero")
    print(10 / x)
except ZeroDivisionError:
    print("div")
except NameError:
    print("name")
except ValueError:
    print("value")
except:
    print("other")

text = "Enjoy the test"
result = text.strip().split()[0]

x = str(int('1.0'))
x[-1] = '2'

x = str(1.0)
x [ - 1 ] = '2'