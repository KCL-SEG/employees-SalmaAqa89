"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name
        self.contract_type = None
        self.commission_type = None
        self.hours = None
        self.salary = None
        self.contract_num = None
        self.commision_amount = None
        
        if (self.name == "Billie"):
            self.contract_type = "monthly"
            self.salary = 4000

        if (self.name == "Charlie"):
            self.contract_type = "hourly"
            self.hours = 100
            self.salary = 25

        if (self.name == "Renee"):
            self.contract_type = "monthly"
            self.salary =3000
            self.commission_type = "contract"
            self.contract_num = 4
            self.commision_amount = 200

        if (self.name == "Jan"):
            self.contract_type = "hourly"
            self.hours = 150
            self.salary = 25
            self.commission_type = "contract"
            self.contract_num = 3
            self.commision_amount = 220
        
        if (self.name == "Robbie"):
            self.contract_type = "monthly"
            self.salary = 2000
            self.commission_type = "bonus"
            self.commision_amount = 1500

        if (self.name == "Ariel"):
            self.contract_type = "hourly"
            self.hours = 120
            self.salary = 30
            self.commission_type = "bonus"
            self.commision_amount = 600

    def get_pay(self):
        final_salary = 0
        if self.contract_type == "monthly":
            final_salary += self.salary

        if self.contract_type == "hourly":
            final_salary += self.salary * self.hours

        if self.commission_type:
            if self.commission_type == "contract":
                final_salary += self.contract_num * self.commision_amount

            if self.commission_type == "bonus":
                final_salary += self.commision_amount

        return final_salary

    def __str__(self):
        final_string = f'{self.name} works on a '
        
        if self.contract_type == "monthly":
            final_string += f'monthly salary of {self.salary}'

        if self.contract_type == "hourly":
            final_string += f'contract of {self.hours} hours at {self.salary}/hour'

        if self.commission_type is None:
            final_string += f'. '
        
        else:
            final_string += f' and receives a '
            
            if self.commission_type == "contract":
                final_string += f'commission for {self.contract_num} contract(s) at {self.commision_amount}/contract. '
            
            if self.commission_type == "bonus":
                final_string += f'bonus commission of {self.commision_amount}. '

        final_string += f'Their total pay is {self.get_pay()}.'
        return final_string
    


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')