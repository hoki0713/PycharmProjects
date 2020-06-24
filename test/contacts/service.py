class Service:
    def __init__(self):
        self._contacts = []

    def add_contact(self, payload):
        self._contacts.append(payload)

    def get_contact(self, payload) -> object:
        for i in self._contacts:
            if payload == i.name:
                return i

    def get_contacts(self) -> []:
        contacts = []
        for i in self._contacts:
            contacts.append(i.to_string())
        return ' '.join(contacts)

    def del_contact(self, payload):
        for i, t in enumerate(self._contacts):
            if payload == t.name:
                del self._contacts[i]
