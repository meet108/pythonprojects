class TransactionMaxAmountError(Exception):
    pass


class TransactionMaxLimitError(Exception):
    pass


class HDFCBank:
    def __init__(self):
        self.__TransactionMaxLimit = 3
        self.__TransactionMaxAmount = 20000
        self.__userTransactionLimit = 0
        self.__userTransactionAmount = 0.0

    def withdraw(self, amount):
        try:
            if amount > self.__TransactionMaxAmount:

                raise TransactionMaxAmountError

            else:
                self.__userTransactionAmount += amount

                if self.__userTransactionAmount > self.__TransactionMaxAmount:

                    self.__userTransactionAmount -= amount

                    raise TransactionMaxAmountError

                elif self.__userTransactionAmount == self.__TransactionMaxAmount:

                    print("Transaction for HDFC Bank has been done !")

                    print(
                        "Maximum Transaction Amount for HDFC Bank is {} which is complete in your Transaction!".format(
                            self.__TransactionMaxAmount))

                    exit()

                else:

                    self.__userTransactionLimit += 1

                    if self.__userTransactionLimit == self.__TransactionMaxLimit:
                        print("Transaction for HDFC Bank has been done !")

                        raise TransactionMaxLimitError
                    else:
                        print("Transaction for HDFC Bank has been done !")

        except TransactionMaxLimitError:

            print("Maximum Transaction Limit for HDFC Bank is {}".format(self.__TransactionMaxLimit))

            exit()

        except TransactionMaxAmountError:

            print("Maximum Transaction Amount for HDFC Bank is {} which is exceeded in your Transaction!".format(
                self.__TransactionMaxAmount))


class AXISBank:
    def __init__(self):
        self.__TransactionMaxLimit = 5
        self.__TransactionMaxAmount = 30000
        self.__userTransactionLimit = 0
        self.__userTransactionAmount = 0.0

    def withdraw(self, amount):

        try:

            if amount > self.__TransactionMaxAmount:
                raise TransactionMaxAmountError

            else:

                self.__userTransactionAmount += amount

                if self.__userTransactionAmount > self.__TransactionMaxAmount:

                    self.__userTransactionAmount -= amount

                    raise TransactionMaxAmountError

                elif self.__userTransactionAmount == self.__TransactionMaxAmount:

                    print("Transaction for AXIS Bank has been done !")

                    print(
                        "Maximum Transaction Amount for AXIS Bank is {} which is complete in your Transaction!".format(
                            self.__TransactionMaxAmount))

                    exit()

                else:

                    self.__userTransactionLimit += 1

                    if self.__userTransactionLimit == self.__TransactionMaxLimit:

                        print("Transaction for AXIS Bank has been done !")

                        raise TransactionMaxLimitError

                    else:
                        print("Transaction for AXIS Bank has been done !")

        except TransactionMaxLimitError:

            print("Maximum Transaction Limit for AXIS Bank is {}".format(self.__TransactionMaxLimit))

            exit()

        except TransactionMaxAmountError:

            print("Maximum Transaction Amount for AXIS Bank is {} which is exceeded in your Transaction!".format(
                self.__TransactionMaxAmount))


def transaction(objectBank, amount):
    objectBank.withdraw(amount)


class ATM:
    def __init__(self):

        self.bankObject = None

        self.bankName = input("Press 'h' or 'H' for HDFC & 'a' or 'A' for AXIS:")

        if self.bankName == 'A' or self.bankName == 'a':

            self.bankObject = AXISBank()
            self.inputAmount()

        elif self.bankName == 'h' or self.bankName == 'H':

            self.objectHDFCBank = HDFCBank()
            self.bankObject = self.objectHDFCBank
            self.inputAmount()

    def inputAmount(self):

        amount = float(input("Enter Amount:"))

        transaction(self.bankObject, amount)

        choice = input("Press 'Y' or 'y' to continue Transaction & 'N' or 'n' to Terminate:")

        if choice == 'Y' or choice == 'y':

            self.inputAmount()

        elif choice == 'N' or choice == 'n':

            exit()


objectATM = ATM()
