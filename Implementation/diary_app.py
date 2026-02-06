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

    def edit_entry(self):
        entry_date = input("Enter the date of the entry you want to edit")
        for entry in self.entries:
            if entry['date'] == entry_date:
                new_content = input(f"Enter new content for entry {entry_date}: ")
                entry['content'] == new_content
                print(f"Entry {entry_date} has been edited")
                return
        print(f"No entry found with date {entry_date} ")

