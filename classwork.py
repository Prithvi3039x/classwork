# Printing weekdays :-

# num = int(input("Enter number of day :"))

# if num == 1:
#     print("It's Sunday !!")
# elif num == 2:
#     print("It's Monday !!")
# elif num == 3:
#     print("It's Tuesday !!")
# elif num == 4:
#     print("It's Wednesday !!")
# elif num == 5:
#     print("It's Thursday !!")
# elif num == 6:
#     print("It's Friday !!")
# elif num == 7:
#     print("It's Saturday !!")
# else:
#     print("Please enter a valid number !!")


# Underage without ID

# age = 20
# has_Id = True

# if age >= 18:
#     if has_Id:
#         print("Entry Allowed !!")
#     else :
#         print("Entry not allowed !!")
# else:
#     print("Underage!!")


# Match Case

# day = int(input("Enter number of day :"))

# match day:
#     case 1:
#         print("It's Sunday !!")
#     case 2:
#         print("It's Monday !!")
#     case 3:
#         print("It's Tueday !!")
#     case 4:
#         print("It's Wednesday !!")
#     case 5:
#         print("It's Thursday !!")
#     case 6:
#         print("It's Friday !!")
#     case 7:
#         print("It's Saturday !!")
#     case _:
#         print("Please enter valid day !!")

# Even Odd

# num = int(input("Enter a number :"))

# if num % 2 == 0 :
#     print("Even Number !!")
# else:
#     print("Odd Number !!")

# result = "Even" if num % 2 == 0 else "Odd"
# print("result")


# Discount for children

# age = int(input("Enter age :"))
# price = 599

# if age < 12:
#     print(f"You have got a 10% Discount !! Price is : {price-(price/10)}")
#     # print(f"You have got a 10% Discount !! Price is :{price-(price*10/100)}")
# else :
#     print(f"Price is : {price}")


# Grading System

# score = int(input("Enter you score :"))

# if score >= 90 and score <=100: 
#     print("Grade O !!")
# elif score >= 80 and score < 90:
#     print("Grade A !!")
# elif score >= 65 and score < 80:
#     print("Grade B !!")
# elif score >= 35 and score < 65:
#     print("Grade C !!")
# elif score < 35:
#     print("You have failed the exam !!")
# else :
#     print("Wrong input !!")

num = int(input("Enter a number : "))

if num > 0:
    print(f"{num} is a Positive Number")
elif num < 0:
    print(f"{num} is a Negative Number")
else:
    print("You have entered zero !!")