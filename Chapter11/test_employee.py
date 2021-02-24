import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        fname = "John"
        lname = "Doe"
        salary = 24000
        store = "Traverse City Location"
        self.employee = Employee(fname, lname, salary, store)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 29000)

    def test_give_custom_raise(self):
        raise_amount = 5500
        self.employee.give_raise(raise_amount)
        self.assertEqual(self.employee.salary, 29500)

if __name__ == '__main__':
    unittest.main()