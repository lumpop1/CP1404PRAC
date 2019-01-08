out_file=open('name.txt','w')
userName=input('Please enter your name')
print(userName,file=out_file)
out_file.close()
