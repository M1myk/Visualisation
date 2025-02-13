import random

def generator_paroliv():
    list=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    n=random.randint(0,999999999)
    a=random.choice(list)
    print(n)



#амінь ножиці папір
def knp():
    list=['камінь','ножиці','папір']

    g = random.choice(list)
    n=str(input(f'Введи один із запропонованиї варіантів - {list}: '))
    print(f"Ваш вибір: {n}")
    print(f"Вибір комп'ютера: {g}")
    if n==g:
        print('Нічия!')
    elif n=='камінь':
        if g == 'ножиці':
            print('Ви виграли!')
        else:
            print('Компютер виграв!')
    elif n=='папір':
        if g == 'камінь':
            print('Ви виграли!')
        else:
            print('Компютер виграв!')
    else:
        print('Ви ввели неправильний варіант!')



# Вгадай число
def vgadaj():
    n = random.randint(1, 10)
    a = int(input('Вгадай число яке я загадав від 1 до 10: '))
    if a == n:
        print('Правильно!' * 1)
    else:
        print(f'Неправльно, спробуй ще раз.\n')
        return main()

def zad3():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for num in a:
        if num < 5:
            print(num)

def zad4():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    result = list(filter(lambda elem: elem in b, a))
    print(result)


def main():
    vgadaj()
    generator_paroliv()
    knp()
    zad3()
    zad4()

main()



