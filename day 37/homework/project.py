


# def creating_accaunt():
#     print('აქაუნთის შექმნა')
#     username = input("შექმენით ახალი სახელი:")
#     password = input("შექმენით ახალი პაროლი:")
#     repeat_password=input('გაიმეორეთ პაროლი:')

#     while password!=repeat_password:
#         print('პაროლები ერთმანეთს არ ემთხვევა!')
#         repeat_password=input('გაიმეორეთ პაროლი:')

#     print('აქაუნთი წარმატებით შეიქმნა!\nთქვენი სახელია:',username,'\nთქვენი პაროლია:', password)

def creating_accaunt():
       print('აქაუნთის შექმნა')
       username = input("შექმენით ახალი სახელი:")
       password = input("შექმენით ახალი პაროლი:")
       repeat_password=input('გაიმეორეთ პაროლი:')
       while password!=repeat_password:
        print('პაროლები ერთმანეთს არ ემთხვევა!')
        repeat_password=input('გაიმეორეთ პაროლი:')
        print('აქაუნთი წარმატებით შეიქმნა!\nთქვენი სახელია:',username,'\nთქვენი პაროლია:', password)

def show_balance():
    print(f"თანხა შენს ანგარიშზე: {balance:.2f} ლარი")

def deposit():
        print('თანხის შეტანა ანგარიშზე')
        amount = float(input("რა რაოდენობის თანხის შეტანა გსურთ?: "))

        if amount < 0:
             print("ეს შეუძლებელია, სცადეთ თავიდან!")
             return 0
        else:
             return amount

def withdraw():
    print('თანხის გამოტანა ანგარიშიდან')
    amount = float(input("რა რაოდენობის თანხის გამოტანა გსურთ?: "))

    if amount > balance:
         print("ეს შეუძლებელია!")
         return 0
    elif amount < 0:
         print("ეს შეუძლებელია")
         return 0
    else:
         return amount

balance=0
is_running=True

while is_running:
    
    print('1.შექმენი აქაუნთი')
    print('2.ანგარიშზე არსებული თანხის ნახვა')
    print('3.გააკეთე დეპოზიტი')
    print('4.გამოიტანე თანხა')
    print('5.გამოსვლა')

    choice=input('ამოირჩიე (1-5): ')

    if choice=='1':
        creating_accaunt()
    elif choice=='2':
        show_balance()
    elif choice =='3':
        balance += deposit()
    elif choice=='4':
        balance -= withdraw()
    elif choice=='5':
        is_running=False
    else:
        print('აირჩიე სასურველი ვარიანტი!')


print('მადლობა ნდობისთვის!')




