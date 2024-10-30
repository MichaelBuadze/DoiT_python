import os
import json
# ზემოთ შემოვიტანეთ აუცილებელი მოდულები

# შესაქმნელი ფაილის მისამართი:
file_path = "[12] Lesson_12/chess_data/players.json"

# განვსაზღვროთ 'შემქმნელი ფუნქცია':

def create_file(directory, filename):
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as f:
        pass  # შექმნის ახალ ფაილს, ან გაასუფთავებს მას
    return filepath

# "მკითხველი ფუნქცია":

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    return content # წაიკითხავს შექმნილს, ან გასუფთავებულ ფაილს, ანუ გამოიტანს არაფერს

# "გამნახლებელი ფუნქცია"

def update_file(filepath, data_dict):
    try:
        with open(filepath, 'r+', encoding='utf-8') as f:
            content = f.read()
            if content:
                chess_players = json.loads(content)
            else:
                chess_players = []
    except FileNotFoundError:
        chess_players = []
    
    # ამატებს ახალ ლექსიკოინს და არა ლისტს
    chess_players.append(data_dict)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(chess_players, f,  indent=4)


create_file('[12] Lesson_12/chess_data', 'players.json')

# ფაილის კონტენტის წაკითხვა
print("პირველი წაკითხვის შედეგი - სიცარიელე")
print(read_file('[12] Lesson_12/chess_data/players.json'))


chess_players = [
  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
  {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
  {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
  {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
  {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
  {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
  {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
  {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]

players_to_add = [
  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
]


# შექმნილი, ან განახლებული ფაილის შევსება
for player in chess_players:
    update_file(file_path, player)


# ფაილის შიგთავსის წაკითხვა
print("ფაილის მე-2 წაკითხვა")
print(read_file('[12] Lesson_12/chess_data/players.json'))

# შევსებული ფაილის განახლება, ბოლო ორი ლექსიკონის დამატება
for player in players_to_add[:2]:  # მხოლოდ 2 ლექსიკონის დამატება
    update_file(file_path, player)

# ფაილის კონტენტის წაკითხვა
print("საბოლოო წაკითხვა")
print(read_file('[12] Lesson_12/chess_data/players.json'))
