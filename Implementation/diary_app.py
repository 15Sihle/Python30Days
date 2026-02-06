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

    def delete_entry(self):
        entry_date = input("Enter the date of the entry you want to delete: ")
        for entry in self.entries:
            if entry['date'] == entry_date:
                self.entries.remove(entry)
                print(f"Entry {entry_date} has been deleted")
                return
        print(f"No entry found with date {entry_date}")

    def save_entries_to_file(self):
        with open("entries.txt", "w") as file:
            for entry in self.entries:
                file.write(f"Date: {entry['date']}\n")
                file.write(f"Title: {entry['content']}\n")
                file.write("\n")

    def run(self):

        while True:
            print("\nSimple Diary Application Menu: " )
            print("1. Create Entry")
            print("2. View Entry")
            print("3. Edit Entry")
            print("4. Delete Entry")
            print("5. Save Entry")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_entry()
            elif choice == '2':
                self.view_entry()
            elif choice == '3':
                self.edit_entry()
            elif choice == '4':
                self.delete_entry()
            elif choice == '5':
                self.save_entries_to_file()
            elif choice == '6':
                print("Exiting Diary Application")
                break
            else:
                print("Invalid choice. Please try again")

if __name__ == "__main__":
    diary = Diary()
    diary.run()




