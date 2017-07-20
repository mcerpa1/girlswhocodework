class User:
    # Define the fields and methods for your object here.
    def __init__(self, newUsername, newUserID):
        self.username = newUsername
        self.userID = newUserID
        self.friends = []

    def getUserName(self):
        return self.username

    def getUserID(self):
        return self.userID

    def getFriends(self):
        return self.friends

    def addFriends(self, friendID):
        self.friends.append(friendID)




class Network:
    # Define the fields and methods for your object here.
    def __init__(self):
        self.users = []

    def numUsers(self):
        return len(self.users)

    def addUser(self, username):
        userID = len(self.users)
        self.users.append(User(username,userID))

    def getUserID(self, username):
        for user in self.users:
            if username == user.getUserName():
                user_ID = user.getUserID()
        return user_ID


    def addConnection(self, user1, user2):
        user1_ID = self.getUserID(user1)
        user2_ID = self.getUserID(user2)

        user1 = self.users[user1_ID]
        user2 = self.users[user2_ID]

        self.users[user2_ID].addFriends(user1_ID)
        self.users[user1_ID].addFriends(user2_ID)

    def printUsers(self):
        print("This is the Network")
        for user in self.users:
            print("\tUser {}: {}".format(user.getUserID(), user.getUserName()))

    def printConnections(self, username):
        user = self.users[self.getUserID(username)]
        connections = user.getFriends(ra)
        print("\t{}'s connections".format(user.getUserName()))
        for friendID in connections:
            friend=self.users[friendID]
            print("\t{}".format(friend.getUserName()))

def main():
    # Define the program flow for your user interface here.
    mynetwork = Network()
    done = False
    while not done:
        action = input("\nWhat would you like to do ? Add a user(u), Add a connections(c), Print Friend List (f), Print User (p) Exit (e)")
        if action == "u":
            username = input("What username?")
            mynetwork.addUser(username)
        elif action == "c":
            if mynetwork.numUsers()<2:
                print("ERROR")
                continue
            else:
                user1 = input("First User?")
                user2 = input("Second User?")
            mynetwork.addConnection(user1,user2)
        elif action == "f":
            user = input("What user?")
            mynetwork.printConnections(user)
        elif action == "p":
            mynetwork.printUsers()
        elif action == "e":
            print("BYEEEEEEEEEEE!")
            done = True
        else:
            print("UHHH...WHATS WRONG WITH YOU?")

# Runs your program.
if __name__ == '__main__':
    main()
