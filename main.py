from datetime import datetime

from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    print(datetime.today().strftime(f'Текущая дата: %d.%m.%Y - %H:%M:%S'))
    calculate_salary()
    get_employees()
