from data import gather_data
from model.address_book import AddressBook
from search_strategy.search_strategy import SearchStrategy

class LinearSearch(SearchStrategy):

    data: list[AddressBook] = gather_data.get_data_list()

    def search_name(self, name: str) -> list[AddressBook]:
        for address_book in self.data:
            if address_book.name() == name:
                return [address_book]
        return []

    def search_phone_number(self, phone_number: str) -> list[AddressBook]:
        for address_book in self.data:
            if address_book.phone_number() == phone_number:
                return [address_book]
        return []

    def search_address(self, address: str) -> list[AddressBook]:
        for address_book in self.data:
            if address_book.address() == address:
                return [address_book]
        return []
