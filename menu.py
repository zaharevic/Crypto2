from tabnanny import check

from algorithnms import algorithm


class menu:
    def __init__(self):
        print("==Проверка штрих-кода в формате EAN-13==\n")

    def start_menu(self):
        flag = True
        try:
            while flag:
                a = int(input("Меню:\n"
                          "1. Проверить корректность штрих кода.\n"
                          "2. Вычислить контрольную цифру\n"
                          "3. Выход\n"
                          "Выбертие операцию:\n"))
                if a == 1:
                    self.check()
                elif a == 2:
                    self.find()
                elif a == 3:
                    print("Завершение работы!")
                    flag = False
                else:
                    "Ошибка! Вы ввели некорректную цифру!"
        except ValueError:
            print("Ошибка! Вы ввели некорректный символ")

    def check(self):
        flag = True
        algo = algorithm()

        while flag:
            ans = list(input("Введите код:"))
            try:
                if len(ans) == 13:
                    res = []
                    for i in ans:
                        res.append(int(i))
                    if algo.check(res):
                        print("Данный код является корректным!")
                    else:
                        print("Данный код НЕ является корректным!")
                    flag = False
                else:
                    print("Ошибка! Код введен не полностью!")
            except ValueError:
                print('Ошибка! Введен некорректный символ')

    def find(self):
        flag = True
        algo = algorithm()

        while flag:
            ans = list(input("Введите код без контрольной цифры:"))
            try:
                if len(ans) == 12:
                    res = []
                    for i in ans:
                        res.append(int(i))
                    print(f'Контрольная цифра: {algo.find(res)}')
                    flag = False
                else:
                    print("Ошибка! Код введен не полностью!")
            except ValueError:
                print('Ошибка! Введен некорректный символ')

menu().start_menu()