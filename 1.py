whiletru = True
while whiletru:
    def inputcontact():
        with open('spravochnik.txt', 'a', encoding ='utf-8') as file:
            str = input("введите ФИО и номер телефона через пробле: ")
            file.write(str + '\n')
            print('пользователь внесен в телефонную книгу')
            print()
            

    def searchcontact ():
        desired = input("Введите имя или телефон человека: ")
        with open('spravochnik.txt', 'r', encoding = 'utf-8') as file:
            contacts = file.read()
            contacts = contacts.split("\n")
            search = list(filter(lambda x: desired in x, contacts))
            if search == []:
                print("человек не найден")
                print()
            else:
                print(*search)
                print()
                

    def fulllist():
        with open('spravochnik.txt', 'r', encoding = 'utf-8') as file:
            txt = file.read()
            print(txt)
            print()

        
    print("введите команду СПИСОК для вывода всех контактов")
    print("введите команду ВВОД для добавления контакта")
    print("введите команду ПОИСК для поиска контакта в списке")
    print("введите команду ВЫХОД для выхода из программы")
    choise = input()
    if choise.upper() == 'ВВОД':
        inputcontact()
    elif choise.upper() == 'ПОИСК':
        searchcontact ()
    elif choise.upper() == 'ВЫХОД':
        whiletru = False
    elif choise.upper() == "СПИСОК":
        fulllist()

