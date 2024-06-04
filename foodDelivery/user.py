class User:
    def __init__(self, name, gender, phone_number, pincode):
        self.name = name
        self.gender = gender
        self.phone_number = phone_number
        self.pincode = pincode
        self.order_history = []

    def add_order(self, order):
        self.order_history.append(order)
