list_words = input().split()
if not list_words:
    print("Please enter the data and try again")
else:
    new_words = []
    for i in range(len(list_words)):
        if(len(list_words[i])>5):
            if(list_words[i] not in new_words):
                new_words.append(list_words[i])
    print(new_words)
