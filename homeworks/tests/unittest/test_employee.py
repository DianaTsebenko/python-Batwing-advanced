import unittest
from employee import Employee


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.employer = Employee('diana', 'tsebenko', 500)

    def test_email(self):
        self.assertEqual(self.employer.email, 'diana.tsebenko@email.com')

    def test_fullname(self):
        self.assertEqual(self.employer.fullname, 'diana tsebenko')

    def test_apply_raise(self):
        self.assertEqual(self.employer.pay * Employee.raise_amt, 525)
