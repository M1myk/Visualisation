#prompt = "If you tell us who you are, we can personalize the messages you see."
#prompt += "\nWhat is your first name? "
#name = input(prompt)
#print(f"\nHello, {name}!")
#
#number = input("Enter a number, and I'll tell you if it's even or odd: ")
#number = int(number)
#if number % 2 == 0:
#    print(f"\nThe number {number} is even.")
#else:
#    print(f"\nThe number {number} is odd.")


#current_number = 1
#while current_number <= 5:
#    print(current_number)
#    current_number += 1
#
#prompt = "\nTell me something, and I will repeat it back to you:"
#prompt += "\nEnter 'quit' to end the program. "
#message = ""
#while message != 'quit':
#    message = input(prompt)
#    if message != 'quit':
#        print(message)

#active = True
#while active:
#    message = input(prompt)
#    if message == 'quit':
#        active = False
#    else:
#        print(message)


#promp = "\nPlease enter the name of a city you have visited:"
#promp += "\n(Enter 'quit' when you are finished.) "
#while True:
#    city = input(promp)
#    if city == 'quit':
#        break
#    else:
#        print(f'i would like to visit {city.title()}')


#current_number = 0
#while current_number < 10:
#    current_number += 1
#    if current_number % 2 == 0:
#        continue
#    print(current_number)
#
#
#default =(f'Якщо хочете зупинитись напишіть "Це все"')
#default += f'\nЗамовляйте страви: '
#
#while True:
#    message = input(default)
#    if message == 'Це все':
#        break
#    else:
#        print(f'{message} додано в замовлення !')


#age = 'Введіть свій вік: '
#
#while True:
#    message = int(input(age))
#    if message < 3:
#        print('Білет безплатний.')
#
#    elif message >= 3 and message < 12:
#        print('Білет коштує 100 грн')
#    else:
#        print('Білет коштує 200 грн.')


unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)


responses = {}
# Установка флага продолжения опроса.
polling_active = True
while polling_active:
# Запрос имени и ответа пользователя.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
# Ответ сохраняется в словаре:
    responses[name] = response
# Проверка продолжения опроса.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# Опрос завершен, вывести результаты.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
