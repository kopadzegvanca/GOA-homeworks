#classwork
#2) მომხამრებელს შემოატანინეთ ახლანდელი ასაკი ასევე შემოატანინეთ ახლანდელი წელი, შემდეგ შეეკითხეთ რამდენი წლით სურს დროში მოგზაურობა შემდეგ კი დაბეჭდეთ ერთ გრძელ წინადადებაში რამდენი წლის იქნება მომხარებელი დროში მოგზაურობის შემდეგ და რომელი წელიწადი იქნება დროში მოგზაურობის შემდეგ


# age = int(input("რამდენი წლის ხართ: "))
# year = int(input("ამჟამინდელი წელი: "))
# num = int(input("რამდენი წლით გსურთ დროში მოგზაურობა: "))

# print(str(num) + " წლის შემდეგ თქვენ იქნებით " + str(age + num) +  " წლის," + " და იქნებით " + str(year + num) + " წელიწადში.")


current_age = int(input("Enter Your Age: "))
current_year = int(input("Enter Current Year: "))

time_travel = int(input("For how many years, do you want to travel in time: "))


print("After time travel you will be " + str(current_age + time_travel) + " years old " + " And will be in year " + str(current_year + time_travel))