class Book:
    def __init__(self,title,author,pages):
        self._title = title
        self._author = author
        self._pages = pages


    def get_info(self):  
        return f"'{self._title}' by {self._author}, {self._pages} pages"

    def read(self): 
        return f"Reading '{self._title}'..."
        

class FictionBook(Book):  
    def __init__(self, title, author, pages, genre): 
        super().__init__(title, author, pages)  
        self._genre = genre  

    def get_info(self):  
        return f"{super().get_info()}, Genre: {self._genre}"

    def read(self):  
        return f"Enjoying the {self._genre} story of '{self._title}'..."
    
class NonFictionBook(Book):
    def __init__(self, title, author, pages, topic):
        super().__init__(title, author, pages)
        self._topic = topic

    def get_info(self):
        return f"{super().get_info()}, Topic: {self._topic}"

    def read(self):
        return f"Learning about {self._topic} from '{self._title}'..."
    

if __name__ == "__main__":  
    novel = FictionBook("The Hobbit", "J.R.R. Tolkien", 310, "Fantasy")
    biography = NonFictionBook("Steve Jobs", "Walter Isaacson", 656, "Biography")

    books = [novel, biography]  
    for book in books:  
        print(book.get_info()) 
        print(book.read())
        print()  