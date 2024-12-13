#18)შეიყვანეთ რიცხვი და გამოიყენეთ while ციკლი, რომ შეამოწმოთ, არის თუ არა რიცხვი დადებითი.

num = int(input("enter number: "))

while num > 0:
    print("positive")
    break

while num < 0:
    print("negative")
    break

while num == 0:
    print("0")
    break