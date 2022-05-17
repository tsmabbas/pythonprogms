

list1 = ["book1", "book2", "book3"]
list2 = ["book4", "book5", "book6"]
books = {"Auth1" : list1, "Auth2" : list2}

#books = {"Auth1" : "book1", "Auth1" : "book2", "Auth2" : "book3", "Auth2" : "book4"}



s1 = input("Enter the Auther Name : ")

print(books[s1])