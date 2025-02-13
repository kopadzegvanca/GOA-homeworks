#9) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება ასაკს თუ მისი ასაკი მეტია 18 ზე უთხრას რომ სრულწლოვანია თუარადა არარის

def age():
    x = int(input("enter your age: "))
    if x >= 18:
        print("You are of legal age.")
    else:
        print("You are not of legal age.")

age()
    