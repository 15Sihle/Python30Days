class Diary:
    def __init__(self):
        self.entries = []

    def create_entry(self):
        entry_date = input("Enter the date: ")
        content = input("Enter the content of that day: ")
        self.entries.append({"date": entry_date, "content": content})
        print("entry has been created")

    def view_entry(self):
        if not self.entries:
            print("No entry found")
        else:
            print("Available entries")
            for entry in self.entries:
                print(f"Date: {entry['date']}")

