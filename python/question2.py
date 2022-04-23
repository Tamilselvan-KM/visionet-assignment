def stringOccuranceCount(a, b):
    count_sub_string = 0
    for i in a:
        if i in b:
            count_sub_string += 1
    return count_sub_string

main_string = input()
sub_string = input()
isInput = False
if(main_string == '' or sub_string == ''):
    print("Please enter the value")
    isInput = True
    while(isInput):
        main_string = input()
        sub_string = input()
        print("No of occurances of " + sub_string +" in " + main_string +" is: ",stringOccuranceCount(main_string, sub_string))
        break
else:
    print("No of occurances of " + sub_string +" in " + main_string +" is: ",stringOccuranceCount(main_string, sub_string))
