import datetime

class Note:
    _id = 0
    
    def __init__(self, memo='', tag=''):
        self.id = Note._id
        Note._id += 1
        self.memo = memo
        self.tag = tag
        self.creation_date = datetime.date.today()

class Notebook:
    def __init__(self):
        self.notes = []

    def new_note(self, memo, tag=''):
        self.notes.append(Note(memo, tag))

    def modify_memo(self, note_id, memo):
        note = self.find_note_by_id(note_id)
        if note:
            note.memo = memo
        else:
            print(f"Nota con id {note_id} no encontrada.")

    def modify_tag(self, note_id, tag):
        note = self.find_note_by_id(note_id)
        if note:
            note.tag = tag
        else:
            print(f"Nota con id {note_id} no encontrada.")

    def search(self, filter):
        matching_notes = []
        for note in self.notes:
            if self.match(note.memo, filter) or self.match(note.tag, filter):
                matching_notes.append(note)
        return matching_notes

    def find_note_by_id(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        print(f"Nota con id {note_id} no encontrada.")
        return None

    def print_notes(self):
        for note in self.notes:
            print("Note ID:", note.id)
            print("Memo:", note.memo)
            print("Tag:", note.tag)
            print("Creation Date:", note.creation_date)
            print()

    def match(self, note, filter):
        return filter.lower() in note.lower()

if __name__ == '__main__':
    notebook = Notebook()
    
    while True:
        print("\n¿Qué deseas hacer?")
        print("1. Agregar nueva nota")
        print("2. Modificar una nota existente")
        print("3. Buscar notas")
        print("4. Mostrar todas las notas")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            memo = input("Ingrese el mensaje de la nota: ")
            tag = input("Ingrese la etiqueta de la nota (opcional): ")
            notebook.new_note(memo, tag)
            print("Nota agregada correctamente.")
        elif opcion == '2':
            note_id = int(input("Ingrese el ID de la nota que desea modificar: "))
            memo = input("Ingrese el nuevo mensaje de la nota: ")
            notebook.modify_memo(note_id, memo)
            print("Mensaje de la nota modificado correctamente.")
        elif opcion == '3':
            filter = input("Ingrese el filtro para buscar notas: ")
            matching_notes = notebook.search(filter)
            if matching_notes:
                print("Notas encontradas:")
                for note in matching_notes:
                    print("ID:", note.id)
                    print("Memo:", note.memo)
                    print("Tag:", note.tag)
                    print("Creation Date:", note.creation_date)
                    print()
            else:
                print("No se encontraron notas que coincidan con el filtro.")
        elif opcion == '4':
            print("Todas las notas en el cuaderno:")
            notebook.print_notes()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")