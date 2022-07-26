#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui



def mainMenu():
    print("")
    print("1. Create a new account")
    print("2. Manage my account")
    print("3. Quit")
    print("********************************************************")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. View all my messages")
    print("5. <- Go back ")
    return input("Please Choose a number: ")


#Create instance of main social network object
ai_social_network = SocialNetwork()
user = None
#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()

        elif choice == "2":
            user = ai_social_network.sign_in()#sign into the account each time
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                if inner_menu_choice == "7":
                    break
                elif inner_menu_choice == "1":
                   user.edit(ai_social_network)
                elif inner_menu_choice == "2":
                    friend = input("Enter your friend's ID: ")
                    user.add_friend(friend, ai_social_network)
                elif inner_menu_choice == "3":
                    friend = input("Enter the ID that you'd like to block: ")
                    user.block_friend(friend, ai_social_network)
                elif inner_menu_choice == "5":
                    messages = input("Whose message would you like to see? (Enter their ID)")
                    user.check_messages(messages, ai_social_network)
                elif inner_menu_choice == "4":
                    user.show_friends()
                elif inner_menu_choice == "6":
                    friend = input("Who do you want to send it to? (Enter their ID)")
                    message = input("What do you want to say:")
                    user.send_message(friend, message, ai_social_network)

                inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            print("Thank you for visiting. Goodbye3")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
