def print_field(fileld):
    x=0
    while x<15:
        print(fileld[x:x+4])
        x+=4

def winner(field,side):
    x = "x" if side else "o"
    a = field[5] == field[6] == field [7] == x
    b = field[9] == field[10] == field[11] == x
    c = field[13] == field[14] == field[15] == x
    d = field[5] == field[9] == field[13] == x
    e = field[6] == field[10] == field[14] == x
    f = field[7] == field[11] == field[15] == x
    i = field[5] == field[10] == field[15] == x
    j = field[7] == field[10] == field[13] == x
    return any([a,b,c,d,e,f,i,j])

def choose_side():
    side = ""
    while str.lower(side) not in ["x","o","0"]:
        side = input("Выберете сторону (введите 'х' или 'о'): \n")
        return str.lower(side) == "x" if str.lower(side) in ["x","o","0"] else print("Введены некорректные данные. Повторите ввод.")

def choose_step(field):
    while True:
        step_string = input("Введите через пробел номер строки и стобца, куда вы хотите поставить {x}: \n")
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

def ai_step(field):
    print("Отлично. Мой ход!")
    return 15

def game_process(side):
    global field
    print_field(field)
    x, y = ("x", "o") if side else ("o", "x")
    while not winner(field,not side):
        if side:
            field[choose_step(field)] = x
        else:
            field[ai_step(field)] = y
        side = not side
        print_field(field)
    return not side


field = ["",0,1,2,0,"-","-","-",1,"-","-","-",2,"-","-","-"]
field1 = ["",0,1,2,0,"x","-","-",1,"x","-","-",2,"-","-","-"]

side = choose_side()
print(side)
if game_process(side):
    print("Поздравляем, вы победили!")
else:
    print("Увы, вы проиграли.")
#print_field(field1)
#print(winner(field1,side))
#x = "x" if side else "o"
#field1[choose_step(field1)] = x
#print_field(field1)
#print(winner(field1,side))