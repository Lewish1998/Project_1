class Owner:
    def __init__(self, first_name, last_name, address, contact, active=True, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.contact = contact
        self.active = active
        self.id = id