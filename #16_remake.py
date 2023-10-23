class EmailAlreadyExistsException(Exception):
    pass


def validate(self):
    with open('emails.csv)', 'r') as file:
        emails = file.read().splitlines()
        if self.email in emails:
            raise EmailAlreadyExistsException('Email already exists in the file.')

class Employee:
    def __init__(self, name, salary_per_day, email):
        self.name = name
        self.salary_per_day = salary_per_day
        self.email = email
        self.validate()
        self.save_email()

    def __str__(self):
        return f"Job: {self.__class__.__name__}, Name: {self.name}, Salary per day: {self.salary_per_day}"

    def work(self):
        return 'I come to the office.'

    def check_salary(self, days):
        self.days = days
        self.salary_per_days = self.days * self.salary_per_day

    def __lt__(self, other):
        return self.salary_per_day < other.salary_per_day
        return self.leng < other.leng

    def __gt__(self, other):
        return self.salary_per_day > other.salary_per_day
        return self.leng > other.leng

    def __eq__(self, other):
        return self.salary_per_day == other.salary_per_day
        return self.leng == other.leng

    def save_email(self):
        with open('emails.csv)', 'a') as file:
            file.write(self.email + '\n')




class Recruiter(Employee):
    def work(self):
        return 'I come to the office and start to hiring.'


class Developer(Employee):
    def __init__(self, name, salary_per_day, tech, email):
        super().__init__(name, tech, email)
        self.salary_per_day = salary_per_day
        self.tech = tech
        leng = len(tech)

    def __str__(self):
        return f"Job: {self.__class__.__name__}, Name: {self.name}, Salary per day: {self.salary_per_day}, Tech: {self.tech}"

    def work(self):
        return 'I come to the office and start to coding.'

    def _add__(self, other):
        if self.salary_per_day > other.salary_per_day:
            salary_per_day = self.salary_per_day
        else:
            salary_per_day = other.salary_per_day
        return Developer(name=(self.name + other.name), salary_per_day=salary_per_day,
                         tech=set((self.tech + other.tech)), email='developer2@gmail.com')


employee1 = Employee("Terry", 35, 'employee1@gmail.com')
employee = Employee("Kate", 30, 'employee@gmail.com')
recruiter = Recruiter("Alex", 100, 'recruiter@gmail.com')
recruiter1 = Recruiter("Tom", 140, 'recruiter1@gmail.com')
developer = Developer("Ben", 120, ('Python', 'HTML', 'CSS', 'JS'), 'developer@gmail.com')
developer1 = Developer("Mick", 160, ('Python', 'JS', 'SQL', 'Ruby'), 'developer1@gmail.com')

print(employee < employee1)  # Сравнение employee по уровню ЗП
print(employee < employee1)  # Сравнение employee по уровню ЗП
print(employee > employee1)  # Сравнение employee по уровню ЗП
print(employee == employee1)  # Сравнение employee по уровню ЗП
print(developer > developer1)  # Сравнение Developer за кол-вом технологий

employee.check_salary(22)  # Кол-во рабочих дней
print(employee.salary_per_days)  # ЗП за заданное кол-во дней

print(employee.work())  # Вывод значений для employee
print(recruiter.work())  # Вывод значений для recruiter
print(developer.work())  # Вывод значений для developer

print(employee)  # Вывод информации о employee
print(employee1)  # Вывод информации о employee1
print(recruiter)  # Вывод информации о recruiter
print(developer)  # Вывод информации о developer
print(recruiter1)  # Вывод информации о recruiter1
print(developer1)  # Вывод информации о developer1

developer2 = developer1._add__(developer)  # Конкатенация developer1 и developer
print(developer2)  # Вывод информации о developer2



