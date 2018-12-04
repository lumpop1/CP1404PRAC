colour_NAMES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "	#faebd7", "AntiqueWhite1": "#ffefdb",
                "AntiqueWhite2": "#eedfcc",
                "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378", "aquamarine1": "#7fffd4"}
colour = input("Enter colour name: ")
while colour != "":
    if colour in colour_NAMES:
        print(colour, "is", colour_NAMES[colour])
    else:
        print("Invalid colour name")
    colour = input("Enter colour name: ")

from collections import Counter
text =input('Please type a sentence')
text_clean=filter(str.isalpha,text.lower())
counter=Counter(text_clean)
for letter,count in counter.most_common():
  print(letter,count)