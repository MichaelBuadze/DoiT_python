class Stack:
    def __init__(self):
        # "stack" წარმოადგენს ცარიელ სიას ელემენტების შესანახად
        self.stack = []

    def push(self, data):
        # ელემენტის დამატება stack-ში გამოყენებით list-ის append მეთოდის
        self.stack.append(data)

    def pop(self):
        # ელემენტის ამოღება stack-იდან გამოყენებით list-ის pop მეთოდის
        if self.stack:
            return self.stack.pop()
        else:
            print("Stack ცარიელია")
            return None
