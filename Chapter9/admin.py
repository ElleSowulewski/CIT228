from user import User

class Admin(User):

    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.login_attempts = 0
        self.privileges = ["can add post", "can delete post", "can ban user", "can edit post", "can delete user"]

    def show_privileges(self):
        print("Privilege list:")
        for i in self.privileges:
            print(i)
