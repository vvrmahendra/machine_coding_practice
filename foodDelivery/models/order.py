class Order:
    def __init__(self,restaurant, food_item, quantity, price):
        self.restaurant = restaurant
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"Restaurant: {self.restaurant}, FoodItem: {self.food_item}, Quantity: {self.quantity}, Price: {self.price}"