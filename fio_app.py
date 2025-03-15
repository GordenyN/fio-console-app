import bisect

def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return sorted(line.strip() for line in file)
    except FileNotFoundError:
        print("Файл не найден.")
        return []

def save_file(filename, names):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(names))

def search_names(names, query):
    return [name for name in names if query.lower() in name.lower()]

def add_name(names, new_name):
    bisect.insort(names, new_name)
    return names

def delete_name(names, query):
    matches = search_names(names, query)
    if not matches:
        print("Совпадений не найдено.")
        return names
    
    while True:
        print("Найденные записи:")
        for i, name in enumerate(matches, 1):
            print(f"{i}. {name}")
        
        choice = input("Введите точное ФИО для удаления или новую подстроку для поиска: ").strip()
        if choice in matches:
            names.remove(choice)
            print(f"Удалено: {choice}")
            return names
        matches = search_names(names, choice)
        if not matches:
            print("Совпадений не найдено.")

if __name__ == "__main__":
    filename = input("Введите имя файла: ")
    names = read_file(filename)
    
    try:
        while True:
            print("\nМеню:")
            print("1. Поиск ФИО")
            print("2. Добавить ФИО")
            print("3. Удалить ФИО")
            print("4. Выйти")
            
            choice = input("Выберите действие: ")
            
            if choice == "1":
                query = input("Введите подстроку для поиска: ")
                results = search_names(names, query)
                print("\nРезультаты поиска:")
                for name in results:
                    print(name)
            elif choice == "2":
                new_name = input("Введите новое ФИО: ")
                names = add_name(names, new_name)
                save_file(filename, names)
                print("ФИО добавлено.")
            elif choice == "3":
                query = input("Введите подстроку для удаления: ")
                names = delete_name(names, query)
                save_file(filename, names)
            elif choice == "4":
                print("Выход из программы.")
                break
            else:
                print("Неверный ввод, попробуйте снова.")
    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем.")
