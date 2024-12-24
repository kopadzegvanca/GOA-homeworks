#4) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ მხოლოდ 5 ის ჯერადი რიცხვების ჯამი ცალკე და მხოლოდ 3ის ჯერადი რიცხვების ჯამი ცალკე, გამოიყენეთ while loop


num = int(input("enter number: "))

sum1 = 0
sum2 = 0

for i in range(num):
    if i % 5 == 0:
        sum1 = sum1 + i
    if i % 3 == 0:
        sum2 = sum2 + i

print(sum1)
print(sum2)
