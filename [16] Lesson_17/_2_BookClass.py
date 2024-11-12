class Book:
    def __init__(self, title, author):
        # ინიციალიზაცია: წიგნის სათაური და ავტორი
        self.title = title
        self.author = author

    def __eq__(self, other):
        # ტოლობის შემოწმება: წიგნები ითვლებიან ტოლად თუ მათი სათაური და ავტორი იდენტურია
        return self.title == other.title and self.author == other.author

# გამოყენება დავალებაში მოცემული მაგალითის მიხედვით:
book1 = Book('1984', 'George Orwell')
book2 = Book('1984', 'George Orwell')
book3 = Book('Brave New World', 'Aldous Huxley')
print(book1 == book2)  # Output: True
print(book1 == book3)  # Output: False
