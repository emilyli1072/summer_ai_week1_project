# You can implement user interface functions here.

def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. Block a friend")
    print("4. View all my friends")
    print("5. View a friend's messages")
    print("6. Send message to friend")
    print("7. Sign out and go back")
    return input("Please Choose a number: ")
