import unittest
from unittest import mock
from unittest.mock import *

from src.zad01.main import File


class FileTest(unittest.TestCase):

    def setUp(self):
        self.file = File()

    def test_read(self):
        path = "file.txt"
        mock = mock_open(read_data="text")
        with patch("builtins.open", mock):
            self.assertEqual("text", self.file.read(path))

    def test_edit(self):
        path = "file.txt"
        mock = mock_open(read_data="text")
        with patch("builtins.open", mock):
            self.file.edit(path, "different text")
        mock.assert_called_once_with(path, "w")

    @mock.patch('src.zad01.main.os.path')
    @mock.patch('src.zad01.main.os')
    def test_remove(self, mock_os, mock_path):
        path = "file.txt"
        mock_path.exists.return_value = True
        self.file.remove(path)
        mock_os.remove.assert_called_with(path)

    def tearDown(self):
        self.file = None
