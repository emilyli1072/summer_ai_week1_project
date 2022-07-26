# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
        self.list_of_IDs = []                         # you can save objects of people on the network in this list
        self.ID_to_people = {}
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass
    def sign_in(self):
        id = None
        while (id not in self.list_of_IDs):
            id = input("Enter your ID: ")
        pw = None
        while (pw != self.ID_to_people[id].password):
            pw = input("Enter your password: ")
        i = self.list_of_IDs.index(id)
        for i in self.list_of_people:
            if i.id == id:
                return i
 
    def  create_account(self):
        #print(self.list_of_IDs, 1)
        id = input("Enter your ID: ")
        while (id in self.list_of_IDs):#repeat until the ID is not taken
            print("Invalid ID")
            id = input("Enter your ID: ")
        password = input("Create password: ")
        while (len(password)<8):
            print("Password is too short. Must be at least 8 characters.")
            password = input("Create password: ")
        print("Creating ...")
        user = Person(id, password)
        self.list_of_people.append(user)
        self.list_of_IDs.append(id)
        self.ID_to_people[id] = user
        return
        #implement function that creates account here


class Person:
    def __init__(self, name, password):
        self.id = name
        self.password = password
        self.friendlist = []
        self.inbox = {}#inbox is a dictionary that takes a Person object: a list of messages
    def edit(self, ai_social_network):
        oldID = self.id
        id = input("Enter your new ID: ")
        while (id in ai_social_network.list_of_IDs):
            print("Invalid ID")
            id = input("Enter your new ID: ")
        self.id = id
        password = input("Create new password: ")
        while (len(password)<8):
            print("Password is too short. Must be at least 8 characters.")
            password = input("Create new password: ")
        self.password = password
        print("Updating...")
        ai_social_network.list_of_IDs.remove(oldID)#update the list of IDS
        ai_social_network.list_of_IDs.append(self.id)
        del ai_social_network.ID_to_people[oldID]#update the ID:person object dictionary
        ai_social_network.ID_to_people[self.id] = self
    def show_friends(self):
        for i in self.friendlist:
            print(i.id)
        print()
    def add_friend(self, person_ID, ai_social_network):
        if person_ID not in ai_social_network.list_of_IDs:
            print("Does not exist.")
            return
        self.friendlist.append(ai_social_network.ID_to_people[person_ID])
        ai_social_network.ID_to_people[person_ID].friendlist.append(self)
    def block_friend(self, person_ID, ai_social_network):
        if (ai_social_network.ID_to_people[person_ID] in self.friendlist):
            self.friendlist.remove(ai_social_network.ID_to_people[person_ID])
            print("Removed")
        else:
            print("Not your friend.")
    def check_messages(self, person_ID, ai_social_network):
        person = ai_social_network.ID_to_people[person_ID]
        messages = self.inbox[person]
        for i in range(0, len(messages)):
            print(messages[i])
        print()
    def send_message(self, person_ID, message, ai_social_network):
        print(person_ID)
        if (self not in ai_social_network.ID_to_people[person_ID].friendlist or ai_social_network.ID_to_people[person_ID] not in self.friendlist):
            print("You are not friends with that person.")
            return
        else:
            if  self in ai_social_network.ID_to_people[person_ID].inbox:#if previously sent messages before
               ai_social_network.ID_to_people[person_ID].inbox[self].append(message)
            else: 
                ai_social_network.ID_to_people[person_ID].inbox[self]=[message]
        #implement sending message to friend here

