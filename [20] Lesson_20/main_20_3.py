import os
import dill


def serialize_object_with_dill(obj, filename):
  """
  ფუნქცია ობიექტის სერიალიზაციისთვის Dill-ის გამოყენებით.

  Args:
    obj: სერიალიზებული ობიექტი.
    filename: ფაილის სახელი, სადაც ინფორმაცია უნდა შენახოს.
  """
 # განსაზღვრეთ მიმდინარე დირექტორიაში ფაილის სრული გზა
  current_dir = os.path.dirname(os.path.abspath(__file__))
  file_path = os.path.join(current_dir, filename)
  # ვიქმნით მარტივ ლამბდა ფუნქციას და ვამატებთ ობიექტს
  obj_with_lambda = (lambda x: x*2, obj)

  try:
    with open(file_path, 'wb') as f:
      dill.dump(obj_with_lambda, f)
      print(f"ობიექტი წარმატებით შენახულია Dill ფორმატში ფაილში: {filename}")
  except Exception as e:
      print(f"ობიექტის სერიალიზაცია ვერ მოხერხდა: {e}")

# ობიექტის მაგალითი
my_object = {'name': 'გიორგი', 'age': 30, 'city': 'თბილისი'}

# ფუნქციის გამოძახება
serialize_object_with_dill(my_object, 'my_data_dill.pkl')