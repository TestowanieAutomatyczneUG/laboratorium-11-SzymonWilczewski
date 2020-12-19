class FriendShips:
    def __init__(self):
        self.friendships = {}

    def makeFriends(self, person1, person2):
        if type(person1) != str or type(person2) != str:
            raise TypeError("Person is not a string")
        self.addFriend(person1, person2)
        self.addFriend(person2, person1)

    def getFriendsList(self, person):
        if type(person) != str:
            raise TypeError("Person is not a string")
        if person not in self.friendships:
            raise KeyError("Person doesn't exist")
        return self.friendships[person]

    def areFriends(self, person1, person2):
        if type(person1) != str or type(person2) != str:
            raise TypeError("Person is not a string")
        if person1 not in self.friendships:
            raise KeyError("Person doesn't exist")
        if person2 in self.friendships[person1]:
            return True
        return False

    def addFriend(self, person, friend):
        if type(person) != str or type(friend) != str:
            raise TypeError("Person is not a string")
        if person not in self.friendships:
            self.friendships[person] = [friend]
        else:
            self.friendships[person].append(friend)
