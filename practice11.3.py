import csv


def read_and_calculate_expenses(filename):
    total = 0
    print("Нужно купить:")

    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Пропускаем заголовок

        for row in reader:
            product, quantity, price = row
            total += int(quantity) * int(price)
            print(f"{product} - {quantity} шт. за {price} руб.")

    print(f"\nИтоговая сумма: {total} руб.")


read_and_calculate_expenses('1.csv')