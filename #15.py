class Employee:
    def __init__(self, name, salary_per_day):
        self.name = name
        self.salary_per_day = salary_per_day

    def work(self):
        return 'I come to the office.'

    def __str__(self):
        return f"Job: {self.__class__.__name__}, Name: {self.name}"


class Recruiter(Employee):
    def work(self):
        return 'I come to the office and start to hiring.'


class Developer(Employee):
    def work(self):
        return 'I come to the office and start to coding.'


employee = Employee("Kate", 0)
recruiter = Recruiter("Alex", 1000)
recruiter1 = Recruiter("Tom", 1400)
developer = Developer("Ben", 1200)
developer1 = Developer("Mick", 1600)

print(employee.work())
print(recruiter.work())
print(developer.work())

print(employee)
print(recruiter)
print(developer)
print(recruiter1)
print(developer1)





