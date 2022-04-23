def evenNum(n):
    sum = 0
    even_list = []
    for i in range(0, n, 2):
        even_list.append(i)
        sum += i
    return (sum, even_list)
print("Enter the number")
n = int(input())
print(evenNum(n))
