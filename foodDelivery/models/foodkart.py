from models.user import User
from models.restaurent import Restaurant

class Foodkart:
    def __init__(self):
        self.users = {}
        self.restaurants = {}
        self.current_user = None

    def register_user(self, name, gender, phone_number, pincode):
        if phone_number in self.users:
            print(f"User with phone number {phone_number} already exists.")
            return
        user = User(name, gender, phone_number, pincode)
        self.users[phone_number] = user

    def login_user(self, phone_number):
        if phone_number not in self.users:
            print(f"User with phone number {phone_number} not found.")
            return
        self.current_user = self.users[phone_number]
        print(f"User {self.current_user.name} logged in successfully.")

    def register_restaurant(self, restaurant_name, serviceable_pincodes, food_item, food_price, quantity):
        if restaurant_name in self.restaurants:
            print(f"Restaurant {restaurant_name} already exists.")
            return
        restaurant = Restaurant(restaurant_name, serviceable_pincodes, food_item, food_price, quantity)
        self.restaurants[restaurant_name] = restaurant

    def update_quantity(self, restaurant_name, quantity_to_add):  # negative value to reduce quantity
        if restaurant_name not in self.restaurants:
            print(f"Restaurant {restaurant_name} not found.")
            return
        restaurant = self.restaurants[restaurant_name]
        restaurant.update_quantity(quantity_to_add)

    def rate_restaurant(self, restaurant_name, rating, comment=""):
        if restaurant_name not in self.restaurants:
            print(f"Restaurant {restaurant_name} not found.")
            return
        if rating < 1 or rating > 5:
            print("Rating should be in between 1 and 5 inclusively.")
        restaurant = self.restaurants[restaurant_name]
        restaurant.add_rating(rating, comment)

    def show_restaurants(self, order_by="rating"):
        serviceable_restaurants = [
            restaurant for restaurant in self.restaurants.values()
            if self.current_user.pincode in restaurant.serviceable_pincodes and restaurant.quantity > 0
        ]
        if order_by == "rating":
            serviceable_restaurants.sort(key=lambda x: x.average_rating, reverse=True)
        elif order_by == "price":
            serviceable_restaurants.sort(key=lambda x: x.food_price, reverse=True)
        for restaurant in serviceable_restaurants:
            print(
                f"{restaurant.name}: {restaurant.food_item} - ${restaurant.food_price} - Avg Rating: {restaurant.average_rating}")

    def place_order(self, restaurant_name, quantity):
        if restaurant_name not in self.restaurants:
            print(f"Restaurant {restaurant_name} not found.")
            return
        restaurant = self.restaurants[restaurant_name]
        if quantity > restaurant.quantity:
            print(f"Insufficient quantity. Available quantity is {restaurant.quantity}.")
            return
        restaurant.update_quantity(-quantity)
        order = {
            "restaurant": restaurant.name,
            "food_item": restaurant.food_item,
            "quantity": quantity,
            "price": restaurant.food_price * quantity
        }
        self.current_user.add_order(order)
        print(f"Order placed successfully: {order}")

    def order_history(self):
        if not self.current_user:
            print("No user is currently logged in.")
            return
        print(f"Order history for {self.current_user.name}:")
        for order in self.current_user.order_history:
            print(order)
