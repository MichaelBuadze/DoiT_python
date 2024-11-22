import os
import json
import pickle

def serialize_object(obj, filename):
    """
    ფუნქცია ობიექტის სერიალიზაციისთვის JSON ან Pickle ფორმატში.

    Args:
        obj: სერიალიზებული ობიექტი.
        filename: ფაილის სახელი, სადაც ინფორმაცია უნდა შენახოს.

    Returns:
        None
    """
     # განსაზღვრეთ მიმდინარე დირექტორიაში ფაილის სრული გზა
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, filename)
    try:
        # ვცდილობთ ობიექტის სერიალიზაციას JSON-ის გამოყენებით
        with open(file_path, 'w', encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False)  # ensure_ascii=False არა-ASCII სიმბოლოების შესანარჩუნებლად
            print(f"ობიექტი წარმატებით შენახულია JSON ფორმატში ფაილში: {filename}")
    except TypeError:
        print("ობიექტი არ არის JSON-ისთვის სერიალიზებადი. ვცდილობთ Pickle-ის გამოყენებას...")
        try:
            # თუ JSON ვერ მუშაობს, ვცდილობთ Pickle-ის გამოყენებას
            with open(file_path, 'wb') as f:  # encoding პარამეტრი ამოვიღეთ
                pickle.dump(obj, f)
                print(f"ობიექტი წარმატებით შენახულია Pickle ფორმატში ფაილში: {filename}")
        except Exception as e:
            print(f"ობიექტის სერიალიზაცია ვერ მოხერხდა: {e}")

# ობიექტის მაგალითი
my_object = {'name': 'გიორგი', 'age': 30, 'city': 'თბილისი'}

# ფუნქციის გამოძახება
serialize_object(my_object, 'my_data.json')