class Notebook:
    def __init__(self):
        self.notes = []
        self.current_id = 0

    def new_note(self, memo, tag):
        self.notes.append(Note(memo, tag, self.current_id))
        self.current_id += 1

    def modify_memo(self, note_id, memo):
        for note in self.notes:
            if note.note_id == note_id:
                note.memo = memo
                break

    def modify_tag(self, note_id, tag):
        for note in self.notes:
            if note.note_id == note_id:
                note.tag = tag
                break

    def find_note_by_id(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                return note
        print("Nota no encontrada.")
        return None

    def search(self, filtro):
        return [note for note in self.notes if note.match(filtro)]

    def print_notes(self):
        for note in self.notes:
            print(vars(note))

class Note:
    def __init__(self, memo, tag, note_id):
        self.memo = memo
        self.tag = tag
        self.note_id = note_id

    def match(self, filtro):
        return filtro in self.memo or filtro in self.tag