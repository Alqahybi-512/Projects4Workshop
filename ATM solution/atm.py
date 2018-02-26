class ATM:
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name

    def withdraw(self, request):
        print("Welcome to " + str(self.bank_name))
        print("Current balance = " + str(self.balance))
        print "========================================="

        if request > self.balance:
            print "Sorry, Can't give you all this money !!"
            print "========================================="

        elif request < 0:
            print "Must be more than 0 ,TRY more plz!"
            print "========================================="

        else:
            self.balance -= request
            self.process_request(request)

    @staticmethod
    def process_request(request):
            allowed_papers = [100, 50, 10, 5, 1]
            for x in allowed_papers:
                while request >= x:
                    print "Give:", x
                    request -= x

            print "========================================="
            return request


balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")

atm1.withdraw(277)
atm1.withdraw(800)

atm2.withdraw(100)
atm2.withdraw(2000)


###################################################





