#1) გააკეთეთ სარეგისტრაციო, მომხმარებელს შემოატანიეთ სახელი და პაროლი, რეგისტრაციის შემდეგ მოხმარებელი უნდა შევიდეს ექაუნთზე, შეეკითხეთ სახელი და პაროლი მომხარებელს რათა შევიდეს ექაუნთზე სანამ მომხმარებელი არ შეიტანს იმ ინფორმაციას რაც შეიყვანა რეგისტრაციის დროს მანამ დაიბეჭდოს რომ შეტანილი ინფორმაცია არასწორია და შეეკითხოს თავიდან, ხოლო თუ მომხმარებელმა ყველაფერი სწორად შეიყვანა დაიბეჭდოს welcome

print("regiatration:")
name = input("Enter your name: ")
password = input("Enter yor password: ")

print("LogIn: ")
log_name = input("Enter you name: ")
log_password = input("Enter your password: ")

while log_name != password or log_password != password:
    print("inccorect name or password")
    log_name = input("Enter you name: ")
    log_password = input("Enter your password: ")

print("welcome")