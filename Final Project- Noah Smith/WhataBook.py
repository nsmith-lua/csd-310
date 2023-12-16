
#Noah Smith
#Bellevue University 
#12/16/23
#Final Project python app
#version 3''


import sys
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
}
# imports the database and module
class WhatABookApp:
    def __init__(avar):
        avar.connection = mysql.connector.connect(**config)
        avar.cursor = avar.connection.cursor()
        avar.user_id = None 

# Show menu systems. I thought it would be better to keep the menu system where you type in the command word for word. That is so users can access menu option from any place in the app as long as the try is true.
# Also this helps users not get confused between the two similar menus. 
    def show_menu(avar):
        commands = {
            'show_books': avar.show_books,
            'show_locations': avar.show_store_locations,
            'show_account_menu': avar.show_account_menu,
            'exit': avar.exit,
        }

        print("\n********Main Menu**********")
        print("\n1. show_books")
        print("\n2. show_locations")
        print("\n3. show_account_menu") 
        print("\n4. exit")
        print("\nType a command to begin")

        user_input = input("Enter your command: ").lower()
        if user_input in commands:
            commands[user_input]()
        else:
            print("Invalid command. Try typing show_books")

    def show_account_menu(avar):
        commands = {
            'wishlist': avar.show_wishlist,
            'show_books_to_add': avar.show_books_to_add,
            'add_book_to_wishlist': avar.add_book_to_wishlist,
            'main_menu': avar.show_menu,
            'exit': avar.exit,
        }
        print("\nAccount Menu:")
        print("\n1. wishlist")
        print("\n2. show_books_to_add")
        print("\n3. add_book_to_wishlist")
        print("\n4. main_menu")
        print("\n5. exit")
        print("\nType a command to move forward")

        user_input = input("Enter your command: ").lower()
        if user_input in commands:
            commands[user_input]()
        else:
            print("Invalid command")
#So this tests if the user is the user. I didn't understand this at all until I saw the professor's code. I got this to work with the class instead of other's solution somehow. 
    def validate_user(avar):
        while True:
            try:
                user_id = int(input("Enter ID: "))
                query = "SELECT user_id FROM user WHERE user_id = %s"
                avar.cursor.execute(query, (user_id,))
                result = avar.cursor.fetchone()
                if result:
                    avar.user_id = user_id
                    return
                else:
                    print("Invalid ID.")
            except ValueError:
                print("Invalid input.")

# Grabs the books query and presents it to the user after type the command into the console.
    def show_books(avar):
            avar.cursor.execute("SELECT book_id, book_name, author FROM book")
            books = avar.cursor.fetchall()

            print("\n** Books **")
            for book in books:
                print("  Book ID: {}\n  Book Name: {}\n  Author: {}\n".format(book[0], book[1], book[2]))

# Grabs the store location query and presents it to the user after type the command into the console.
    def show_store_locations(avar):
        avar.cursor.execute("SELECT store_id, locale from store")
        locations = avar.cursor.fetchall()

        print("\n** Store Locations **")
        for location in locations:
            print(f"{location[0]}. {location[1]}")

# Grabs the wishlist query and validates the user that is using it. Then presents it to the user after type the command into the console.
    def show_wishlist(avar):
        print(f"User ID: {avar.user_id}")
        avar.cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(avar.user_id))
        wishlist = avar.cursor.fetchall()
        print("Wishlist:", wishlist)

# exits the program with sys import functions
    def exit(avar):
        sys.exit()

#shows the books that can be added
    def show_books_to_add(avar):
        query = ("SELECT book_id, book_name, author "
                "FROM book "
                "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(avar.user_id))
        avar.cursor.execute(query)
        books_to_add = avar.cursor.fetchall()

        print("\n** Adding Books **")
        for book in books_to_add:
            print(f"{book[0]}. {book[1]} by {book[2]}")

#Adds the book to the users wishlist by the user inputting the books name. Has to be exactly right or it errors out.
    def add_book_to_wishlist(avar):
        try:
            book_id = int(input("Enter the book ID to add to your wishlist (or 0 to exit): "))
            if book_id == 0:
                return
            query = "INSERT INTO wishlist (user_id, book_id) VALUES (%s, %s)"
            avar.cursor.execute(query, (avar.user_id, book_id))
            
            avar.connection.commit() #commit changes
            print("Book added!")
        except ValueError:
            print("Invalid input.")


# This the end of the class. This is a part of a solution that I found a online on geeks for geeks. It is not exactly the same though, I obviously made it work for my program and did not copy and paste the code, but borrowed the concept. 
# This was the only solution that I could find to work with my head.
# While it tries to start a block it handles errors that might occur. Validating the user it will show the menu until indefinitely and if anything else it will error out or at the end it will close.
if __name__ == "__main__":
    try:
        avar = WhatABookApp()
        avar.validate_user()
        while True:
            avar.show_menu()
    except Exception as i:
        print(f"error: {i}")
    finally:
        if avar and avar.connection:
            avar.connection.close()


# Although a difficult assignment, it was a lot of fun learning more about python code and the try function is eye opening because I never really used them until now.


