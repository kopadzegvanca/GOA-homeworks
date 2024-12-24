#2) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ მხოლოდ ლუწი რიცხვების ჯამი, გამოიყენეთ for loop


num = int(input("enter number: "))

evens_sum = 0

for i in range(num):
    if i % 2 == 0:
        evens_sum = evens_sum + i

print(evens_sum)