filedata = open("demofile.txt", "a")
print("Enter the 2 line of sentence to insert into the file")
sentence1 = input()
sentence2 = input()
filedata.write(sentence1)
filedata.write(sentence2)
filedata.close()

file = open("demofile.txt", "r")
print(file.read())
