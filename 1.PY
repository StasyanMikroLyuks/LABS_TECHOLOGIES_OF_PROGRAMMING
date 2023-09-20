# Вычислить произведение четных элементов верхней треугольной матрицы.
import tkinter as tk


def calculate_product():
    input_matrix = input_text.get("1.0", "end-1c")

    try:
        # Преобразуем введенную строку в список списков (матрицу)
        matrix = [list(map(int, row.split()))
                  for row in input_matrix.strip().split('\n')]

        product = 1  # Инициализируем произведение
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                if matrix[i][j] % 2 == 0:
                    product *= matrix[i][j]

        # Очищаем поле вывода и выводим результат
        output_text.delete("1.0", "end")
        output_text.insert(
            "1.0", "Произведение четных элементов верхней треугольной матрицы: {}".format(product))
    except ValueError:
        output_text.delete("1.0", "end")
        output_text.insert(
            "1.0", "Ошибка: Пожалуйста, введите корректную матрицу целых чисел.")


# Создаем графический интерфейс
root = tk.Tk()
root.title("Вычисление произведения четных элементов верхней треугольной матрицы")

input_label = tk.Label(root, text="Введите матрицу:")
input_label.pack()

input_text = tk.Text(root, height=5, width=30)
input_text.pack()

calculate_button = tk.Button(root, text="Вычислить", command=calculate_product)
calculate_button.pack()

output_label = tk.Label(root, text="Результат:")
output_label.pack()

output_text = tk.Text(root, height=1, width=30)
output_text.pack()

root.mainloop()
