def insertNew(list, n):
    index = len(list)
    for i in range(len(list)):
        if(list[i]>n):
            index = i
            break
    list = list[:index] + [n] + list[index:]
    return list
print("Enter the input numbers separated by space")
list_num = list(map(int, input().split()))
if not list_num:
    print("Please enter the data and try again")
else:
    tuple_num = tuple(sorted(list_num))
    result = sorted(list_num)
    print(result)
    print("Enter the new number")
    input_num = int(input())
    print(insertNew(result, input_num))
