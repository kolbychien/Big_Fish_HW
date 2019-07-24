
from base_user import BaseUser

class Employee(BaseUser):
    def set_network_access(self):
        self.employee_network_access = True
        self.vendor_network_access = True
        self.contractor_network_access = True