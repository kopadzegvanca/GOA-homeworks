#7) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი დაბეჭდავს ეს რიცხვი ლუწია თუ კენტი

def even_odd():
    num = int(input("enter a number: "))
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

even_odd()
  