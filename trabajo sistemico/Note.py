class Note:
    def __init__(self, memo, tag, note_id):
        self.memo = memo
        self.tag = tag
        self.note_id = note_id

    def match(self, filtro):
        return filtro in self.memo or filtro in self.tag