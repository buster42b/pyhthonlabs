import csv


def print_menu():
    """Предоставляет пользователю меню"""
    res = ""
    while (res not in ['1', '2', '3']):
        print("-------------------------------------")
        print("1. Вывести все отделы")
        print("2. Вывести сводный отчет")
        print("3. Сохранить сводный отчет в csv")
        res = input("Введи пункт меню: ")
    if (res == '1'):
        print_all_departments()
    elif (res == '2'):
        print_report()
    elif (res == '3'):
        save_report()
    else:
        print("Неправильное значение")


def print_all_departments():
    """Печатает список отделов"""
    print()
    departments = get_departments()
    for dept in departments:
        print(dept)


def print_report():
    """Печатает сводный отчет"""
    print()
    report = generate_report()
    for r in report:
        print(r[0] + ": численность: " + r[1] + "; вилка: " + r[2] + " - " + r[3] + "; средняя зарплата: " + r[4])


def save_report():
    """Сохраняет сводный отчет в csv файл"""
    report = generate_report()
    with open('report.csv', 'w', newline='') as resultFile:
        writer = csv.writer(resultFile, delimiter=';', quoting=csv.QUOTE_ALL)
        writer.writerow(["Отдел", "Количество сотрудников", "Минимальная зарплата",
                         "Максимальная зарплата", "Средняя зарплата"])
        writer.writerows(report)
        print("Отчет сформирован")


def generate_report() -> list:
    """
    Генерирует сводный отчет
    :rtype: list
    """
    departments = list(get_departments())
    res = []
    depts_salaries = {departments[i]: [] for i in range(len(departments))}

    with open('data.csv', newline='') as csvFile:
        reader = csv.reader(csvFile, delimiter=';')
        for row in reader:
            depts_salaries.get(row[2]).append(int(row[4]))
        for dept, salaries in depts_salaries.items():
            res.append([dept, str(len(salaries)),
                        str(min(salaries)),
                        str(max(salaries)),
                        str(round(sum(salaries) / len(salaries)))])
        return res


def get_departments():
    """Возвращает множество отделов"""
    res = set('')
    with open('data.csv', newline='') as csvFile:
        reader = csv.reader(csvFile, delimiter=';')
        for row in reader:
            res.add(row[2])
        return res


if __name__ == '__main__':
    print_menu()
