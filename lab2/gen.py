import csv
from faker import Faker
import random

fake = Faker('ru_RU')


def generate_csv(row_cnt: int) -> None:
    """Генерирует csv файл с случайными данными с заданным количеством
    :rtype: None
    :param row_cnt:
    """
    with open('data.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile, delimiter=";", quoting=csv.QUOTE_ALL)
        for i in range(row_cnt):
            writer.writerow([get_name(), get_job(), get_department(), get_review(), get_salary()])


def get_name():
    """Генерирует случайное имя"""
    return fake.name()


def get_job():
    """Генерирует случайную должность"""
    return fake.job()


def get_department():
    """Генерирует случайный отдел из списка"""
    departments = ['Отдел разработки',
                   'Отдел кадров',
                   'Отдел коммерции',
                   'Отдел CRM',
                   'Отдел развития',
                   'Отдел отдыха',
                   'Отдел финансов']
    return departments[random.randint(0, len(departments) - 1)]


def get_review():
    """Генерирует случайную оценку сотрудника"""
    return random.randint(1, 5)


def get_salary():
    """Генерирует случайную зарплату от 50 до 250 тысяч"""
    return random.randint(50000, 250000)


if __name__ == '__main__':
    row_count = int(input("Введите число строк: "))
    generate_csv(row_count)

