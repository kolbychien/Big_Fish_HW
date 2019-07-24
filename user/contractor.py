
from base_user import BaseUser

class Contractor(BaseUser):
    def set_network_access(self):
        self.employee_network_access = False
        self.vendor_network_access = False
        self.contractor_network_access = True