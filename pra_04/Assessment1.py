import csv
csvFile=open("songs.csv", "r")
reader = csv.reader(csvFile)
content = []
for line in csvFile:
    print(line)

def main():
    print('Songs To Learn 1.0 - by Jianjian Chen Ward 7 songs loaded')
    choseMenu = str(input('Menu:''\nL - List songs''\nA - Add new song''\nC - Complete a song''\nQ - Quit')).upper()
    judgemenu(choseMenu)
    if choseMenu == 'L':
        csvFile = open("songs.csv", "r")
        reader = csv.reader(csvFile)
        column0 = [row[0] for row in reader]
        csvFile = open("songs.csv", "r")
        reader = csv.reader(csvFile)
        column1 = [row[1] for row in reader]


        for x,y in zip(column0,column1):
            print("Name: {}, Singer: {}".format(x,y))







def judgemenu(choseMenu):
    while choseMenu != 'L' and choseMenu != 'A' and choseMenu != 'C' and choseMenu != 'Q':
        print('Invalid menu choice.')
        choseMenu = str(input('Menu:''\nL - List songs''\nA - Add new song''\nC - Complete a song''\nQ - Quit')).upper()




main()