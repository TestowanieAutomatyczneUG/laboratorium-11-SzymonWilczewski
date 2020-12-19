import unittest
from unittest.mock import *

from src.zad03.friendships_storage import FriendShipsStorage


class TestFriendShipsStorage(unittest.TestCase):
    def setUp(self):
        self.friendships_storage = FriendShipsStorage()

    def test_make_friends(self):
        self.friendships_storage.friendships.makeFriends = MagicMock()
        self.friendships_storage.makeFriends("Kowalski", "Nowak")
        self.friendships_storage.friendships.makeFriends.assert_called_once_with("Kowalski", "Nowak")

    def test_get_friends_list(self):
        self.friendships_storage.friendships.getFriendsList = MagicMock(return_value=["Kowalski", "Wiśniewski"])
        self.assertEqual(["Kowalski", "Wiśniewski"], self.friendships_storage.getFriendsList("Nowak"))

    def test_are_friends(self):
        self.friendships_storage.friendships.areFriends = MagicMock(return_value=True)
        self.assertTrue(self.friendships_storage.areFriends("Kowalski", "Nowak"))

    def test_add_friend(self):
        self.friendships_storage.friendships.addFriend = MagicMock()
        self.friendships_storage.addFriend("Kowalski", "Nowak")
        self.friendships_storage.friendships.addFriend.assert_called_with("Kowalski", "Nowak")

    def test_make_friends_type_error(self):
        self.friendships_storage.friendships.makeFriends = MagicMock(side_effect=TypeError("Person is not a string"))
        with self.assertRaisesRegex(TypeError, "Person is not a string"):
            self.friendships_storage.makeFriends("Kowalski", [])

    def test_get_friend_list_type_error(self):
        self.friendships_storage.friendships.getFriendsList = MagicMock(side_effect=TypeError("Person is not a string"))
        with self.assertRaisesRegex(TypeError, "Person is not a string"):
            self.friendships_storage.getFriendsList(True)

    def test_get_friend_list_key_error(self):
        self.friendships_storage.friendships.getFriendsList = MagicMock(side_effect=KeyError("Person doesn't exist"))
        with self.assertRaisesRegex(KeyError, "Person doesn't exist"):
            self.friendships_storage.getFriendsList("Kowalski")

    def test_are_friends_type_error(self):
        self.friendships_storage.friendships.areFriends = MagicMock(side_effect=TypeError("Person is not a string"))
        with self.assertRaisesRegex(TypeError, "Person is not a string"):
            self.friendships_storage.areFriends({}, "Nowak")

    def test_are_friends_key_error(self):
        self.friendships_storage.friendships.areFriends = MagicMock(side_effect=KeyError("Person doesn't exist"))
        with self.assertRaisesRegex(KeyError, "Person doesn't exist"):
            self.friendships_storage.areFriends("Kowalski", "Nowak")

    def test_add_friend_type_error(self):
        self.friendships_storage.friendships.addFriend = MagicMock(side_effect=TypeError("Person is not a string"))
        with self.assertRaisesRegex(TypeError, "Person is not a string"):
            self.friendships_storage.makeFriends(True, [])

    def tearDown(self):
        self.friendships_storage = None
