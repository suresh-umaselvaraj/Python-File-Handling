import re
def welcome():
    print("Welcome to your dashboard")
    print("You Logged in Successfully")
    print("All Fine. Thank You")


def gainAccess(Username=None, Password=None):
    print("Welcome to Login Page")
    Username = input("Enter your Registered Email ID:")
    Password = input("Enter your Password:")

    if not len(Username or Password) < 1:

        if True:
            db = open("database.txt", "r")
            d = []
            f = []
            for i in db:
                a, b = i.split(",")
                b = b.strip()
                c = a, b
                d.append(a)
                f.append(b)
            data = dict(zip(d, f))
            # print(data)

            try:
                if data[Username]:
                    try:
                        if Password == data[Username]:
                            print("Login success!")
                            print("Hi", Username)
                            welcome()
                        else:
                            print("Incorrect password or username")
                            ret = data[Username]
                            forgotpassword(ret)
                    except:
                        print(" ")

                else:
                    print("Password or username doesn't exist. Register")
                    register()
            except:
                print("Password or username doesn't exist")
                register()
                exit()
        else:
            print("Error logging into the system")

    else:
        print("Please attempt login again")
        gainAccess()


def register(Username=None, Password1=None):
    Username = input("Register your Email ID:")
    usercheck(Username)
    checkemail(Username)
    dbusercheck(Username)
    Password1 = input("Create password:")

    db = open("database.txt", "r")
    d = []
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        c = a, b
        d.append(a)

    if (len(Password1) >= 5) and (len(Password1) <= 16):
        isAllPresent(Password1)
        db = open("database.txt", "r")

        if not Username == None:
            if len(Username) < 1:
                print("Please provide a username")
                register()
            elif Username in d:
                print("Email ID has already been Registered. Login or use new Email ID.")
                home()
            else:
                db = open("database.txt", "a")
                db.write(Username + ", " + Password1 + "\n")
                print("User created successfully!")
                print("Refresh(Rerun) & login to proceed:")

    else:
        print("Password must be 5 to 16 characters in length")


def home(option=None):
    print("Welcome, please select an option 1 or 2")
    option = input("1.Login | 2.Signup:  ")
    if option == "1":
        gainAccess()
    elif option == "2":
        register()
    else:
        print("Please enter a valid option 1 or 2 only")
        home()


def isAllPresent(str):
    # ReGex to check if a string
    # contains uppercase, lowercase
    # special character & numeric value
    regex = ("^(?=.*[a-z])(?=." +
             "*[A-Z])(?=.*\\d)" +
             "(?=.*[-+_!@#$%^&*., ?]).+$")

    # Compile the ReGex
    p = re.compile(regex)

    # If the string is empty
    # return false
    if (str == None):
        print("Password must have minimum One Uppercase, One Lowercase, Special Char and Digit")
        return

    # Print Yes if string
    # matches ReGex
    if (re.search(p, str)):
        return
    else:
        print("Password must have minimum One Uppercase, One Lowercase, Special Char and Digit")


def usercheck(str):
    regex = ("^(?=.*\\d)")
    regex1 = ("^(?=.*[-+_!@#$%^&*., ?]).+$")
    # Compile the ReGex
    p = re.compile(regex)
    q = re.compile(regex1)
    if len(str) < 1:
        print("Please provide a Valid Email ID")
        register()
    # If the string is empty
    # return false
    if (str == None):
        print("Email cannot be Empty")
        register()
        return

    if (re.search(p, str[0])):
        if (re.search(q, str[0])):
            print("Email cannot start with Digit or Special Characters.Enter Valid Email ID")
            register()
        else:
            print("Email cannot start with Digit or Special Characters.Enter Valid Email ID")
            register()
    elif (re.search(q, str[0])):
        print("Email cannot start with Digit or Special Characters.Enter Valid Email ID")
        register()
    else:
        return


def checkemail(email):
    regex2 = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}\b'

    # pass the regular expression
    # and the string into the fullmatch() method
    if (re.fullmatch(regex2, email)):
        return
    else:
        print("Invalid Email. Enter Valid Email ID")
        register()

def dbusercheck(str):

    db = open("database.txt", "r")
    e = []
    for i in db:
        a, b = i.split(",")
        b = b.strip()
        c = a, b
        e.append(a)
        if not str == None:
            if len(str) < 1:
                print("Please provide a Valid Email ID")
                register()
            if str in e:
                print("Email ID has already been Registered. Login or use new Email ID.")
                gainAccess()
                exit()

def forgotpassword(str):

    print("Forgot Password?, please select an option 1 or 2")
    option = input("1.Retrieve | 2.No-Thanks :  ")
    if option == "1":
        print("Your Password has been sent below! Try Again")
        print(str)
        gainAccess()
        exit()
    elif option == "2":
        print("Thank you")
    else:
        print("Please enter a valid option 1 or 2 only")
        home()


home()