from base_user import BaseUser
from employee import Employee
from vendor import Vendor
from contractor import Contractor

# My attempt using Factory Method Pattern, but problems all over:
#   Add new network access type
#   Add new user type


class User:
    """ User information and behaviors."""

    def __init__(self, first_name=None, last_name=None, user_type=None):
        self.user_obj = self.create_user(first_name, last_name, user_type)
        self.first_name = self.user_obj.first_name
        self.last_name = self.user_obj.last_name
        self.user_type = self.user_obj.user_type

    def create_user(self, first_name=None, last_name=None, user_type=None):
        # Went with Factory Method, but addomg new types breaks Open/Closed
        # I saw examples instantiating with globals() but doesn't seem like
        # good practice
        if user_type == 'Employee':
            return Employee(first_name, last_name, user_type)
        if user_type == 'Vendor':
            return Vendor(first_name, last_name, user_type)
        if user_type == 'Contractor':
            return Contractor(first_name, last_name, user_type)
        return BaseUser(first_name, last_name, user_type)

    def revoke_all_network_access(self):
        self.user_obj.revoke_all_network_access()

    def set_user_type(self, user_type):
        self.user_obj = self.create_user(self.first_name, self.last_name, user_type)
        self.user_type = user_type
        self.user_obj.set_network_access()

    def get_accessible_networks(self):
        networks = []
        msg_template = " ".join([self.get_full_name(), "has access to these networks:"])
        networks.append(msg_template)
        if self.has_employee_network_access():
            networks.append("Employee")
        if self.has_vendor_network_access():
            networks.append("Vendor")
        if self.has_contractor_network_access():
            networks.append("Contractor")

        return " ".join(networks)

    def get_full_name(self):
        return " ".join([self.user_obj.first_name, self.user_obj.last_name])

    def has_employee_network_access(self):
        return self.user_obj.employee_network_access

    def has_vendor_network_access(self):
        return self.user_obj.vendor_network_access

    def has_contractor_network_access(self):
        return self.user_obj.contractor_network_access

