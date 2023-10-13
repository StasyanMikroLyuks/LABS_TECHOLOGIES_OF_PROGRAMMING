# Постpоить класс для pаботы с многочленами. Класс должен включать соответствующие поля:
# порядок, набор коэффициентов.
# Класс должен обеспечивать пpостейшие функции для pаботы с данными классами:
# вычисление значения многочлена для данного параметра,
# вывод многочлена в удобной форме и т.д.
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox


class КалькуляторМногочлена:
    def __init__(self, master):
        self.master = master
        master.title("Калькулятор Многочлена")

        self.label_coefficients = Label(
            master, text="Введите коэффициенты (через пробел):")
        self.entry_coefficients = Entry(master)
        self.label_x = Label(master, text="Введите x:")
        self.entry_x = Entry(master)
        self.button_calculate = Button(
            master, text="Вычислить", command=self.calculate)
        self.label_result = Label(master, text="Результат:")
        self.label_polynomial = Label(master, text="Многочлен:")

        self.label_coefficients.pack()
        self.entry_coefficients.pack()
        self.label_x.pack()
        self.entry_x.pack()
        self.button_calculate.pack()
        self.label_result.pack()
        self.label_polynomial.pack()

    def calculate(self):
        try:
            coefficients = [float(coeff.strip())
                            for coeff in self.entry_coefficients.get().split(' ')]
            x = float(self.entry_x.get())
            result = self.evaluate_polynomial(coefficients, x)
            self.label_result.config(text=f"Результат: {result}")

            # Выводим многочлен в удобной форме
            polynomial_str = self.display_polynomial(coefficients)
            self.label_polynomial.config(text=f"Многочлен: {polynomial_str}")

        except ValueError:
            messagebox.showerror(
                "Ошибка", "Неверный ввод. Пожалуйста, введите корректные коэффициенты и значение x.")

    @staticmethod
    def evaluate_polynomial(coefficients, x):
        result = 0  # cчётчик для накопления суммы
        for i, coeff in enumerate(coefficients):
            # пройтись по всем элементам списка coefficients.
            # coeff переменная которая будет содержать значение текущего элемента в списке(коэффициент)
            # enumerate возвращает пары (индекс, значение) для каждого элемента в списке.
            # пример coefficients = [1, 2, 3], тогда переменная coeff
            # содержит под индекасами 0:коэфф 1, 1:2, 2:3
            result += coeff * (x ** i)
            # += сложение с присваиванием,
            # 2, 4, 5, 6
            # x=2
            # 2*2^0+4*2^1+5*2^2+6*2^3=48+20+8+2=78
        return result

    @staticmethod
    def display_polynomial(coefficients):
        terms = []  # создание пустой список
        # пройтись по списку в обратном порядке
        for i, coeff in enumerate(coefficients[::-1]):
            # от старшей к младшей
            # Проверяет, что текущий коэффициент не равен нулю.
            if coeff != 0:
                # Это делается для исключения нулевых членов многочлена из вывода.
                term = f"{coeff}x^{len(coefficients) - i - 1}"
                # f = f-строка, коэффициент, x^
                terms.append(term)  # добавление в переменную terms термов
        return " + ".join(terms)
    # Возврат строки, в которой все члены многочлена объединены знаками " + ".


root = tk.Tk()
app = КалькуляторМногочлена(root)
root.mainloop()

# например при коэффициентах 2, 4, 5 ,6
# x = 2
# многочлен 6*x^3+5*x^2+4*x^1+2*x^0
# 6*8+5*4+4*2+2=48+20+8+2=78
