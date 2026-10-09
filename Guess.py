# import random
# print("### GUESS THE NUMBER BETWEEN 1 TO 20  ###")

# a = random.randint(1,20)
# b = int(input("Enter your guess: "))



# while True:
#     if a == b:
#         print("Yayy you guessed it!!")
#         break
#     if b < a:
#         print("GREATER")
#     else:
#         print("LESSER")
#     b = int(input("Enter your guess: "))




#create a list of numbers and strings accept the values from user separate the list from the maximum number display the names in descending order

list = input("Enter name and numbers: ").split()

names = []
for i in list:
    names.append(i)

print(names)

print(names.sort(reverse=True))