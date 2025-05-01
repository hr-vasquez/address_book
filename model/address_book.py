
class AddressBook:
    def __init__(self, name: str, phone_number: str, address: str):
        self.__name = name
        self.__phone_number = phone_number
        self.__address = address

    def name(self):
        return self.__name

    def phone_number(self):
        return self.__phone_number

    def address(self):
        return self.__address

    def to_dict(self):
        return {
            "name": self.__name,
            "phone_number": self.__phone_number,
            "address": self.__address
        }