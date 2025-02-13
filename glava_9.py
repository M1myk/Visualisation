class Dog():
    """Простая модель собаки."""

    def __init__(self, name, age):
        """Инициализирует атрибуты name и age."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Собака перекатывается по команде."""
        print(f"{self.name} rolled over!")


my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()


class Resaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def open_restaurant(self):
        print(f'{self.name} вже відкритий!')

    def describe_restaurant(self):
        print(f'Ресторан подає такі страви: {self.cuisine} ')





restaurant = Resaurant('Galyczyna', 'Борщ, Вареники')
print(f'{restaurant.name} подає такі страви: {restaurant.cuisine}')
restaurant.open_restaurant()
restaurant.describe_restaurant()

restaurant2 = Resaurant('Puzata Hata','Сало з частиком')
restaurant2.describe_restaurant()
