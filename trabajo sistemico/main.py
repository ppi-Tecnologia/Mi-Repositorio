from cuaderno import Notebook

if __name__ == '__main__':
    notebook = Notebook()
    notebook.new_note('Hello World')
    notebook.new_note('Hello World again')

    print('Printing all addresses of notes in the notebook:')
    notebook.print_note_memory_addresses()
    print('')

    print('notebook.notes[0].id: {}'.format(notebook.notes[0].id))
    print('notebook.notes[1].id: {}'.format(notebook.notes[1].id))
    print('notebook.notes[0].memo: {}'.format(notebook.notes[0].memo))
    print()

    print('Executing notebook.search(\'Hello\'):')
    print('Printing all addresses of notes in the notebook with the string \'Hello\' in memo or tag :')
    for note1 in notebook.notes:
        print(note1)
    print('')

    print("Executing notebook.modify_memo(1, 'Hi World')")
    notebook.modify_memo(1, 'Hi World')
    print('notebook.notes[1].memo: {}'.format(notebook.notes[1].memo))

    print("Executing notebook.new_note('With tag', 'Peter')")
    notebook.new_note('With tag', 'Peter')
    print('Printing all addresses of notes in the notebook:')
    notebook.print_note_memory_addresses()
    print('')

    print("Executing vars(notebook.notes[0])")
    print(vars(notebook.notes[0]))
    print()

    print("Executing print(notebook.notes[2].tag)")
    print(notebook.notes[2].tag)

    print("Executing notebook.find_note_by_id(3)")
    note1 = notebook.find_note_by_id(3)
    print(note1)
    print()

    print("Executing notebook.find_note_by_id(2)")
    note2 = notebook.find_note_by_id(2)
    print(vars(note2))
    print()

    print("Executing notebook.modify_tag(2, 'John')")
    notebook.modify_tag(2, 'John')
    print("Executing print(notebook.notes[2].tag)")
    print(notebook.notes[2].tag)
    print()
   
    print('Printing all addresses of notes in the notebook:')
    notebook.print_note_memory_addresses()
    print('')

    print("Printing all notes iterating over the notebook and using vars() for each note:")
    for note in notebook.notes:
        print(vars(note))
    print('')

    print('Printing all notes using print_notes() method:')
    notebook.print_notes()
