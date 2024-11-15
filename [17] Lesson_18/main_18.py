class Node:
    def __init__(self, value):
        # ატრიბუტი "value" ინახავს ნოუდის მონაცემს
        self.value = value
        # "next" მიუთითებს მომდევნო ნოუდზე სიაში
        self.next = None

class LinkedList:
    def __init__(self):
        # სიის პირველი ნოუდი, "head", თავდაპირველად ცარიელია
        self.head = None

    def append(self, value):
        # ახალი ნოუდის შექმნა გადაცემული მონაცემით
        new_node = Node(value)
        # თუ სია ცარიელია, ახალი ნოუდი ხდება "head"
        if not self.head:
            self.head = new_node
        else:
            # ვპოულობთ სიის ბოლო ნოუდს
            current = self.head
            while current.next:
                current = current.next
            # სიის ბოლოს ვამატებთ ახალ ნოუდს
            current.next = new_node

    def remove(self):
        # თუ სია ცარიელია, ვაბრუნებთ შეტყობინებას
        if not self.head:
            print("სიაში ელემენტები არ არის")
            return

        # თუ სიაში მხოლოდ ერთი ელემენტია, ვაშორებთ მას
        if not self.head.next:
            self.head = None
        else:
            # ვპოულობთ ბოლოს წინა ნოუდს
            current = self.head
            while current.next and current.next.next:
                current = current.next
            # ვშლით ბოლო ნოუდს
            current.next = None
