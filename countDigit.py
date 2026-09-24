num = int(input("Enter a number :"))
count = 0

if(num < 10):
    count = 1
elif(num == 10):
    count = 2
else:
    while num>1:
       num = num / 10
       count+=1

print(count)