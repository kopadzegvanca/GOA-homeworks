#3)შეამოწმეთ, არის თუ არა მოცემული ციფრი დადებითი ან ნული, თუმცა არ არის უარყოფითი.

num = int(input("Enter Your Namber:"))

if num == 0:
    print("number is zero")

elif num > 0:
    print("number is positive")

elif num < 0:
    print("number is negative")