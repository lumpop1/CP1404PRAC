"""Input a name and print alternate characters"""
def main():
    name = get_name()
    num = int(input("Enter the skip value"))
    print_name(name, num)

def print_name(name, num):
    print(name[::num])

def get_name():
    name = input("Enter name")
    # error check for name to be blank
    while len(name) < 1:
        name = input('Enter names')
    return name

main()


