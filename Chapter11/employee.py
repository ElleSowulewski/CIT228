class Employee:

    def __init__(self, fname, lname, salary, store):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        self.store = store
    
    def give_raise(self, raise_amount = 5000):
        self.salary += raise_amount
        print(f"{self.lname}'s salary is now: {self.salary}")


