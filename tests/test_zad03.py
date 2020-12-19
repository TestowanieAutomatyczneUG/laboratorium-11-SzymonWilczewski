import unittest

from src.zad03.friendships import FriendShips


class TestFriendships(unittest.TestCase):
    def setUp(self):
        self.friendships = FriendShips()

    def test_make_friends(self):
        self.friendships.makeFriends("Kowalski", "Nowak")
        self.assertEqual(self.friendships.friendships, {"Kowalski": ["Nowak"], "Nowak": ["Kowalski"]})

    def test_get_friend_list(self):
        self.friendships.makeFriends("Kowalski", "Nowak")
        self.friendships.makeFriends("Nowak", "Wiśniewski")
        self.assertEqual(self.friendships.getFriendsList("Nowak"), ["Kowalski", "Wiśniewski"])

    def test_are_friends(self):
        self.friendships.makeFriends("Kowalski", "Nowak")
        self.assertTrue(self.friendships.areFriends("Kowalski", "Nowak"))

    def test_add_friend(self):
        self.friendships.addFriend("Kowalski", "Nowak")
        self.friendships.addFriend("Kowalski", "Wiśniewski")
        self.assertEqual(self.friendships.friendships, {"Kowalski": ["Nowak", "Wiśniewski"]})

    def test_make_friends_type_error(self):
        with self.assertRaisesRegex(TypeError, "Person is not a string"):
            self.friendships.makeFriends("Kowalski", [])

    def test_get_friend_list_type_error(self):
        with self.assertRaisesRegex(TypeError, "Person is not a string"):
            self.friendships.getFriendsList(True)

    def test_get_friend_list_key_error(self):
        with self.assertRaisesRegex(KeyError, "Person doesn't exist"):
            self.friendships.getFriendsList("Kowalski")

    def test_are_friends_type_error(self):
        with self.assertRaisesRegex(TypeError, "Person is not a string"):
            self.friendships.areFriends({}, "Nowak")

    def test_are_friends_key_error(self):
        with self.assertRaisesRegex(KeyError, "Person doesn't exist"):
            self.friendships.areFriends("Kowalski", "Nowak")

    def test_add_friend_type_error(self):
        with self.assertRaisesRegex(TypeError, "Person is not a string"):
            self.friendships.makeFriends(True, [])

    def tearDown(self):
        self.friendships = None
