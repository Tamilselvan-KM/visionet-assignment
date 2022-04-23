print("Enter the input string separated by space")
list_str = input().split()
count_search_string = 0
if not list_str:
    print("Please enter the data and try again")
else:
    print("Enter the input search string")
    search_str = input()
    for i in list_str:
        if i == search_str:
            count_search_string += 1
    print("No of occurances of "+ search_str +" is ",count_search_string)
