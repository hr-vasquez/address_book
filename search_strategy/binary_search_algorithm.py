from data import gather_data
from model.address_book import AddressBook
from search_strategy.search_strategy import SearchStrategy

class BinarySearch(SearchStrategy):

    sorted_list_by_name: list[AddressBook] = gather_data.get_sorted_data_by_name()
    sorted_list_by_phone: list[AddressBook] = gather_data.get_sorted_data_by_phone()
    sorted_list_by_address: list[AddressBook] = gather_data.get_sorted_data_by_address()

    def search_name(self, name: str) -> list[AddressBook]:
        index_result = self._search_index(self.sorted_list_by_name, 'name', 0, len(self.sorted_list_by_name) - 1, name)

        if index_result == -1:
            return []

        return [self.sorted_list_by_name[index_result]]

    def search_phone_number(self, phone_number: str) -> list[AddressBook]:
        index_result = self._search_index(self.sorted_list_by_phone, 'phone_number', 0, len(self.sorted_list_by_phone) - 1, phone_number)

        if index_result == -1:
            return []

        return [self.sorted_list_by_phone[index_result]]

    def search_address(self, address: str) -> list[AddressBook]:
        index_result = self._search_index(self.sorted_list_by_address, 'address', 0, len(self.sorted_list_by_address) - 1, address)

        if index_result == -1:
            return []

        return [self.sorted_list_by_address[index_result]]

    def _search_index(self, my_list, method_name, start, end, search_data):
        if end < start:
            return -1

        middle = int(start + (end - start) / 2)
        item = getattr(my_list[middle], method_name)()
        if item == search_data:
            return middle

        if item < search_data:
            start = middle + 1
        elif item > search_data:
            end = middle - 1

        return self._search_index(my_list, method_name, start, end, search_data)
