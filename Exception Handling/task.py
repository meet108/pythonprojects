import re


class MinimumCharError(Exception):
    pass


class MaximumCharError(Exception):
    pass


class OneLowerCaseError(Exception):
    pass


class OneUpperCaseError(Exception):
    pass


class OneDigitError(Exception):
    pass


class OneSpecialCharError(Exception):
    pass


class LoginError(Exception):
    pass


class SignUp:
    def __init__(self, signUpFirstName, signUpLastName, signUpUserName,
                 signUpPassword):
        self.signUpFirstName = signUpFirstName
        self.signUpLastName = signUpLastName
        self.signUpUserName = signUpUserName
        self.signUpPassword = signUpPassword


class SignIn:
    def __init__(self, signUpObejct, signInUserName, signInPassword):
        self.signInUserName = signInUserName
        self.signInPassword = signInPassword
        self.signUpObejct = signUpObejct

    def loginCheck(self):

        if self.signUpObejct.signUpUserName == self.signInUserName and self.signUpObejct.signUpPassword == self.signInPassword:
            return True
        else:
            return False


class Main:
    def __init__(self):
        uppercase_regex = '[A-Z]'  # regular Expression
        lowercase_regex = '[a-z]'
        digit_regex = '[0-9]'

        print("Enter Value for SignUp:")

        signUpFirstName = input("Enter Firstname:")
        signUpLastName = input("Enter Lastname:")
        signUpUserName = input("Enter Username:")

        while True:
            try:
                digit = False
                lower = False
                upper = False
                special = False
                signUpPassword = input("Enter Password:")

                if len(signUpPassword) < 8:
                    raise MinimumCharError

                if len(signUpPassword) > 16:
                    raise MaximumCharError

                if re.findall(uppercase_regex, signUpPassword):
                    upper = True
                if not upper:
                    raise OneUpperCaseError

                if re.findall(lowercase_regex, signUpPassword):
                    lower = True
                if not lower:
                    raise OneLowerCaseError

                if re.findall(digit_regex, signUpPassword):
                    digit = True
                if not digit:
                    raise OneDigitError

                for i in signUpPassword:
                    if 33 <= ord(i) <= 47 or 58 <= ord(i) <= 64 or 91 <= ord(
                            i) <= 96 or 123 <= ord(i) <= 126:
                        special = True
                        break
                if not special:
                    raise OneSpecialCharError

                break

            except MinimumCharError:

                print("Minimum 8 characters required !")

                print()

            except MaximumCharError:

                print("Maximum 16 characters allowed !")

                print()

            except OneLowerCaseError:

                print(
                    "Password contain atleast one lower Charecter, try again!")

                print()

            except OneUpperCaseError:
                print(
                    "Password contain atleast one upper Charecter, try again!")

                print()

            except OneDigitError:

                print("Password contain atleast one Digit, try again!")

                print()

            except OneSpecialCharError:

                print(
                    "Password contain atleast one Special Character, try again!")

                print()

        try:
            signUpObejct = SignUp(signUpFirstName, signUpLastName,
                                  signUpUserName, signUpPassword)
            print("Enter Value for signin:")
            signInUserName = input("Ënter Username:")
            signInPassword = input("Enter Password:")
            signInObject = SignIn(signUpObejct, signInUserName, signInPassword)
            response_flag = signInObject.loginCheck()

            if response_flag:

                print(
                    "Welcome {} {} !".format(signUpFirstName, signUpLastName))

            else:

                raise LoginError

        except LoginError:

            print("Username or Password is incorrect !")


objectMain = Main()
