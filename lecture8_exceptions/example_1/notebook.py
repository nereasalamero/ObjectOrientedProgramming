class Notebook:
    def __init__(self):
        self.__notes = []

    def add_note(self, note):
        self.__notes.append(note)

    def retrieve_notes(self, index):
        return self.__notes[index]
    
    def all_notes(self):
        return ",".join(self.__notes)