import json

# ---------- ФУНКЦІЇ ----------

def load_data(filename):
    """Завантаження даних з JSON файлу"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(filename, data):
    """Збереження даних у JSON файл"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def show_data(data):
    """Виведення вмісту JSON"""
    if not data:
        print("Файл порожній або не знайдено даних.")
    else:
        for country in data:
            print(f"{country['name']} — Площа: {country['area']} км², "
                  f"Населення: {country['population']} млн, "
                  f"Частина світу: {country['continent']}")

def add_country(data):
    """Додавання нового запису"""
    name = input("Назва країни: ")
    area = float(input("Площа (км²): "))
    population = float(input("Населення (млн): "))
    continent = input("Частина світу: ")
    data.append({
        "name": name,
        "area": area,
        "population": population,
        "continent": continent
    })
    print("Країну додано успішно!")

def delete_country(data):
    """Видалення запису"""
    name = input("Введіть назву країни для видалення: ")
    for country in data:
        if country["name"].lower() == name.lower():
            data.remove(country)
            print(f"Країну {name} видалено.")
            return
    print("Країну не знайдено.")

def search_country(data):
    """Пошук країни за назвою"""
    name = input("Введіть назву країни для пошуку: ")
    for country in data:
        if country["name"].lower() == name.lower():
            print(f"Знайдено: {country}")
            return
    print("Країну не знайдено.")

def find_asia_africa(data):
    """Пошук країн в Африці або Азії"""
    result = [c["name"] for c in data if c["continent"].lower() in ["африка", "азія"]]
    if result:
        print("Країни, що знаходяться в Африці або Азії:")
        for name in result:
            print("-", name)
        save_data("result.json", result)
        print("Результат збережено у файл result.json")
    else:
        print("Серед заданих країн немає тих, що розташовані в Африці або Азії.")

# ---------- ГОЛОВНА ПРОГРАМА ----------

filename = "countries.json"
data = load_data(filename)

while True:
    print("\n--- МЕНЮ ---")
    print("1. Показати всі дані")
    print("2. Додати нову країну")
    print("3. Видалити країну")
    print("4. Пошук країни")
    print("5. Пошук країн в Африці або Азії (варіантне завдання)")
    print("6. Вихід")

    choice = input("Оберіть дію: ")

    if choice == "1":
        show_data(data)
    elif choice == "2":
        add_country(data)
        save_data(filename, data)
    elif choice == "3":
        delete_country(data)
        save_data(filename, data)
    elif choice == "4":
        search_country(data)
    elif choice == "5":
        find_asia_africa(data)
    elif choice == "6":
        save_data(filename, data)
        print("Дані збережено. Вихід із програми.")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
