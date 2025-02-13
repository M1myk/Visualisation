def glava_2():  # 06.11.2023 ПОЧАТОК КНИГИ
    f_n = 'Dmytro  '
    l_n = '   zvir'
    message = f'\t {f_n.title().strip()} {l_n.title().lstrip()} how are u ?'
    message1 = f'\n\t{f_n.lower().strip()} {l_n.upper().strip()} how are u ?'
    f_p = '   Albert Einstein once said, "A person who never made \n  a mistake never tried anything new."'
    print(f'{message}{message1}\n{f_p}')

    universe_age = 14_000_000_000
    print(universe_age)


def glava_3():
    bicycles = ['trek', 'cannondale', 'redline', 'specialized']
    print(bicycles[0].title())  # Показує перший елемент
    print(bicycles[-1])  # Показує останній елемент
    message = f"My first bicycle was a {bicycles[0].title()}, but my second was a {bicycles[-2]}."
    print(message)

    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(motorcycles)
    motorcycles[0] = 'ducati'
    print(motorcycles)
    motorcycles.append('honda')  # Добавляє елемент в кінець листа
    print(motorcycles)

    motorcycles = []
    motorcycles.append('honda')  # Добавлення елементів в пустий список
    motorcycles.append('yamaha')
    motorcycles.append('suzuki')
    print(motorcycles)

    motorcycles = ['honda', 'yamaha', 'suzuki']
    motorcycles.insert(0, 'ducati')  # Добавлення елемента в конкретне місце
    print(motorcycles)
    del motorcycles[1]  # видаленняя елемента остаточно
    print(motorcycles)

    print(f'\n')
    motorcycles = ['honda', 'yamaha', 'suzuki']
    poped_motorcycles = motorcycles.pop()  # видаленняя елемента не остаточно
    print(motorcycles)
    print(poped_motorcycles)

    motorcycles = ['honda', 'yamaha', 'suzuki']
    last_owned = motorcycles.pop()  # Пустсий - останній   # 0 - перший
    print(f'The last motorcycled i owned was {last_owned.title()}')
    motorcycles.remove('yamaha')  # Видаляє елемент по назві
    print(motorcycles)

    names = ['mama', 'tato', 'baba']
    names.append('dido')
    print(f'Запрошую тебе, {names[0].title()} на день народження!')
    print(f'Запрошую тебе, {names[-2].title()} на день народження!')
    baba = names.pop()
    print(f'Запрошую тебе, {baba.title()} на день народження!')


def glava_4():
    magicians = ['alice', 'david', 'carolina']
    for magician in magicians:
        print(f"{magician.title()}, that was a great trick!")
        print(f"I can't wait to see your next trick, {magician.title()}.\n")
    print("Thank you, everyone. That was a great magic show!")
    print(f'\n')

    pizzas = ['Margharita', 'Salami', 'Proschuto']
    for pizza in pizzas:
        print(f'I like {pizza} pizza!')
    print(f"\nI really love pizza!\n")

    numbers = list(range(1, 6))
    print(numbers)
    even_numbers = list(range(2, 11, 2))
    print(even_numbers)

    squares = []
    for value in range(1, 11):
        squares.append(value ** 2)
    print(squares)
    print(f'\n\tІнший метод: ')
    squares = [value ** 2 for value in range(1, 11)]
    print(squares)

    lisst = []
    for value in range(1, 1000001):
        lisst.append(value)
    print(min(lisst), max(lisst), sum(lisst))
    value = []
    for i in range(1, 20, 2):
        value.append(i)
    print(value)

    lisst = []
    for i in range(3, 31, 3):
        lisst.append(i ** 3)
    print(lisst)
    lisst = [i ** 3 for i in range(3, 31, 3)]
    print(lisst)

    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    print(players[0:3])
    print(players[2:])  # від 2 до останнього елемента

    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    print("Here are the first three players on my team:")
    for player in players[:3]:
        print(player.title())

    my_foods = ['pizza', 'falafel', 'carrot cake']
    friend_foods = my_foods[:2]

    my_foods.append('cannoli')
    friend_foods.append('ice cream')

    print(f"\nMy favorite foods are: ")
    print(my_foods)
    print("\nMy friend's favorite foods are:")
    print(friend_foods)

    dimensions = (200, 50)  # кортежи
    print(dimensions[0])
    print(dimensions[1])

    #  my_t = (3,)  # Для роботи з одним елементом

    print("Original dimensions:")
    for dimension in dimensions:
        print(dimension)

    dimensions = (400, 100)
    print("\nModified dimensions:")
    for dimension in dimensions:
        print(dimension)


def main():
    glava_2()
    glava_3()
    glava_4()


main()
