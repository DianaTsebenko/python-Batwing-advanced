class BookDB:
    books = [
        {"title": "title1", "author": "Author1", "description": "Some text about book1"},
        {"title": "title2", "author": "Author2", "description": "Some text about book2"}
    ]

    def get_all(self):
        return self.books

    def retrieve(self, title):
        for book in self.books:
            if book['title'] == title:
                return book
        return None

    def add(self, title, author, description):
        for book in self.books:
            if book['title'] == title:
                return None
        book = {
            "title": title,
            "author": author,
            "description": description
        }
        self.books.append(book)
        return book

    def update(self, title, author, description):
        for book in self.books:
            if book["title"] == title:
                book["author"] = author
                book["description"] = description
                return book
        return None

    def delete(self, title):
        self.books = [book for book in self.books if book["title"] != title]
