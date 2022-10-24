def start():
    print('-----------------------------')
    print()
    print('          Привет!')
    print()
    print(' Давай сыграем в одну игру...')
    print()
    print('        ДА НАЧНУТСЯ')
    print()
    print('   "!!!КРЕСТИКИ-НОЛИКИ!!!"')
    print()
    print('------------------------------')
    print()
    global cross
    cross = input('Представься, Игрок1: ')
    print(f'Добро пожаловать, {cross}!')
    print()
    global null
    null = input('Игрок2, назовись:')
    print(f'Приветствую тебя, {null}!')
    print()
    print('Правила просты:')
    print('Выбираешь клетку,')
    print('вводишь координаты,')
    print('собираешь линию из трех одинаковых символов и...')
    print('ПОБЕЖДАЕШЬ')
    print('ну или лажаешь, если тебя опередит оппонент.')
    print()
    print(f'{cross}, {null}, поехали!')


def wire():
    print('    | 0 | 1 | 2 |')
    print('    -------------')
    for i, row in enumerate(cage):
        row_line = f"  {i} | {' | '.join(row)} | "
        print(row_line)
        print('    -------------')
    print()


def rules():
    while True:
        cords = input('Выбери позицию:').split()

        if len(cords) != 2:
            print('Введи две координаты!')
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print('Алё, разве это числа!?')
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Ты промахнулся мимо поля!')
            continue

        if cage[x][y] != " ":
            print('ЗАНЯТО!')
            continue

        return x, y


def winner():
    wins = (
            ((0, 0), (0, 1), (0, 2)),
            ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)),
            ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)),
            ((0, 2), (1, 2), (2, 2)),
            ((0, 0), (1, 1), (2, 2)),
            ((2, 0), (1, 1), (0, 2))
            )

    for cord in wins:
        symbols = []
        for a in cord:
            symbols.append(cage[a[0]][a[1]])
        if symbols == ['X', 'X', 'X']:
            print(f'Победа твоя, {cross}!')
            return True
        if symbols == ['O', 'O', 'O']:
            print(f'{null}, поздравляю с победой!')
            return True


start()
cage = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    wire()
    if count % 2 == 1:
        print(f'Жги, {cross}!')
    else:
        print(f'{null}, твоя очередь!')

    x, y = rules()

    if count % 2 == 1:
        cage[x][y] = 'X'
    else:
        cage[x][y] = 'O'

    if winner():
        break

    if count == 9:
        print('Ничья!')
        break
