# Create a list of 10 numbers print the sum of last 4 elements of the list find out the difference between max and min element of the list insert a number in a list at sixth position this number must be 1/3rd of number stored at 4th position.

l = [12,24,21,56,31,22,74,23,12,56]

sum = 0
for i in l[:5:-1]:
    sum += i
print("The sum of last 4 elements of the list is: ", sum)
print("The difference between maximum and minimum element of list is: " ,(max(l) - min(l)) )

num = l[3] // 3
l[5] = num

print("After inserting number at 6th position list is: ",l)

print(sorted(l))