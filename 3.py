# Найти номера строк матрицы, суммы произведений ненулевых цифр которых делятся на 5.
import tkinter as tk


def find_rows_with_divisible_sum():
    input_matrix = input_text.get("1.0", "end-1c")

    try:
        # Преобразуем введенную строку в список списков (матрицу)
        matrix = [list(map(int, row.split()))
                  for row in input_matrix.strip().split('\n')]

        rows_with_divisible_sum = []  # Инициализируем список для номеров строк

        for i in range(len(matrix)):
            row_product = 1  # Инициализируем произведение ненулевых цифр строки
            for j in range(len(matrix[i])):
                num = matrix[i][j]
                while num != 0:
                    digit = num % 10
                    if digit != 0:
                        row_product *= digit
                    num //= 10
            if row_product % 5 == 0:
                rows_with_divisible_sum.append(i)

        # Очищаем поле вывода и выводим результат
        output_text.delete("1.0", "end")
        if rows_with_divisible_sum:
            output_text.insert("1.0", "Номера строк с суммой произведений ненулевых цифр, делящейся на 5: {}".format(
                rows_with_divisible_sum))
        else:
            output_text.insert(
                "1.0", "Нет строк с суммой произведений ненулевых цифр, делящейся на 5.")
    except ValueError:
        output_text.delete("1.0", "end")
        output_text.insert(
            "1.0", "Ошибка: Пожалуйста, введите корректную матрицу целых чисел.")


# Создаем графический интерфейс
root = tk.Tk()
root.title(
    "Поиск строк матрицы с суммой произведений ненулевых цифр, делящейся на 5")

input_label = tk.Label(root, text="Введите матрицу:")
input_label.pack()

input_text = tk.Text(root, height=5, width=30)
input_text.pack()

find_button = tk.Button(
    root, text="Найти", command=find_rows_with_divisible_sum)
find_button.pack()

output_label = tk.Label(root, text="Результат:")
output_label.pack()

output_text = tk.Text(root, height=2, width=30)
output_text.pack()

root.mainloop()
