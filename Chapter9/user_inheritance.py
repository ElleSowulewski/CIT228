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

class Admin(User):

    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.login_attempts = 0
        self.privileges = ["can add post", "can delete post", "can ban user", "can edit post", "can delete user"]

    def show_privileges(self):
        print("Privilege list:")
        for i in self.privileges:
            print(i)

admin1 = Admin("Jane", "Doe", "Female", "52")
admin1.show_privileges()