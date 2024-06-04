from foodkart import Foodkart
if __name__ == "__main__":
    foodkart = Foodkart()

    foodkart.register_user("Alice", "Female", "1234567890", 560001)
    foodkart.register_user("Bob", "Male", "0987654321", 560002)

    foodkart.login_user("1234567890")

    foodkart.register_restaurant("Pizza Hut", [560001, 560002], "Pizza", 12, 100)
    foodkart.register_restaurant("Burger King", [560001], "Burger", 8, 50)
    foodkart.register_restaurant("Subway", [560002], "Sub", 10, 30)

    foodkart.show_restaurants(order_by="rating")

    foodkart.place_order("Pizza Hut", 2)

    foodkart.rate_restaurant("Pizza Hut", 5, "Great pizza!")

    foodkart.show_restaurants(order_by="price")

    foodkart.order_history()

    foodkart.login_user("0987654321")

    foodkart.place_order("Subway", 1)

    foodkart.order_history()
