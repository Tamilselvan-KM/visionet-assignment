def divisibleByThree(n):
    if((n >='A' and n <='Z') or (n >='a' and n <='z')):
        print("Entered value is not numeric value please try again!")
    else:
        if(int(n)%3 == 0):
            print("Yes - number is divisible by 3")
        else:
            print("No - number is not divisible by 3")
numeric_data = input()
isInput = False
if(numeric_data == ''):
    print("Please enter the value")
    isInput = True
    while(isInput):
        numeric_data = input()
        divisibleByThree(numeric_data)
        break
else:
    divisibleByThree(numeric_data)
