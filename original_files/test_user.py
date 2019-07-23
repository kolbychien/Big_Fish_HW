import random
import unittest

from user import User


class UserTest(unittest.TestCase):
    """Suite of tests for user behaviors."""

    def test_user_init(self):
        new_user = User("Aaron", "Wilson", "Employee")

        self.assertEqual(new_user.first_name, "Aaron")
        self.assertEqual(new_user.last_name, "Wilson")
        self.assertEqual(new_user.user_type, "Employee")

    def test_set_user_type(self):
        new_user = User("Aaron", "Wilson")
        new_user.set_user_type("Employee")

        self.assertEqual(new_user.user_type, "Employee")

        new_user.set_user_type("Vendor")

        self.assertEqual(new_user.user_type, "Vendor")

    def test_set_employee_network_access(self):
        user = User("Aaron", "Wilson", "Employee")

        self.assertTrue(user.has_employee_network_access())
        self.assertTrue(user.has_vendor_network_access())
        self.assertTrue(user.has_contractor_network_access())

        user.set_user_type("Vendor")

        self.assertFalse(user.has_employee_network_access())
        self.assertFalse(user.has_contractor_network_access())
        self.assertTrue(user.has_vendor_network_access())

        user.set_user_type("Contractor")

        self.assertTrue(user.has_contractor_network_access())
        self.assertFalse(user.has_vendor_network_access())
        self.assertFalse(user.has_employee_network_access())

        user.set_user_type(None)

        self.assertFalse(user.has_employee_network_access())
        self.assertFalse(user.has_contractor_network_access())
        self.assertFalse(user.has_vendor_network_access())

    def test_revoke_all_network_access(self):
        user = User()

        user.employee_network_access = random.randint(0, 1)
        user.employee_network_access = random.randint(0, 1)
        user.vendor_network_access = random.randint(0, 1)

        user.revoke_all_network_access()

        self.assertFalse(user.has_employee_network_access())
        self.assertFalse(user.has_contractor_network_access())
        self.assertFalse(user.has_vendor_network_access())

    def test_network_access_string(self):
        user = User("Aaron", "Wilson", "Employee")

        x = user.get_accessible_networks()
        self.assertEqual(x, "Aaron Wilson has access to these networks: Employee Vendor Contractor")

        user.set_user_type("Vendor")
        x = user.get_accessible_networks()
        self.assertEqual(x, "Aaron Wilson has access to these networks: Vendor")

        user.set_user_type("Contractor")
        x = user.get_accessible_networks()
        self.assertEqual(x, "Aaron Wilson has access to these networks: Contractor")


if __name__ == "__main__":
    unittest.main()
