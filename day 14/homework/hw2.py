#2) გამოიყენეთ and და or ოპერატორები, რათა შეამოწმოთ, თუ მოცემული ციფრები არიან 10-ზე მეტი ან 50-ზე ნაკლები.

num = int(input("Enter Number:"))

if (num > 10 and num < 50):
    print("სწორია")

elif (num < 10 or num > 50):
    print("არასწორია")