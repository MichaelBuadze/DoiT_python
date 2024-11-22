import dill
import os

def deserialize_file_with_dill(filename):
    """
    ფუნქცია დაშიფრული ფაილის დესერიალიზაციისთვის Dill-ის გამოყენებით.

    Args:
        filename: დაშიფრული ფაილის სახელი.
    """
    try:
        # განსაზღვრეთ მიმდინარე დირექტორიაში ფაილის სრული გზა
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, filename)
        
        
        # გახსენით ფაილი
        with open(file_path, 'rb') as f:
            data = dill.load(f)
            # ვიღებთ ობიექტს ტუპლის მეორე ელემენტიდან
            obj = data[1]
            print(obj)
    except (dill.UnpicklingError, EOFError) as e:
        print(f"ფაილის დესერიალიზაცია ვერ მოხერხდა: {e}")
    except FileNotFoundError:
        print(f"ფაილი '{filename}' ვერ მოიძებნა მიმდინარე დირექტორიაში: {current_dir}")
    
# ფუნქციის გამოძახება
deserialize_file_with_dill('my_data_dill.pkl')
