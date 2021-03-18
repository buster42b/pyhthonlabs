import csv
from faker import Faker
import random

fake = Faker('ru_RU')


def csv_gen(rows: int) -> None:
    """Создает csv с заданным набором строк"""
    with open('data.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile, delimiter=";", quoting=csv.QUOTE_ALL)
        for i in range(rows):
            writer.writerow([employee(), occupation(), department(), grade(), pay()])


def employee():
    """Возвращает рандомное имя из fake"""
    return fake.name()


def occupation():
    """Возвращает рандомную должность из списка"""
    return fake.job()


def department():
    """Возвращает рандомное место работы из списка"""
    dept = ['Бухгалтерия',
            'Связи с общественностью',
            'Разработка',
            'Маркетинг',
            'Креативный отдел',
            'Тестирование']
    return dept[random.randint(0, len(dept) - 1)]


def grade():
    """Генерирует случайную оценку сотрудника"""
    return random.randint(1, 5)


def pay():
    """Определяет зарплату в диапазоне от 30 до 300 тысяч"""
    return random.randint(30000, 300000)


if __name__ == '__main__':
    lines = int(input("Количество сотрудников: "))
    csv_gen(lines)
