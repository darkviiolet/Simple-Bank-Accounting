from Bank import Bank

if __name__ == "__main__":
    Bank_object = Bank()
    print("Welcome to my Bank")
    print("1.Login")
    print("2.Creata a new Account")
    user = int(input("Make decision: "))

    if user == 1:
        print("Logging in")
        name = input("Enter Name: ")
        ph = int(input("Enter Phone Number: "))
        password = input("Enter password: ")
        Bank_object.login(name, ph, password)
        while True:
            if Bank_object.loggedin:
                print("1.Add amount")
                print("2.Check Balcane")
                print("3.Tranfer amount")
                print("4.Edit profile")
                print("5.Logout")
                login_user = int(input())
                if login_user == 1:
                    print("Balance =", Bank_object.cash)
                    amount = int(input("Enter amount: "))
                    Bank_object.add_cash(amount, name)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_user == 2:
                    print("Balacne =", Bank_object.cash)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_user == 3:
                    print("Balance =", Bank_object.cash)
                    amount = int(input("Enter amount: "))
                    if amount >= 0 and amount <= Bank_object.cash:
                        name = input("Enter person name: ")
                        ph = input("Enter person phone number: ")
                        Bank_object.Tranfer_cash(amount, name, ph)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif amount < 0:
                        print("Enter please correct value of amount")

                    elif amount > Bank_object.cash:
                        print("Not enough balance")

                elif login_user == 4:
                    print("1.Password change")
                    print("2.Phone Number change")
                    edit_profile = int(input())
                    if edit_profile == 1:
                        new_passwrod = input("Enter new Password: ")
                        Bank_object.password_change(new_passwrod)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif edit_profile == 2:
                        new_ph = int(input("Enter new Phone Number: "))
                        Bank_object.ph_change(new_ph)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break

                elif login_user == 5:
                    break

    if user == 2:
        print("Creating a new  Account")
        name = input("Enter Name: ")
        ph = int(input("Enter Phone Number: "))
        password = input("Enter password: ")
        Bank_object.register(name, ph, password)
