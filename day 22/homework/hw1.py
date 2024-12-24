#1) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან მომხმარებლის შემოტანილ რიცხვამდე დაბეჭდეთ ყველა რიცხვის ჯამი, for loop ის გამოყენებით

num = input("Ente your number: ")

sum=0

for i in range(num):
    sum = sum + i

print(sum)

sum = sum + i 
# shemoklebuli forma
sum += i