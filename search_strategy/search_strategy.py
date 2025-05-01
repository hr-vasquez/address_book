from model.address_book import AddressBook

class SearchStrategy:
    def search_name(self, name: str) -> list[AddressBook]:
        pass

    def search_phone_number(self, phone_number: str) -> list[AddressBook]:
        pass

    def search_address(self, address: str) -> list[AddressBook]:
        pass
