#3) მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ კი დაბეჭდეთ ერთიდან ამ რიცხვამდე მხოლოდ ლუწი რიცხვების ჯამი ცალკე და მხოლოდ კენტი რიცვხების ჯამი ცალკე, გამოიყენეთ for loop

num = int(input("enter number: "))

evens_sum = 0
odds_sum = 0

for i in range(num):
    if i % 2 == 0:
        evens_sum = evens_sum + i
    else:
        odds_sum = odds_sum + i

print(evens_sum)
print(odds_sum)
