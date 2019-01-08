from pra_6.Car import Car

def main():
    """Demo test code to show how to use car class."""
    limo=Car(100, 'My Limousine')
    limo.add_fuel(20)
    print("fuel =", limo.fuel)
    limo.drive(115)
    print("odo =", limo.odometer)
    print(limo)

    print("Car {}, {}".format(limo.fuel, limo.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=limo))


main()