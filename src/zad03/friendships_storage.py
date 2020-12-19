from src.zad03.friendships import FriendShips


class FriendShipsStorage:
    def __init__(self):
        self.friendships = FriendShips()

    def makeFriends(self, person1, person2):
        self.friendships.makeFriends(person1, person2)

    def getFriendsList(self, person):
        return self.friendships.getFriendsList(person)

    def areFriends(self, person1, person2):
        return self.friendships.areFriends(person1, person2)

    def addFriend(self, person, friend):
        self.friendships.addFriend(person, friend)
