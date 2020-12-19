class Note:
    def __init__(self, name, note):
        if name is None:
            raise TypeError
        if name == "":
            raise ValueError
        if note < 2 or note > 6:
            raise ValueError

        self.name = name
        self.note = note

    def get_name(self):
        return self.name

    def get_note(self):
        return self.note
