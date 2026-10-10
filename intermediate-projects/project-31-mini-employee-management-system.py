class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def show_info(self):
        print('=== EMPLOYEE INFO ===')
        print(f'Name: {self.name}')
        print(f'Salary: {self.salary}')
        print('================')

class Developer(Employee):
    def __init__(self, name, salary, programming_language: str):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def show_developer(self):
        print('=== DEVELOPER INFO ===')
        print(f'Programming language: {self.programming_language}')
        print('=================')

class Manager(Employee):
    def __init__(self, name, salary, team_size: int):
        super().__init__(name, salary)
        self.team_size = team_size

    def show_manager(self):
        print('=== MANAGER INFO ===')
        print(f'Team size: {self.team_size}')
        print('===============')

Employee1 = Employee('Jodell', 5000)
developer = Developer('Jodell', 25000, 'Python')
manager = Manager('Dale', 35000, 5)
Employee1.show_info()
developer.show_info()
developer.show_developer()
manager.show_info()
manager.show_manager()