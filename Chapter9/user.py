class User:

    def __init__ (self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"User Profile Summary: \t\nName: {self.first_name} {self.last_name} \t\nGender: {self.gender} \t\nAge: {self.age}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! I hope you're having a wonderful day!")

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1

    def reset_login_attempts(self):
        self.login_attempts = 0
