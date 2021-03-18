import csv

def ui():
    """Предоставляет пользователю меню"""
    option = ""
    options = {'1', '2', '3', '4'}
    while option not in options:
        print("--------------------------------------\n"
              "1. Показать все отделы\n"
              "2. Показать сводный отчёт по отделам\n"
              "3. Сохранить сводный отчёт в виде csv\n"
              "4. Закрыть\n")
        option = input()
    return option


def run_cycle():
    """Осуществляет взаимодействие с пользователем"""
    while 1:
        option = ui()
        if option == '1':
            show_depts()
        elif option == '2':
            rep_print()
        elif option == '3':
            rep_save()
        elif option == '4':
            break


def rep_gen() -> list:
    """Создает сводный отчет"""
    departments = list(get_depts())
    option = []
    depts_salaries = {departments[i]: [] for i in range(len(departments))}

    with open('data.csv', newline='') as csvFile:
        reader = csv.reader(csvFile, delimiter=';')
        for row in reader:
            depts_salaries.get(row[2]).append(int(row[4]))
        for dept, salaries in depts_salaries.items():
            option.append([dept, str(len(salaries)),
                           str(min(salaries)),
                           str(max(salaries)),
                           str(round(sum(salaries) / len(salaries)))])
        return option


def get_depts():
    """Возвращает отделы"""
    option = set('')
    with open('data.csv', newline='') as csvFile:
        reader = csv.reader(csvFile, delimiter=';')
        for row in reader:
            option.add(row[2])
        return option


def show_depts():
    """Выводит список отделов"""
    print()
    depts = get_depts()
    for dept in depts:
        print(dept)


def rep_print():
    """Выводит отчет в консоль"""
    print()
    report = rep_gen()
    for r in report:
        print(r[0] + ": сотрудников: " + r[1] + "; амплитуда зарплат: " + r[2] + " - " + r[3] + "; средняя зарплата: " +
              r[4])


def rep_save():
    """Сохраняет сводный отчет в csv файл"""
    report = rep_gen()
    with open('report.csv', 'w', newline='') as resultFile:
        writer = csv.writer(resultFile, delimiter=';', quoting=csv.QUOTE_ALL)
        writer.writerow(["Отдел", "Количество сотрудников", "Минимальная зарплата",
                         "Максимальная зарплата", "Средняя зарплата"])
        writer.writerows(report)
        print("Отчет сформирован")


if __name__ == '__main__':
    run_cycle()
