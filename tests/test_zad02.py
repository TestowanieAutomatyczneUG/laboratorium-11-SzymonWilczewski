import unittest
from unittest.mock import *

from src.zad02.Note import Note
from src.zad02.NotesService import NotesService


class NotesServiceTest(unittest.TestCase):
    def setUp(self):
        self.notesService = NotesService()

    def test_add(self):
        self.notesService.notesStorage.add = MagicMock(side_effect=lambda note: note)
        self.assertIsInstance(self.notesService.add(Note("Adam", 4.5)), Note)

    def test_add_wrong_type_exception(self):
        self.notesService.notesStorage.add = MagicMock(
            side_effect=lambda note: note if isinstance(note, Note) else exec("raise TypeError"))
        with self.assertRaises(TypeError):
            self.notesService.add("4.5")

    def test_average_of(self):
        self.notesService.notesStorage.getAllNotesOf = MagicMock(
            side_effect=lambda name: name == "Adam" and [Note("Adam", 4.5), Note("Adam", 3.5)])
        self.assertEqual(4.0, self.notesService.averageOf("Adam"))

    def test_average_of_wrong_type_exception(self):
        self.notesService.notesStorage.getAllNotesOf = MagicMock(
            side_effect=lambda name: name == "Adam" and [Note("Adam", 4.5), Note("Adam", 3.5)] if type(
                name) == str else exec("raise TypeError"))
        with self.assertRaises(TypeError):
            self.notesService.averageOf(4.0)

    def test_clear(self):
        self.notesService.notesStorage.clear = MagicMock(return_value=[])
        self.assertEqual([], self.notesService.clear())

    def tearDown(self):
        self.notesService = None
