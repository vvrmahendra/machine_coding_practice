class Restaurant:
    def __init__(self, name, serviceable_pincodes, food_item, food_price, quantity):
        self.name = name
        self.serviceable_pincodes = serviceable_pincodes
        self.food_item = food_item
        self.food_price = food_price
        self.quantity = quantity
        self.ratings = []

    def update_quantity(self, quantity_to_add):
        if self.quantity + quantity_to_add < 0:
            print("Quantity cannot be less than 0.")
            return
        self.quantity += quantity_to_add

    def add_rating(self, rating, comment=""):
        self.ratings.append((rating, comment))

    @property
    def average_rating(self):
        if not self.ratings:
            return 0
        return sum(r[0] for r in self.ratings) / len(self.ratings)
