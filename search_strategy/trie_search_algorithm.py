from data import gather_data
from model.address_book import AddressBook
from search_strategy.search_strategy import SearchStrategy

class TrieSearch(SearchStrategy):

    data: list[AddressBook] = gather_data.get_data_list()

    def search_name(self, name: str) -> list[AddressBook]:
        trie = gather_data.get_sorted_trie_by_name()
        return trie.search(name)

    def search_phone_number(self, phone_number: str) -> list[AddressBook]:
        trie = gather_data.get_sorted_trie_by_phone()
        return trie.search(phone_number)

    def search_address(self, address: str) -> list[AddressBook]:
        trie = gather_data.get_sorted_trie_by_address()
        return trie.search(address)
