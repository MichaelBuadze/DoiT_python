import os
import json
import pickle

def deserialize_file(filename):
  """
  ფუნქცია დაშიფრული ფაილის დესერიალიზაციისთვის JSON ან Pickle ფორმატში.

  Args:
    filename: დაშიფრული ფაილის სახელი.

  Returns:
    None
  """
   # განსაზღვრეთ მიმდინარე დირექტორიაში ფაილის სრული გზა
  current_dir = os.path.dirname(os.path.abspath(__file__))
  file_path = os.path.join(current_dir, filename)
  try:
    # ვცდილობთ ფაილის წაკითხვას და დესერიალიზაციას JSON-ის გამოყენებით
    with open(file_path, 'r', encoding="utf-8") as f:
      data = json.load(f)
      print(data)
  except json.JSONDecodeError:
    print("ფაილი არ არის JSON ფორმატში. ვცდილობთ Pickle-ის გამოყენებას...")
    try:
      # თუ JSON ვერ მუშაობს, ვცდილობთ Pickle-ის გამოყენებას
      with open(file_path, 'rb') as f:
        data = pickle.load(f)
        print(data)
    except (pickle.UnpicklingError, EOFError) as e:
      print(f"ფაილის დესერიალიზაცია ვერ მოხერხდა: {e}")

# ფუნქციის გამოძახება
deserialize_file('my_data.json')