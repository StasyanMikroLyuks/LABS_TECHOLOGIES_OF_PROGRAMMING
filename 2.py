# ·Найти элемент и его индексы, сумма цифр которого максимальна.
import tkinter as tk


def find_max_digit_sum_element():
    input_matrix = input_text.get("1.0", "end-1c")

    try:
        # Преобразуем введенную строку в список списков (матрицу)
        matrix = [list(map(int, row.split()))
                  for row in input_matrix.strip().split('\n')]

        max_digit_sum = 0  # Инициализируем максимальную сумму цифр
        max_element = None  # Инициализируем элемент с максимальной суммой цифр
        max_indices = None  # Инициализируем индексы элемента
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                num = matrix[i][j]
                digit_sum = sum(int(digit)
                                for digit in str(abs(num)))  # Сумма цифр числа
                if digit_sum > max_digit_sum:
                    max_digit_sum = digit_sum
                    max_element = num
                    max_indices = (i, j)

        # Очищаем поле вывода и выводим результат
        output_text.delete("1.0", "end")
        if max_element is not None and max_indices is not None:
            output_text.insert("1.0", "Максимальная сумма цифр: {}\nЭлемент: {}\nИндексы: {}".format(max_digit_sum,
                               max_element,                                                                                                     max_indices))
        else:
            output_text.insert(
                "1.0", "Матрица пуста или не содержит целых чисел.")
    except ValueError:
        output_text.delete("1.0", "end")
        output_text.insert(
            "1.0", "Ошибка: Пожалуйста, введите корректную матрицу целых чисел.")


# Создаем графический интерфейс
root = tk.Tk()
root.title("Поиск элемента с максимальной суммой цифр и его индексов")

input_label = tk.Label(root, text="Введите матрицу:")
input_label.pack()

input_text = tk.Text(root, height=5, width=30)
input_text.pack()

find_button = tk.Button(root, text="Найти", command=find_max_digit_sum_element)
find_button.pack()

output_label = tk.Label(root, text="Результат:")
output_label.pack()

output_text = tk.Text(root, height=3, width=30)
output_text.pack()

root.mainloop()
