class Bank:
    def __init__(self):
        self.client_details_list = []
        self.loggedin = False
        self.cash = 100
        self.TranferCash = False

    def register(self, name, ph, password):
        cash = self.cash
        contitions = True
        if len(str(ph)) > 8 or len(str(ph)) < 8:
            print("Invalid Phone number ! please enter 8 digit number")
            contitions = False

        if len(password) < 5 or len(password) > 18:
            print("Enter password greater than 5 and less than 18 character")
            contitions = False

        if contitions:
            print("Account created successfully")
            self.client_details_list = [name, ph, password, cash]
            with open(f"{name}.txt", "w") as f:
                for details in self.client_details_list:
                    f.write(str(details) + "\n")

    def login(self, name, ph, password):
        with open(f"{name}.txt", "r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in str(self.client_details_list):
                if str(password) in str(self.client_details_list):
                    self.loggedin = True

            if self.loggedin == True:
                print(f"{name} logged in")
                self.cash = int(self.client_details_list[3])
                self.name = name

            else:
                print("Wrong details")

    def add_cash(self, amount, name):
        if amount > 0:
            self.cash += amount
            with open(f"{name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[3]), str(self.cash)))

            print("Amount added successfully")

        else:
            print("Enter correct value of amount")

    def Tranfer_cash(self, amount, name, ph):
        with open(f"{name}.txt", "r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in self.client_details_list:
                self.TranferCash = True

        if self.TranferCash:
            total_cash = int(self.client_details_list[3]) + amount
            left_cash = self.cash - amount
            with open(f"{name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[3]), str(total_cash)))

            with open(f"{self.name}.txt", "r") as f:
                details_2 = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt", "w") as f:
                f.write(details_2.replace(str(self.client_details_list[3]), str(left_cash)))

            print("Amount Transfered Successfully to", name, "-", ph)
            print("Balacne left =", left_cash)

    def password_change(self, password):
        if len(password) < 5 or len(password) > 18:
            print("Enter password greater than 5 and less than 18 character")
        else:
            with open(f"{self.name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[2]), str(password)))
            print("new Password set up successfully")

    def ph_change(self, ph):
        if len(str(ph)) > 8 or len(str(ph)) < 8:
            print("Invalid Phone number ! please enter 8 digit number")
        else:
            with open(f"{self.name}.txt", "r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt", "w") as f:
                f.write(details.replace(str(self.client_details_list[1]), str(ph)))
            print("new Phone number set up successfully")

