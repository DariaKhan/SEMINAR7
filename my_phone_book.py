import os

contacts = []

def import_contacts(filename):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                last_name, first_name, patronymic, phone = line.strip().split(',')
                contacts.append({"last_name": last_name, "first_name": first_name, "patronymic": patronymic, "phone": phone})
        print("Контакты успешно импортированы")
    else:
        print("Файл не найден")

def export_contacts(filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for contact in contacts:
            file.write(f'{contact["last_name"]},{contact["first_name"]},{contact["patronymic"]},{contact["phone"]}\n')
    print("Контакты успешно экспортированы")

def add_contact(last_name, first_name, patronymic, phone):
    contacts.append({"last_name": last_name, "first_name": first_name, "patronymic": patronymic, "phone": phone})
    print("Контакт успешно добавлен")

def search_contacts(query):
    found_contacts = [contact for contact in contacts if query.lower() in contact["last_name"].lower() or query.lower() in contact["first_name"].lower() or query.lower() in contact["patronymic"].lower() or query in contact["phone"]]
    if found_contacts:
        for contact in found_contacts:
            print(f'{contact["last_name"]} {contact["first_name"]} {contact["patronymic"]} {contact["phone"]}')
    else:
        print("Контакты не найдены")

def display_contacts():
    if contacts:
        print("\nТЕЛЕФОННЫЙ СПРАВОЧНИК")
        print("-" *60) 
        header = f"{'Фамилия':<15}{'Имя':<10}{'Отчество':<15}{'Телефон':<15}"
        print(header)
        print("-" *60) 
        
        for contact in contacts:
            print(f'{contact["last_name"]:<15}{contact["first_name"]:<10}{contact["patronymic"]:<15}{contact["phone"]:<15}')
    else:
        print("Контактов нет")


def delete_contact_by_last_name(last_name_to_delete):
    global contacts
    initial_count = len(contacts)
    contacts = [contact for contact in contacts if contact["last_name"].lower() != last_name_to_delete.lower()]
    if len(contacts) < initial_count:
        print("Контакт успешно удален")
    else:
        print("Контакт с такой фамилией не найден")

def main_menu():
    while True:
        print("\nМЕНЮ СПРАВОЧНИКА")
        print("-" * 65) 
        print(f"{'№':<3}{'Действие':<25}{'Описание':<100}")
        print("-" * 65)  
        print(f"{'1':<3}{'Импорт контактов':<25}{'Загрузить контакты из файла':<100}")
        print(f"{'2':<3}{'Экспорт контактов':<25}{'Сохранить контакты в файл':<100}")
        print(f"{'3':<3}{'Добавить контакт':<25}{'Добавить новый контакт в справочник':<100}")
        print(f"{'4':<3}{'Поиск контактов':<25}{'Найти контакты по критериям':100}")
        print(f"{'5':<3}{'Показать контакты':<25}{'Отобразить все сохраненные контакты':<100}")
        print(f"{'6':<3}{'Удалить контакт':<25}{'Удалить контакт по фамилии':<100}")
        print(f"{'0':<3}{'Выход':<25}{'Закрыть телефонный справочник':<100}")
        print("-" * 65)  
        choice = input("Выберите действие: ")
        
        if choice == "1":
            filename = input("Введите имя файла для импорта: ")
            import_contacts(filename)
        elif choice == "2":
            filename = input("Введите имя файла для экспорта: ")
            export_contacts(filename)
        elif choice == "3":
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            patronymic = input("Введите отчество: ")
            phone = input("Введите номер телефона: ")
            add_contact(last_name, first_name, patronymic, phone)
        elif choice == "4":
            query = input("Введите поисковый запрос: ")
            search_contacts(query)
        elif choice == "5":
            display_contacts()
        elif choice == "6":
            last_name_to_delete = input("Введите фамилию контакта для удаления: ")
            delete_contact_by_last_name(last_name_to_delete)
        elif choice == "0":
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main_menu()
