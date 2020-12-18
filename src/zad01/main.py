import os


class File:
    def read(self, path):
        with open(path, "r") as file:
            return file.read()

    def edit(self, path, content):
        with open(path, "w") as file:
            file.write(content)

    def remove(self, path):
        if os.path.exists(path):
            os.remove(path)
