class Employee:
    def __init__(self, basic, da, hra, tax, epf):
        self.basic = basic
        self.da = da
        self.hra = hra
        self.tax = tax
        self.epf = epf

    def gross_salary(self):
        return self.basic + (self.da * self.basic) + (self.hra * self.basic)

    def tax_amount(self):
        return self.tax * self.basic

    def net_salary(self):
        return self.gross_salary() - self.tax_amount() - self.epf

    def pay_details(self):
        print("Gross Salary:", self.gross_salary())
        print("Tax:", self.tax_amount())
        print("EPF:", self.epf)
        print("Net Salary:", self.net_salary())

class Manager(Employee):
    def __init__(self):
        super().__init__(30000, 0.95, 0.20, 0.25, 3000)

class Engineer(Employee):
    def __init__(self):
        super().__init__(20000, 0.80, 0.15, 0.15, 2000)

# Example usage
m = Manager()
print("Manager Pay Details:")
m.pay_details()

e = Engineer()
print("\nEngineer Pay Details:")
e.pay_details()
