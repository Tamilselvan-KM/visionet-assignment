import csv
def total_fees(n):
    total_fee = 0
    for i in n:
        total_fee += i
    return total_fee
    
with open('students.csv')as csv_file:
    csv_reader = csv.DictReader(csv_file)
    fees = []
    for line in csv_reader:
        fees.append(int(line['Fees']))
    print("Total fees : ",total_fees(fees))
