import csv

input_file = "gdp_per_capita.csv"   # твій CSV-файл
output_file = "gdp_per_capita_2016_filtered.csv"

try:
    with open(input_file, encoding="utf-8") as file:
        reader = csv.reader(file)
        data = list(reader)

        # перший рядок — заголовки
        headers = data[0]

        # знаходимо колонку з роком 2016 (вона має формат "2016 [YR2016]")
        year_index = None
        for i, col in enumerate(headers):
            if "2016" in col:
                year_index = i
                break

        if year_index is None:
            raise ValueError("Не знайдено колонку з роком 2016")

        print("Файл успішно відкрито!")
        print("Назви стовпців:", headers)
        print()

        # Отримуємо поріг від користувача
        limit = float(input("Введіть мінімальне значення GDP per capita (current US$): "))

        results = [["Country Name", "Country Code", "Series Name", "2016"]]

        # Обробляємо дані
        for row in data[1:]:
            try:
                country = row[0]
                code = row[1]
                indicator = row[2]
                value = row[year_index]

                if value and float(value) > limit:
                    results.append([country, code, indicator, value])
            except (ValueError, IndexError):
                continue

        # Виводимо результати
        for r in results:
            print(r)

        # Записуємо у новий CSV
        with open(output_file, "w", newline="", encoding="utf-8") as out_file:
            writer = csv.writer(out_file)
            writer.writerows(results)

        print(f"\nРезультати записано у файл: {output_file}")

except FileNotFoundError:
    print("Помилка: файл не знайдено. Переконайтеся, що він у тій самій папці, що й програма.")
except Exception as e:
    print("Виникла неочікувана помилка:", e)
