
# ============================================================
# 📚 LIBRARY MANAGEMENT SYSTEM
# ============================================================

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_available = True

    def display_info(self):
        status = "Available" if self.is_available else "Borrowed"

        print(
            f"ID: {self.book_id} | "
            f"Title: {self.title} | "
            f"Author: {self.author} | "
            f"Status: {status}"
        )


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def display_info(self):
        print(
            f"ID: {self.member_id} | "
            f"Name: {self.name} | "
            f"Borrowed Books: {len(self.borrowed_books)}"
        )


class Library:

    def __init__(self):
        self.books = []
        self.members = []

    # ========================================================
    # ADD BOOK
    # ========================================================

    def add_book(self):

        print("\n========== ADD BOOK ==========")

        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        # Check duplicate ID

        for book in self.books:

            if book.book_id == book_id:

                print("❌ Book ID already exists!")
                return

        book = Book(
            book_id,
            title,
            author
        )

        self.books.append(book)

        print("✅ Book added successfully!")

    # ========================================================
    # VIEW BOOKS
    # ========================================================

    def view_books(self):

        print("\n========== ALL BOOKS ==========")

        if not self.books:

            print("No books available.")

            return

        for book in self.books:

            book.display_info()

    # ========================================================
    # SEARCH BOOK
    # ========================================================

    def search_book(self):

        print("\n========== SEARCH BOOK ==========")

        keyword = input(
            "Enter title, author or ID: "
        ).lower()

        found = False

        for book in self.books:

            if (
                keyword in book.title.lower()
                or keyword in book.author.lower()
                or keyword in book.book_id.lower()
            ):

                book.display_info()

                found = True

        if not found:

            print("❌ No matching book found.")

    # ========================================================
    # ADD MEMBER
    # ========================================================

    def add_member(self):

        print("\n========== ADD MEMBER ==========")

        member_id = input("Enter Member ID: ")
        name = input("Enter Member Name: ")

        # Check duplicate ID

        for member in self.members:

            if member.member_id == member_id:

                print("❌ Member ID already exists!")

                return

        member = Member(
            member_id,
            name
        )

        self.members.append(member)

        print("✅ Member added successfully!")

    # ========================================================
    # VIEW MEMBERS
    # ========================================================

    def view_members(self):

        print("\n========== ALL MEMBERS ==========")

        if not self.members:

            print("No members registered.")

            return

        for member in self.members:

            member.display_info()

    # ========================================================
    # FIND MEMBER
    # ========================================================

    def find_member(self, member_id):

        for member in self.members:

            if member.member_id == member_id:

                return member

        return None

    # ========================================================
    # FIND BOOK
    # ========================================================

    def find_book(self, book_id):

        for book in self.books:

            if book.book_id == book_id:

                return book

        return None

    # ========================================================
    # BORROW BOOK
    # ========================================================

    def borrow_book(self):

        print("\n========== BORROW BOOK ==========")

        member_id = input("Enter Member ID: ")
        book_id = input("Enter Book ID: ")

        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member is None:

            print("❌ Member not found!")

            return

        if book is None:

            print("❌ Book not found!")

            return

        if not book.is_available:

            print("❌ Book is already borrowed!")

            return

        book.is_available = False

        member.borrowed_books.append(book)

        print(
            f"✅ {member.name} borrowed "
            f"'{book.title}' successfully!"
        )

    # ========================================================
    # RETURN BOOK
    # ========================================================

    def return_book(self):

        print("\n========== RETURN BOOK ==========")

        member_id = input("Enter Member ID: ")
        book_id = input("Enter Book ID: ")

        member = self.find_member(member_id)
        book = self.find_book(book_id)

        if member is None:

            print("❌ Member not found!")

            return

        if book is None:

            print("❌ Book not found!")

            return

        if book not in member.borrowed_books:

            print(
                "❌ This member did not borrow this book!"
            )

            return

        book.is_available = True

        member.borrowed_books.remove(book)

        print(
            f"✅ {member.name} returned "
            f"'{book.title}' successfully!"
        )

    # ========================================================
    # REMOVE BOOK
    # ========================================================

    def remove_book(self):

        print("\n========== REMOVE BOOK ==========")

        book_id = input("Enter Book ID: ")

        book = self.find_book(book_id)

        if book is None:

            print("❌ Book not found!")

            return

        if not book.is_available:

            print(
                "❌ Cannot remove a borrowed book!"
            )

            return

        self.books.remove(book)

        print("✅ Book removed successfully!")

    # ========================================================
    # REMOVE MEMBER
    # ========================================================

    def remove_member(self):

        print("\n========== REMOVE MEMBER ==========")

        member_id = input("Enter Member ID: ")

        member = self.find_member(member_id)

        if member is None:

            print("❌ Member not found!")

            return

        if member.borrowed_books:

            print(
                "❌ Cannot remove member while "
                "they have borrowed books!"
            )

            return

        self.members.remove(member)

        print("✅ Member removed successfully!")


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    library = Library()

    while True:

        print("\n")
        print("=" * 50)
        print("        📚 LIBRARY MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. 📖 Add Book")
        print("2. 📚 View Books")
        print("3. 🔍 Search Book")
        print("4. 👤 Add Member")
        print("5. 👥 View Members")
        print("6. 📥 Borrow Book")
        print("7. 📤 Return Book")
        print("8. 🗑️ Remove Book")
        print("9. ❌ Remove Member")
        print("10. 🚪 Exit")

        print("=" * 50)

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            library.add_book()

        elif choice == "2":

            library.view_books()

        elif choice == "3":

            library.search_book()

        elif choice == "4":

            library.add_member()

        elif choice == "5":

            library.view_members()

        elif choice == "6":

            library.borrow_book()

        elif choice == "7":

            library.return_book()

        elif choice == "8":

            library.remove_book()

        elif choice == "9":

            library.remove_member()

        elif choice == "10":

            print("\n👋 Thank you for using")
            print("   Library Management System!")

            break

        else:

            print(
                "❌ Invalid choice! "
                "Please try again."
            )


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":

    main()

