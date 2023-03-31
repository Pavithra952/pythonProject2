import unittest
def apply_raise(self,percentage):
    self.salary=int(self.salary*(1+percentage/100))
class TestEmployee(unitest.TestCase)
    def setup(self):
        self.employee=Employe('Rahul',50000)
    def test_email(self):
        self.assertEqual(self.employee.email,'rahul@example.com')
    def test_apply_raise(self):
        self.employee.apply_raise(10)
        self.assertEqual(self.employee.salary,55000)
        
