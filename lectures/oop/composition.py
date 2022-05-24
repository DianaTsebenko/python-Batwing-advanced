class Book:
    def __init__(self):
        page_1 = Page('Page 1')
        page_2 = Page('Page 2')
        page_3 = Page('Page 3')
        self.pages = [page_1.content, page_2.content, page_3.content]

class Page:
    def __init__(self, content):
        self.content = content

book = Book()
print(book.pages)