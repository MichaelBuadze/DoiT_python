import os
import json

# წიგნის კლასი: ინახავს ინფორმაციას ერთი წიგნის შესახებ
class Book: # იწყება ობიექტის შექმნა
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        # განსაზღვრავს თუ როგორ უნდა გამოიტანოს ობიექტი ტექსტური სახით
        return f"\n{'დასახელება:':<15} {self.title}, \n\n{'ავტორი:':<15} {self.author}, \n\n{'გამოცემის წელი:':<15} {self.year}"


class BookManager: # მართავს წიგნების სიას და ურთიერთქმედებს JSON ფაილთან
    def __init__(self, filename='books.json'):
        self.filename = os.path.join(os.path.dirname(__file__), filename)  # ფაილის სრული მისამართი, სადაც შეინახება მონაცემები, კონკრეტული ხერხისთვის მადლობა Google-ს :)
        self.books = []  # ცარიელი სია წიგნებისთვის
        self.load_from_json()  # ტვირთავს წიგნებს ფაილიდან, თუ არსებობს
    
    # დაამატებს ახალ წიგნს და შეინახავს ცვლილებებს ფაილში
    def add_book(self, book):
        self.books.append(book)
        self.save_to_json()


    def list_books(self): #კონსოლში გამოიტანს ბიბლიოთეკის ფონდში არსებულ წიგნებს
        print() # თავისუფალი სივრცე
        print("=" * 60)
        print(f"{'დასახელება':<20} {'ავტორი':<20} {'გამოცემის წელი':<15}")
        print("=" * 60)
        for book in self.books:
            print(f"{book.title:<20} {book.author:<20} {book.year:<15}")
            print("-" * 60)
        

    def find_book_by_title(self, title): # ეძებს კონკრეტულ წიგნს დასახელების მიხედვით
        for book in self.books:
            if book.title == title:
                return book
        return None

    def save_to_json(self): # ინახავს წიგნების მონაცემებს JSON ფაილში
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump([book.__dict__ for book in self.books], f, indent=4, ensure_ascii=False)

    def load_from_json(self): # ტვირთავს წიგნების მონაცემებს JSON ფაილიდან
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for book_data in data:
                    book = Book(**book_data)
                    self.books.append(book)
        except FileNotFoundError:
            print("ფაილი ვერ მოიძებნა. იქმნება ახალი ფაილი...")

def main(): # მთავარი ფუნქცია, სადაც იწყება პროგრამის შესრულება
    book_manager = BookManager()

    while True:
        print("\nკონსოლში შეიყვანეთ მენიუს შესაბამისი ციფრი და დააჭირეთ Enter-ს.")
        print("\n1. ბიბლიოთეკა - არსებული წიგნები")
        print("2. წიგნის ძებნა დასახელებით")
        print("3. წიგნის დამატება")
        print("4. პროგრამის დახურვა")
        choice = input("\nშეიყვანეთ ციფრი: ")

        
        if choice == "1":
            book_manager.list_books()
        elif choice == "2":
            title = input("შეიყვანეთ დასახელება: ")
            book = book_manager.find_book_by_title(title)
            if book:
                print(book)
            else:
                print("\nმითითებული წიგნი, არ არის ბაზაში.")
        elif choice == "3":
            while True:
                title = input("წიგნის დასახელება: ")
                if not title:
                    print("დასახელება აუცილებელი ველია და ის არ უნდა იყოს ცარიელი!")
                    continue
                else:
                    break
            while True:    
                author = input("ავტორი: ")
                if not author:
                    print("თუ ავტორი უცნობია, ჩაწერე - \"უცნობი ავტორი\"")
                    continue
                else:
                    break
            while True:
                try:
                    year = int(input("გამოცემის წელი: "))
                    if year < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("დაფიქსირდა შეცდობა! შეიყვანეთ დადებითი მთელი რიცხვი.")
            book = Book(title, author, year)
            book_manager.add_book(book)
        elif choice == "4":
            break
        else:
            print("გთხოვთ შეიყვანოთ კონკრეტული მენიუს შესაბამისი ციფრი.")

if __name__ == "__main__":
    main()