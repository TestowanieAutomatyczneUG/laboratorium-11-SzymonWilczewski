from src.zad02.NotesStorage import NotesStorage


class NotesService:
    def __init__(self):
        self.notesStorage = NotesStorage()

    def add(self, note):
        return self.notesStorage.add(note)

    def averageOf(self, name):
        notes = self.notesStorage.getAllNotesOf(name)
        return sum(map(lambda note: note.get_note(), notes)) / len(notes)

    def clear(self):
        return self.notesStorage.clear()
