#2) გამოიყენეთ and და or ოპერატორები, რათა შეამოწმოთ, თუ მოცემული ციფრები არიან 10-ზე მეტი ან 50-ზე ნაკლები.

num = int(input("Enter Number: "))

if (num > 10 and num < 50):
    print("This number is more than 10 and less than 50.")

elif num < 10:
    print("This number is less than 10.")

elif num > 50:
    print("This number is more than 50.")   

elif num == 10:
    print("This number is 10.")  

else:
    print("This number is 50.")    