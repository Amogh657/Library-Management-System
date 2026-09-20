import json

class library:
    books = []
    members = {} 
    ind = 0
    name = ''

    def __init__(self):
        # Load Books
        try:
            with open("Books.json", "r") as file:
                self.books = json.load(file)
        except FileNotFoundError:
            self.books = []
            
        # Load Members
        try:
            with open("members.json", "r") as file:
                self.members = json.load(file)
        except FileNotFoundError:
            self.members = {}

    def greet(welcome):
        def mfx(self):
            print("....Welcome to the library... ")  
            welcome(self)
            print(f"{self.name}, how can I help?")
        return mfx

    @greet
    def welcome(self):
        self.name = input("Enter your name: ").strip()
  
        if self.name not in self.members:
            self.members[self.name] = []
            self.save_members()
            print(f"New member profile created for {self.name}!")
        else:
            print(f"Welcome back, registered member {self.name}!")

    def save_members(self):
        """Helper function to save member data to file"""
        with open("members.json", 'w') as file:
            json.dump(self.members, file, indent=4)

    def add(self):
        bc = input('Enter the book title you want to add:\n').strip()
        if bc in self.books:
            print(f"\"{bc}\" is already in the library.")
        else:
            self.books.append(bc)
            print(f"\"{self.books[-1]}\" IS ADDED") 
            with open("Books.json", 'w') as file:
                json.dump(self.books, file, indent=4)

    def display(self):
        if len(self.books) != 0:
            with open("Books.json", 'r') as file:
                temp = json.load(file)
                print("\n--- Displaying All Available Books ---")
                for l, i in enumerate(temp, start=1):
                    print(f"{l}. {i}")
        else:
            print("Nothing to display (Library is empty).")        

    def borrow(self):
        br = input("Enter the book you want to borrow: ")
        try:
            r = self.books.index(br)
            
            self.books.pop(r)
            with open("Books.json", 'w') as file:
                json.dump(self.books, file, indent=4)
            
            
            self.members[self.name].append(br)
            self.save_members()
            
            print(f"\"{br}\" borrowed successfully by {self.name}!")

        except ValueError:
            print("Book not found in library stock. \nERROR 404")

    def display_members(self):
        print("\n--- Registered Library Members ---")
        if not self.members:
            print("No members registered yet.")
            return
            
        for name, borrowed_books in self.members.items():
            books_str = ", ".join(borrowed_books) if borrowed_books else "No books borrowed"
            print(f"Member: {name} | Borrowed: [{books_str}]")

a = library()
a.welcome()

while True:
    x = input("\nWhat do you want to do?\n1: Add Book\n2: Display Books\n3: Borrow Book\n4: View Members\n5: Exit\nSelect option: ")
    try:
        match int(x):
            case 1:
                a.add()
            case 2:
                a.display()
            case 3:
                a.borrow()
            case 4:
                a.display_members()
            case 5:
                print("THANK YOU FOR VISITING")
                exit(0)
            case _:
                print("Choose wisely (1-5)")
    except Exception as e:
        print(f"Invalid input: {e}")
