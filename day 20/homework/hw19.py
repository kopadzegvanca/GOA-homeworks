#19)შეიყვანეთ რიცხვი და დაბეჭდეთ ყველა რიცხვი, რომელიც არის 3-ზე მეტია, მაგრამ 10-ზე ნაკლები.
num = int(input("enter number: "))

while num >= 3 :
    print(num)
    num +=1
    if num > 10:
        break