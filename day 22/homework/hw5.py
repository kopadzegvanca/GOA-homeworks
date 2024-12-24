# 5) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ ყველა რიცხვის ნამრავლი

num = int(input("Enter your number: "))

sum = 0

for i in range(num):
    sum *= i

print(sum)