#A simply library system for an admin to input, update and delete books 

books_list = []

#collecting book details
def add_book():
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    year = input("Enter the book's publication year: ")

#dictionary to store book details
    book = {
        "title": title,
        "author": author,
        "year": year
    }

#adding the book to the list of books
    books_list.append(book)

#function to display book details
def display_book():
    for book in books_list:
        print(f"Title of book: {book["title"]}, Author: {book["author"]}, Year of publication: {book["year"]}")

#function to remove a book from the list of books
def delete_book():
    title = input("Enter the title of the book you want to delete: ")
    for book in books_list:
        if book["title"] == title:
            books_list.remove(book)
            print("Book deleted successfully!")
        else:
            print("This book cannot be found!")

#main function to run the program
def main():
    while True:
        print("LIBRARY MANAGEMENT SYSTEM")
        print("1. Add Book")
        print("2. Delete Book")
        print("3. Display Book")
        print("4. Exit")

        print("Welcome! What would you like to do?")
        choice = (input("Enter your choice: "))

        if choice == "1":
            add_book()
        elif choice == "2":
            delete_book()
        elif choice == "3":
            display_book()
        elif choice == "4":
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
