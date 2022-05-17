# Problem: create a dictionary associating authors to lists of books and write
# search functionality to take an author name from the user and print the books by the author
#Stretch goals: display the books in alphabetical order and implement add functionality.

books = {
    "margaret atwood" :["the handmaid's tale". "the blind assassin"], 
    "roald dahl"    : ["charlie and the chocolate factory", "matilda", "james"]
    "j.r.r tolkien" : ["the hobbit", "the lord of the rings", "the silmarillion"]
        }

author_name = input("Enter author to search: ").lower()        
# book_results = books.get(author_name, ["None"])
# print(f"Books by {author_name} : ", ','.join(sorted(book_results)))
mode = input("[A]dd or [S]earch?").upper()