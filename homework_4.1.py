# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

from sys import argv


def salary():
    try:
        emp_hours, rate, bonus = map(float, argv[1:])
        print(f"Your salary is: {emp_hours * rate + bonus}")
    except ValueError:
        print('Enter 3 numbers')


salary()
