#10) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი ერთიდან იმ რიცხვამდე დაბეჭდავს ყველა რიცხვს

def num():
    num = int(input("enter a number: "))
    for i in range(num + 1):
        print(i)

num()
    