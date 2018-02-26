class ATM:
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name

    def withdraw(self, request):
        print("Welcome to " + str(self.bank_name))
        print("Current balance = " + str(self.balance))

        allowed_papers = [100, 50, 10, 5, 1]

        if request > self.balance:
            print "Sorry, Can't give you all this money !!"

        elif request < 0:
            print "Must be more than 0 ,TRY more plz!"

        else:
            reminder = self.balance - request

            for x in allowed_papers:
                while request >= x:
                    print "Give:", x
                    request -= x

            return reminder


balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
print
atm1.withdraw(800)
print
atm2.withdraw(100)
print
atm2.withdraw(2000)


###################################################





