main_string = input("Enter the string ", end=" ")
words = main_string.split(" ")
word_length = len(main_string.split(" "))
if(word_length <=1 ):
    print("Please enter more than one words")
else:
    for i in range(word_length):
        if(len(words[i]) <= 1):
            print("please enter the words as minimum two characters")
            break
        else:
            reverseWord = [word[::-1] for word in words]
            newString = " ".join(reverseWord)
            print(newString)
            break
