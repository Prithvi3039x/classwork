lst = input("Enter numbers and names: ").split()

# lst = ['10', 'amit', '99', 'rahul']

max_num = 0
names = []

for x in lst:
    if x.isdigit():
        num = int(x)
        if num > max_num:
            max_num = num
    else:
        names.append(x)

names.sort(reverse=True)

print("Same List:", lst)
print("Maximum Number:", max_num)
print("Names Descending:", names)