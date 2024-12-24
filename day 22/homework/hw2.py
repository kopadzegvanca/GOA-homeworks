#2) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ მხოლოდ ლუწი რიცხვების ჯამი, გამოიყენეთ for loop

num =int(input("Ente your number: "))

sum=0

for i in range(1 , num + 1):
    sum += i

print(sum/num)
