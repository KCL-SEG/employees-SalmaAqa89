"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type, monthly_salary=0, hours_worked=0, hour_rate=0, commission_rate=0, fixed_bonus = 0, contracts_landed = 0):
        self.name = name
        self.contract_type = contract_type
        self.monthly_salary = monthly_salary
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate
        self.commission_rate = commission_rate
        self.fixed_bonus = fixed_bonus
        self.contracts_landed = contracts_landed

    def get_pay(self):
        pay = 0
        if self.contract_type == "Monthly salary":
            pay += self.monthly_salary
        elif self.contract_type == "Hourly salary":
            pay += (self.hours_worked * self.hour_rate)
        else:
            pay = 0

        if self.contract_type == "Monthly salary" and self.contracts_landed > 0:
            pay += (self.commission_rate * self.contracts_landed)
        elif self.contract_type == "Hourly salary" and self.contracts_landed > 0:
            pay += (self.commission_rate * self.contracts_landed)

        pay += self.fixed_bonus

        return pay

        
    def __str__(self):
        pay_info= ""
        if self.contract_type == "Monthly salary":
            pay_info = f"{self.monthly_salary}"
        elif self.contract_type == "Hourly salary":
            pay_info = f"{self.hours_worked} hours at {self.hour_rate}"
        else:
            pay_info = "no pay"

        commission_info = ""
        if self.contracts_landed > 0:
            commission_info = f" and receives a commission for {self.contracts_landed} contract(s) at {self.commission_rate}"

        bonus_info = ""
        if self.fixed_bonus > 0:
            bonus_info = f" and receives a bonus commission of {self.fixed_bonus}"

        pay = self.get_pay()
        return f"{self.name} works on a {self.contract_type} contract of {pay_info}{commission_info}{bonus_info}. Their total pay is {pay}."


billie = Employee("Billie", "Monthly salary", monthly_salary=4000)
charlie = Employee("charlie", "Hourly salary", hours_worked=100, hour_rate=25)
renee = Employee("Renee", "Monthly salary", monthly_salary=3000, contracts_landed=4, commission_rate=200)
jan = Employee("Jan", "Hourly salary", hours_worked=150, hour_rate=25, contracts_landed=3, commission_rate=220)
robbie = Employee("Robbie", "Monthly salary", monthly_salary=2000, fixed_bonus=1500)
ariel = Employee("Ariel", "Hourly salary", hours_worked=120, hour_rate=30, fixed_bonus=600)

print(billie.get_pay())
print(str(billie))

print(charlie.get_pay())
print(str(charlie))

print(renee.get_pay())
print(str(renee))

print(jan.get_pay())
print(str(jan))

print(robbie.get_pay())
print(str(robbie))

print(ariel.get_pay())
print(str(ariel))
