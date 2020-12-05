#Исходное игровое поле
field = [" ",0,1,2,0,"-","-","-",1,"-","-","-",2,"-","-","-"]
#Список строк, стобцов и диагоналей нашего поля
strikes = [(5,6,7),(9,10,11),(13,14,15),(5,9,13),(6,10,14),(7,11,15),(5,10,15),(7,10,13)]

#Выбор уровня сложности
def choose_diff():
    n = input('''Привет!
    Поддаваться тебе или хочешь по-серьезному?
    Введи 0, если хочешь победить.
    Если предел твоих мечтаний - ничья, - введи 1:
    ''')
    if n not in ["0", "1"]:
        print("Разве я могу не поддаваться тому, кто не справился даже с простейшим заданием?")
    return n == '1'

#Находит индекс первого свободного поля для хода компьютера
def find_first(field):
    for i in range(5,16):
        if field[i] == "-": return i

#Проверка наличия потенциально выигрышных/проигрышных ситуаций
def who_can_win(field):
    global strikes
    global side
    x, y = ("x", "o") if side else ("o", "x")
    for (a,b,c) in strikes:
        if any([field[a] == field[b] == y, field[a] == field [c] == y, field[b] == field[c] == y]):
            for i in (a,b,c):
                if field[i] == "-": return i
    for (a,b,c) in strikes:
        if any([field[a] == field[b] == x, field[a] == field [c] == x, field[b] == field[c] == x]):
            for i in (a,b,c):
                if field[i] == "-": return i
    return 0

#Вывод на экран текущего поля крестики-нолики
def print_field(field):
    x=0
    while x<15:
        printstr = ""
        a=x+4
        while x < a:
            printstr = printstr + " " + str(field[x]) + " "
            x+=1
        print(printstr)

#Проверка сложившейся на поле ситуации на предмет победы одного из игроков
def winner(field,side):
    x = "x" if side else "o"
    y = []
    global strikes
    for (a,b,c) in strikes:
        y.append(field[a] == field[b] == field [c] == x)
    return any(y)

#Функция выбора пользователем, чем он будет играть
def choose_side():
    side = ""
    while str.lower(side) not in ["x","o","0"]:
        side = input("Выберете сторону (введите 'х' или 'о'): \n")
        return str.lower(side) == "x" if str.lower(side) in ["x","o","0"] else print("Введены некорректные данные. Повторите ввод.")

#Функция принимает от пользователя адрес поля, куда он хочет походить,
#обрабатывает и возвращает значение индекса этого поля в списке
def choose_step(field):
    while True:
        step_string = input("Введите через пробел номер строки и столбца, куда вы хотите походить: \n")
        step=step_string.split()
        if 0<=int(step[0])<=2 and 0<=int(step[1])<=2:
            a = int(step[0])*4+5+int(step[1])
            if field[a] == "-":
                break
            else:
                print("Данное поле уже занято. Повторите ввод.")
        else:
            print("Введены некорректные данные. Повторите ввод.")
    return a

#Проверка, не заполнилось ли поле
def full_field(field):
    return "-" not in field

#Функция определяет, куда походит AI, и возвращает значение индекса
def ai_step(field):
    global game_diff
    print("Отлично. Мой ход!")
    a=who_can_win(field)
    if a: return a
    if not game_diff: return find_first(field)
    return 15

#Функция предоставляет поочередно возможность ходить игрокам.
#Когда кто-то выигрывает, или заполняется поле, возвращает код победителя
def game_process(side):
    global field
    tor = side
    print_field(field)
    x, y = ("x", "o") if side else ("o", "x")
    while not(winner(field,not tor) or full_field(field)):
        if tor:
            field[choose_step(field)] = x
        else:
            field[ai_step(field)] = y
        tor = not tor
        print_field(field)
    return 2 if full_field(field) else int(not tor)

#Тело программы
game_diff = choose_diff()
if game_diff:
    print("Уровень сложности: Легендарный.")
else:
    print("Уровень сложности: Элементарный.")
side = choose_side()
result = game_process(side)
if result == 2:
    print("Ничья!")
elif result:
    print("Поздравляем, вы победили!")
else:
    print("Увы, вы проиграли.")