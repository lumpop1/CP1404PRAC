try:
 numerator = int(input("Enter the numerator: "))
 denominator = int(input("Enter the denominator: "))
 while denominator == 0:
     print('sorry')
     denominator = int(input("Enter the denominator: "))
 fraction = numerator / denominator
 print(fraction)
except ValueError:
 print("Numerator and denominator must be valid numbers!")

print("Finished.")

#when numerator not a number
#when denominator=0