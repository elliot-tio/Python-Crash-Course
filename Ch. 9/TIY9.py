# Chapter 9 - Classes

# 9-1. Restaurant


class Restaurant ():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant name is " + self.restaurant_name + ".")
        print("This restaurant specializes in " + self.cuisine_type + " food.")

    def open_restaurant(self):
        print(self.restaurant_name + " is currently open!")

    def set_number_served(self, number):
        if number >= self.number_served:
            self.number_served = number
        else:
            print("You can't serve less than you already have!")

    def increment_number_served(self, number):
        if number >= 0:
            self.number_served += number
        else:
            print("You can't serve a negative number of people!")


class User():

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print("This user's name is " + self.first_name + " " + self.last_name)
        print("Their email is: " + self.email)

    def greet_user(self):
        print("Hello " + self.first_name + " " +
              self.last_name + ", how are you doing?")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['Vanilla', 'Chocolate', 'Strawberry']

    def show_flavours(self):
        for flavour in self.flavours:
            print("Offered Flavour: " + flavour)


class Admin(User):

    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.privileges = ['Can add post', 'Can delete post', 'Can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print("Admin privileges: " + privilege)


if __name__ == '__main__':

    print("9-1. Restaurant\n")
    my_restaurant = Restaurant("Joey's Ristorante", "Italian")
    print(my_restaurant.restaurant_name)
    print(my_restaurant.cuisine_type)
    my_restaurant.describe_restaurant()
    my_restaurant.open_restaurant()

    print("\n9-2. Three Restaurants\n")
    new_restaurant = Restaurant("Applebee's", "Canadian")
    chinese_restaurant = Restaurant("New Ho", "Chinese")
    japanese_restaurant = Restaurant("Sakura", "Japanese")
    new_restaurant.describe_restaurant()
    chinese_restaurant.describe_restaurant()
    japanese_restaurant.describe_restaurant()

    print("\n9-3. Users\n")

    joe = User("Joe", "Dat", "joedat@gmail.com")
    jim = User("Jim", "Doe", "jimmy99@gmail.com")
    kim = User("Kim", "Possible", "kimmijim@yahoomail.com")
    joe.describe_user()
    joe.greet_user()
    jim.describe_user()
    jim.greet_user()
    kim.describe_user()
    kim.greet_user()

    print("\n9-4. Number Served\n")
    east_side_marios = Restaurant("East Side Mario's", "Italian")
    print(east_side_marios.number_served)
    east_side_marios.number_served = 10
    print(east_side_marios.number_served)
    east_side_marios.set_number_served(20)
    print(east_side_marios.number_served)
    east_side_marios.increment_number_served(10)
    print(east_side_marios.number_served)

    print("\n9-5. Login Attempts\n")
    new_user = User("Bob", "Delange", "bobbypoo@gmail.com")
    print(new_user.login_attempts)
    new_user.increment_login_attempts()
    new_user.increment_login_attempts()
    new_user.increment_login_attempts()
    new_user.increment_login_attempts()
    new_user.increment_login_attempts()
    new_user.increment_login_attempts()
    print(new_user.login_attempts)
    new_user.reset_login_attempts()
    print(new_user.login_attempts)

    print("\n9-6. Ice Cream Stand\n")
    slickers = IceCreamStand("Slickers", "Ice Cream")
    slickers.show_flavours()

    print("\n9-7. Admin\n")
    admin = Admin("Kevin", "Love", "KLove@gmail.com")
    admin.show_privileges()
