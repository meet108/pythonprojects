class TransactionMaxAmountError(Exception):
    pass


class TransactionMaxLimitError(Exception):
    pass

class HDFCBANK:
    def __init__(self):
        self.__TransactionMaxLimit = 3
        self.__TransactionMaxAmount = 20000
        self.__userTransactionLimit = 0
        self.__userTransactionAmount = 0.0
    def withdraw(self,amount):
        try:
            if amount > self.__TransactionMaxAmount:
                raise TransactionMaxAmountError
            else:
                self.__userTransactionAmount += amount
                if self.__userTransactionAmount > self.__TransactionMaxAmount:
                    self.__userTransactionAmount -= amount
                    raise TransactionMaxAmountError
                elif self.__userTransactionAmount == self.__TransactionMaxAmount:
                    print("Your Transaction is done from HDFC bank")
                    print("Maximum Transaction amount is done by you.",self.__TransactionMaxAmount)
                    exit()
                else:
                    self.__userTransactionLimit += 1

                    if self.__userTransactionLimit == self.__TransactionMaxLimit:
                        print("Transaction for HDFC Bank has been done !")

                        raise TransactionMaxLimitError
                    else:
                        print("Transaction for HDFC Bank has been done !")
        except TransactionMaxLimitError:
            print("Maximum Transaction Limit",self.__TransactionMaxLimit)
            exit()
        except TransactionMaxAmountError:
            print("Maximum Transaction Amount",self.__TransactionMaxAmount)
object_HDFC = HDFCBANK()
object_HDFC.withdraw()

class AXISBANK:
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
                        print("Your Transaction is done from AXIS bank")
                        print("Maximum Transaction amount is done by you.", self.__TransactionMaxAmount)
                        exit()
                    else:
                        self.__userTransactionLimit += 1

                        if self.__userTransactionLimit == self.__TransactionMaxLimit:
                            print("Transaction for AXIS Bank has been done !")

                            raise TransactionMaxLimitError
                        else:
                            print("Transaction for AXIS Bank has been done !")
            except TransactionMaxLimitError:
                print("Maximum Transaction Limit", self.__TransactionMaxLimit)
                exit()
            except TransactionMaxAmountError:
                print("Maximum Transaction Amount", self.__TransactionMaxAmount)
object_AXIS = AXISBANK()
object_AXIS.withdraw()
class ATM:
    def __init__(self,bankname):
        self.bankname = input("Press 'h' or 'H' for HDFC & 'a' or 'A' for AXIS:")
        if self.bankName == 'H' or self.bankName == 'h':

            self.bankObject = HDFCBANK()
            self.inputAmount()

        elif self.bankName == 'A' or self.bankName == 'a':

            self.objectHDFCBank = AXISBANK()
            self.bankObject = self.objectHDFCBank
            self.inputAmount()
    def inputAmount(self):
        amount = float(input("Enter Amount:"))
        choice = input("Press 'Y' or 'y' to continue Transaction & 'N' or 'n' to Terminate:")

        if choice == 'Y' or choice == 'y':

            self.inputAmount()

        elif choice == 'N' or choice == 'n':
            print("Thank You")
            exit()



objectATM = ATM()



