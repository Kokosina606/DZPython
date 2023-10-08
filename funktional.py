#Дополнить телефонный справочник возможностью изменения и удаления данных. 
#Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
#для изменения и удаления данных.

import os,re

def printData(data):
    phoneBook = []
    print(" №  Имя             Фамилия       Телефон")
    personID = 1

    for kontakt in data:
        name, lastName, phone = kontakt.rstrip().split(",")
        phoneBook.append(
            {
                "ID": personID,
                "name": name,
                "lastName": lastName,
                "phone": phone,
            }
        )
        personID += 1

    for kontakt in phoneBook:
        personID, name, lastName, phone = kontakt.values()
        print(f"{personID:>2}. {name:<10} {lastName:<15} -- {phone:<15}")




def showKontakts(fileName):
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)
    input("- нажмите Enter -")

def addKontakt(fileName):  # Функция добавления нового контакта в телефонную книгу
    with open(fileName, "a", encoding="UTF-8") as file:
        res = ""
        res += input("Введите имя: ") + ","
        res += input("Введите фамилию: ") + ","
        phone_number=input("Введите номер: ")
        flag = False
        while not flag:
            try:
                phone_number = input("Введите номер телефона: ")
                if len(str(phone_number)) != 11:
                    print('неверный ввод номера. Повторите.\n')
                else:
                    flag = True
            except ValueError:
                print('Ошибка.Неправильный формат номера')
        res += phone_number

        file.write(res + "\n")

    print('Контакт добавлен'+'\n')
    input("- нажмите Enter -")

def findKontakt(fileName):
    target = input("Введите данные для поиска: ")
    result = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = file.readlines()
        for person in data:
            if target in person:
                result.append(person)

    if len(result) != 0:
        printData(result)
    else:
        print(f"Такого контакта нет '{target}'.")

    input("- нажмите Enter -")

def changeKontakt(fileName):
    phoneBook = []
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberKontakt = int(
            input("Введите номер контакта для исправления: ")
        )
        print(data[numberKontakt - 1].rstrip().split(","))
        if numberKontakt != 0:
            newName = input("Введите новое имя: ")
            newLastName = input("Введите новую фамилию: ")
            flag = False
            while not flag:
                try:
                    newPhone = input("Введите новый телефона: ")
                    if len(str(newPhone)) != 11:
                        print('неверный ввод номера. Повторите.\n')
                    else:
                        flag = True
                except ValueError:
                    print('Ошибка.Неправильный формат номера')
            data[numberKontakt - 1] = (
                newName + "," + newLastName + "," + newPhone + "\n"
            )
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))
                print("\nКонтакт изменен!\n")
                input("- нажмите Enter -")
        else:
            return

def deleteKontakt(fileName):
    with open(fileName, "r+", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberKontakt = int(
            input("Введите номер контакта для удаления: ")
        )
        if numberKontakt != 0:
            print(f"Удаление контакта: {data[numberKontakt-1].rstrip().split(',')}\n")
            data.pop(numberKontakt - 1)
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))

        else:
            return
    input("- нажмите Enter -")


def main(file_name):
    while True:
        command = input('\nВведите команду:\nr-показать телефонную книгу\nw-добавить контакт\nc-изменить контакт\nd-удалить контакт\nf-найти контакт\nДля выхода напишите q\n')
        if command == 'q':
            break
        elif command == 'r':
            if not os.path.exists(file_name):
                print('Файл не создан')
                break
            showKontakts(file_name)
        elif command == 'w':
            if not os.path.exists(file_name):
                print('Файл не создан')
                break
            addKontakt(file_name)
        elif command == 'c':
            if not os.path.exists(file_name):
                print('Файл не создан')
                break
            changeKontakt(file_name)
        elif command == 'd':
            if not os.path.exists(file_name):
                print('Файл не создан')
                break
            deleteKontakt(file_name)
        elif command == 'f':
            if not os.path.exists(file_name):
                print('Файл не создан')
                break
            findKontakt(file_name)

path = "phonebook.txt"
main(path)