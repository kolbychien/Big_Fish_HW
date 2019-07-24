class User:
    """ User information and behaviors."""

    def __init__(self, first_name=None, last_name=None, user_type=None):
        self.first_name = first_name
        self.last_name = last_name
        self.user_type = user_type
        self.employee_network_access = False
        self.vendor_network_access = False
        self.contractor_network_access = False
        self.set_network_access()

    def set_network_access(self):
        if self.user_type == "Employee":
            self.employee_network_access = True
            self.vendor_network_access = True
            self.contractor_network_access = True
        elif self.user_type == "Vendor":
            self.employee_network_access = False
            self.contractor_network_access = False
            self.vendor_network_access = True
        elif self.user_type == "Contractor":
            self.contractor_network_access = True
            self.vendor_network_access = False
            self.employee_network_access = False
        else:
            self.revoke_all_network_access()

    def revoke_all_network_access(self):
        self.employee_network_access = False
        self.contractor_network_access = False
        self.vendor_network_access = False

    def set_user_type(self, user_type):
        self.user_type = user_type
        self.revoke_all_network_access()
        self.set_network_access()

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
        return " ".join([self.first_name, self.last_name])

    def has_employee_network_access(self):
        return self.employee_network_access

    def has_vendor_network_access(self):
        return self.vendor_network_access

    def has_contractor_network_access(self):
        return self.contractor_network_access
