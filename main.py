from random import randint


def attack(char_name, char_class):
    damadg_mes = 'нанёс урон противнику равный'
    if char_class == 'warrior':
        return (f'{char_name} {damadg_mes} {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} {damadg_mes} {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} {damadg_mes} {5 + randint(-3, -1)}')
    return None


def defence(char_name, char_class):
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
    return None


def special(char_name, char_class):
    spels_mes = 'применил специальное умение'
    if char_class == 'warrior':
        return (f'{char_name} {spels_mes} «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} {spels_mes} «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} {spels_mes} «Защита {10 + 30}»')
    return None


def start_training(char_name, char_class):
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print(
        '''Введи одну из команд: attack — чтобы атаковать противника,
        defence — чтобы блокировать атаку противника или special —
        чтобы использовать свою суперсилу.'''
    )
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class():
    text_constan = (
        'Введи название персонажа, за которого хочешь играть:',
        'Воитель — warrior, Маг — mage, Лекарь — healer: ',
        'Воитель — дерзкий воин ближнего боя. Сильный, выносливый и отважный.',
        'Маг — находчивый воин дальнего боя. Обладает высоким интеллектом.',
        'Лекарь — могущественный заклинатель.'
        'Черпает силы из природы, веры и духов.',
        'Нажми (Y), чтобы подтвердить выбор, или любую',
        'другую кнопку, чтобы выбрать другого персонажа '
    )
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input(f'{text_constan[0]} {text_constan[1]}')
        if char_class == 'warrior':
            print(text_constan[2])
        if char_class == 'mage':
            print(text_constan[3])
        if char_class == 'healer':
            print(f'{text_constan[4]} {text_constan[5]}')
        approve_choice = input(f'{text_constan[6]} {text_constan[7]}').lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class()
    print(start_training(char_name, char_class))


if __name__ == '__main__':
    main()
