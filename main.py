from application.salary import calculate_salary
from application.db import people as p
from datetime import datetime

if __name__ == '__main__':
    calculate_salary()
    p.get_employees()
    now = datetime.now()
    print(now.date())