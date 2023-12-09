from termcolor import colored

class Company:

    def __init__(self):
        self.staff = []
        self.branches = []
        self.positions = []

    def add_branch(self, name):
        branch = Branch(name)
        self.branches.append(branch)
        return branch

    def remove_branch(self, branch):
        self.branches.remove(branch)

    def add_position(self, title):
        position = Position(title)
        self.positions.append(position)
        return position

    def remove_position(self, position):
        self.positions.remove(position)

    def add_employee(self, name, position, branch):
        employee = Employee(name, position, branch)
        self.staff.append(employee)
        return employee

    def remove_employee(self, employee):
        self.staff.remove(employee)

    def get_employee_branch(self, branch_name):
        staff = []
        for employee in self.staff:
            if employee.branch.name == branch_name:
                staff.append(employee)
        return staff

    def get_employee_position(self, position_title):
        staff = []
        for employee in self.staff:
            if employee.position.title == position_title:
                staff.append(employee)
        return staff

    def get_branches(self):
        return [branch.name for branch in self.branches]

    def get_positions(self):
        return [position.title for position in self.positions]


class Employee:

    def __init__(self, name, position, branch):
        self.name = name
        self.position = position
        self.branch = branch

class Branch:

    def __init__(self, name):
        self.name = name
        self.staff = []

    def add_employee(self, employee):
        self.staff.append(employee)

    def remove_employee(self, employee):
        self.staff.remove(employee)

class Position:

    def __init__(self, title):
        self.title = title
        self.staff = []

    def add_employee(self, employee):
        self.staff.append(employee)

    def remove_employee(self, employee):
        self.staff.remove(employee)

company = Company()

while True:
    print("\n1. Přidat pobočku")
    print("2. Odebrat pobočku")
    print("3. Přidat pracovní pozici")
    print("4. Odebrat pracovní pozici")
    print("5. Přidat zaměstnance")
    print("6. Odebrat zaměstnance")
    print("7. Seznam poboček")
    print("8. Seznam pracovních pozic")
    print("9. Zaměstnanci v pobočce")
    print("10. Zaměstnanci na pozici")
    print("11. Konec")

    volba = int(input("\nVyberte možnsot:"))

    if volba == 1:
        ammount_branches = int(input("Kolik poboček chcete přidat:"))
        while ammount_branches > 0:
            branch_name = input("Zadejte název pobočky:")
            company.add_branch(branch_name)
            ammount_branches -= 1
            print(colored(f"Seznam poboček:{company.get_branches()}","yellow"))
            
    elif volba == 2:
        ammount_branches = int(input("\nKolik poboček chcete odstranit:"))
        while ammount_branches > 0:
            print(colored(f"Seznam poboček:{company.get_branches()}","yellow"))
            branch_name = input("Zadejte název pobočky:")
            found = False
            for branch in company.branches:
                if branch.name == branch_name:
                    company.remove_branch(branch)
                    ammount_branches -= 1
                    found = True
                    break
            if not found:
                print(colored(f"Pobočka '{branch_name}' nebyla nalezena.","red"))

    elif volba == 3:
        ammount_positions = int(input("Kolik pozicí chcete přidat:"))
        while ammount_positions > 0:
            position_name = input("Zadejte název pracovní pozice:")
            company.add_position(position_name)
            ammount_positions -=1
            print(colored(f"Seznam pracovních pozic:{company.get_positions()}","yellow"))

    elif volba == 4:
        ammount_positions = int(input("Kolik pozicí chcete odebrat:"))
        while ammount_positions > 0:
            print(colored(f"Seznam pracovních pozic:{company.get_positions()}","yellow"))
            position_name = input("Zadejte název pracovní pozice:")
            found = False
            for positon in company.positions:
                if positon.title == position_name:
                    company.remove_position(positon)
                    found = True
                    ammount_positions -=1
                    break
            if not found:
                print(colored(f"Pozice '{position_name}' nebyla nalezena.","red"))

    elif volba == 5:
        employee_name = input("Zadejte jméno zaměstnance:")
        print(colored(f"Seznam pracovních pozic:{company.get_positions()}","yellow"))
        position_title = input("Zadejte název pracovní pozice:")
        print(colored(f"Seznam poboček:{company.get_branches()}","yellow"))
        branch_name = input("Zadejte název pobočky:")
        position = None
        branch = None
        for p in company.positions:
            if p.title == position_title:
                position = p
                break
        for b in company.branches:
            if b.name == branch_name:
                branch = b
                break
        if position and branch:
            company.add_employee(employee_name, position, branch)
            print(colored(f"Zaměstnanec '{employee_name}' byl přidán.", "green"))
        else:
            print(colored("Nepodařilo se najít pracovní pozici nebo pobočku.", "red"))

    elif volba == 6:
        employee_name = input("Zadejte jméno zaměstnance k odstranění:")
        found = False
        for employee in company.staff:
            if employee.name == employee_name:
                company.remove_employee(employee)
                found = True
                print(colored(f"Zaměstnanec '{employee_name}' byl odstraněn.", "green"))
                break
        if not found:
            print(colored(f"Zaměstnanec '{employee_name}' nebyl nalezen.", "red"))

    elif volba == 7:
        print(colored(f"Seznam poboček:{company.get_branches()}","yellow"))

    elif volba == 8:
        print(colored(f"Seznam pracovních pozic:{company.get_positions()}","yellow"))

    elif volba == 9:
        print(colored(f"Seznam poboček:{company.get_branches()}", "yellow"))
        branch_name = input("Zadejte název pobočky:")
        
        found_branch = None
        for branch in company.branches:
            if branch.name == branch_name:
                found_branch = branch
                break
        
        if found_branch:
            staff = company.get_employee_branch(branch_name)
            if staff:
                print(colored(f"Zaměstnanci v pobočce '{branch_name}':", "yellow"))
                for employee in staff:
                    print(employee.name)
            else:
                print(colored(f"Pobočka '{branch_name}' nemá žádné zaměstnance.", "yellow"))
        else:
            print(colored(f"Pobočka '{branch_name}' nebyla nalezena.", "red"))

    elif volba == 10:
        print(colored(f"Seznam pracovních pozic:{company.get_positions()}", "yellow"))
        position_title = input("Zadejte název pracovní pozice:")
        
        staff = company.get_employee_position(position_title)
        
        if staff:
            print(colored(f"Zaměstnanci na pozici '{position_title}':", "yellow"))
            for employee in staff:
                print(employee.name)
        else:
            print(colored(f"Pozice '{position_title}' nebyla nalezena nebo nemá zaměstnance.", "red"))

    elif volba == 11:
        break
    else:
        print(colored("Neplatná volba.","red"))