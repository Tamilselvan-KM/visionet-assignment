data_dict = {1:"one", 2:"two", 3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten"}
print("Enter the Number:")
num = input()
if num == '':
    print("Please enter the data and try again")
elif((num >='A' and num <='Z') or (num >='a' and num <='z')):
    print("Entered value is not numeric value please try again!")
else:
    data = int(num)
    if(data < 1 or data >10):
        print("Please entered the value between 1 to 10")
    else:
        print(data ," : ",data_dict[data])
