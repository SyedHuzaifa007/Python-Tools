def note():
    note = input("Write Your Notes Here..... ")
    with open("note.txt", "a") as file:
        file.write(note)
