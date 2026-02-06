class Diary:
    def __init__(self):
        self.create = []

    def create_entry(self):
        entry_date = input("Enter the date: ")
        content = input("Enter the content of that day: ")
        self.create.append({"date": entry_date, "content": content})
        print("entry has been created")
