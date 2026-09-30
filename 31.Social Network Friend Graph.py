class SocialNetwork:

    def __init__(self):
        self.graph = {}

    # -----------------------------
    # Add User
    # -----------------------------
    def add_user(self, user):

        if user not in self.graph:
            self.graph[user] = set()
            print(user, "added to network")
        else:
            print("User already exists")

    # -----------------------------
    # Add Friendship
    # -----------------------------
    def add_friendship(self, user1, user2):

        if user1 not in self.graph or user2 not in self.graph:
            print("Both users must exist")
            return

        self.graph[user1].add(user2)
        self.graph[user2].add(user1)

        print(user1, "and", user2, "are now friends")

    # -----------------------------
    # Show Friends
    # -----------------------------
    def show_friends(self, user):

        if user not in self.graph:
            print("User not found")
            return

        print("Friends of", user, ":")

        for friend in self.graph[user]:
            print(friend)

    # -----------------------------
    # Friend Suggestions
    # -----------------------------
    def suggest_friends(self, user):

        if user not in self.graph:
            print("User not found")
            return

        suggestions = set()

        for friend in self.graph[user]:
            suggestions |= self.graph[friend]

        suggestions -= self.graph[user]
        suggestions.discard(user)

        print("Friend Suggestions for", user, ":")

        if suggestions:
            for s in suggestions:
                print(s)
        else:
            print("No suggestions available")

    # -----------------------------
    # Show Network
    # -----------------------------
    def display_network(self):

        print("\nSocial Network Graph")

        for user in self.graph:
            print(user, "->", list(self.graph[user]))


# -----------------------------
# Main Program
# -----------------------------

def main():

    network = SocialNetwork()

    while True:

        print("\n1 Add User")
        print("2 Add Friendship")
        print("3 Show Friends")
        print("4 Friend Suggestions")
        print("5 Show Network")
        print("6 Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            user = input("Enter user name: ")
            network.add_user(user)

        elif choice == "2":

            u1 = input("User 1: ")
            u2 = input("User 2: ")

            network.add_friendship(u1, u2)

        elif choice == "3":

            user = input("Enter user: ")
            network.show_friends(user)

        elif choice == "4":

            user = input("Enter user: ")
            network.suggest_friends(user)

        elif choice == "5":

            network.display_network()

        elif choice == "6":

            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
