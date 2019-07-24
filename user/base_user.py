
class BaseUser():
    def __init__(self, first_name=None, last_name=None, user_type=None):
        self.first_name = first_name
        self.last_name = last_name
        self.user_type = user_type
        self.employee_network_access = False
        self.vendor_network_access = False
        self.contractor_network_access = False
        self.set_network_access()

    def set_network_access(self):
        self.revoke_all_network_access()
    
    def revoke_all_network_access(self):
        self.employee_network_access = False
        self.contractor_network_access = False
        self.vendor_network_access = False