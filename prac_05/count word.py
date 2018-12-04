string=input("please enter a sentence:")
string_list=string.split(" ")
word_number={}
for word in string_list:
    if word in word_number:
        word_number[word]+=1
    else:
        word_number[word]=1

d = sorted(word_number.items(), key = lambda k: k[0])
for i in d:
    print(i)


