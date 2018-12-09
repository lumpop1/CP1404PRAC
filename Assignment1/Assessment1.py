import csv
import pandas
csvFile=open("temp.csv", "r")
reader = csv.reader(csvFile)
content = []
for line in csvFile:
    print(line)

def main():
    Songs = pandas.read_csv('temp.csv')
    print("Songs To Learn 1.0 - by Jianjian Chen \n", len(Songs.index), "Ward songs loaded")
    choseMenu = str(input('Menu:''\nL - List songs''\nA - Add new song''\nC - Complete a song''\nQ - Quit')).upper()
    judgemenu(choseMenu)



def judgemenu(choseMenu):
    while choseMenu != 'L' and choseMenu != 'A' and choseMenu != 'C' and choseMenu != 'Q':
        print('Invalid menu choice.')
        choseMenu = str(input('Menu:''\nL - List songs''\nA - Add new song''\nC - Complete a song''\nQ - Quit')).upper()
    while choseMenu == 'L':
        import pandas
        list1 = pandas.read_csv('temp.csv',usecols=[0,1,2,3])
        list1['Learned'].fillna((' '),inplace=True)
        print(list1)
        print(len(list1[list1['Learned']==' ']),'songs learned',len(list1[list1['Learned']=='*']),'songs still to learn')
        choseMenu = str(input('Menu:''\nL - List songs''\nA - Add new song''\nC - Complete a song''\nQ - Quit')).upper()
        judgemenu(choseMenu)
    while choseMenu == 'A':
        import csv
        title = input("Title: ")
        while title == "":
            title = input("Input can not be blank\nTitle: ")
        artist = input("Artist: ")
        while artist == "":
            artist = input("Input can not be blank\nArtist: ")
        year = input("Year: ")
        while year.isalpha():
            print("Invalid input; enter a valid number")
            year = input("Year: ")
        while int(year) <= 0:
            print("Number must be >= 0")
            year = input("Year: ")
        required = "n"
        Learned = '*'
        if Learned=='*':
            required='y'
        New_song = [Learned,title, artist, year, required]
        Songs_csv = open("temp.csv", "a", newline="")
        writer = csv.writer(Songs_csv)
        writer.writerow(New_song)
        Songs_csv.close()
        print(title, "by", artist, "(", year, ") added to song list")
        choseMenu = str(input('Menu:''\nL - List songs''\nA - Add new song''\nC - Complete a song''\nQ - Quit')).upper()
        judgemenu(choseMenu)
    while choseMenu == 'C':
        import  pandas
        df = pandas.read_csv('temp.csv')
        if '*' in list(df['Learned']):
            chose_num = input('Enter the number of a song to mark as learned')
            if chose_num:
                print('Input can not be blank,try again')
                chose_num = int(input('Enter the number of a song to mark as learned'))
            elif chose_num < 0:
                print('Input can not be blank,try again')
                chose_num = int(input('Enter the number of a song to mark as learned'))
            df.iat[chose_num,0]=' '
            df.to_csv("temp.csv", index=False)
            print(df.iat[chose_num,1],'learned')
        else:
            print('No more songs to learn')
        choseMenu = str(input('Menu:''\nL - List songs''\nA - Add new song''\nC - Complete a song''\nQ - Quit')).upper()
        judgemenu(choseMenu)

    while choseMenu=='Q':
        import pandas
        Songs = pandas.read_csv('temp.csv')
        print(len(Songs.index), "saved to temp.csv"'\nHave a nice day :)')
        exit()


main()