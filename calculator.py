print("## CALCULATOR OPENED ##")


is_true = True
while is_true:
    print("Enter 1 for addition\nEnter 2 for subtractiontion\nEnter 3 for multiplication\nEnter 4 for division\nEnter 5 for factorial\nEnter exit to stop program\n")
    ch = input("Enter your choice: ")


    if ch == "5":
        a = int(input("Enter number to calculate factroial :"))
    elif ch == "exit":
        print("Calculator closed..")
        break
    else:
        a = int(input("Enter first number :"))
        b = int(input("Enter second number :"))  

    match ch:
        case "1":
            print(a+b)
        case "2":
            print(a-b)
        case "3":
            print(a*b)
        case "4":
            print(a/b)
        case "5":
            fact = 1
            for i in range(1, a + 1):
                fact = fact*i
            print(fact)
        case "exit":
            print("Calculator closed..")
            is_true = False
        case _:
            print("Invalid choice")
        
        


        
