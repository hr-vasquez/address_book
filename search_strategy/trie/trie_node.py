from model.address_book import AddressBook

class TrieNode:
    def __init__(self):
        self.__children = {}
        self.__is_leaf = False
        self.__data: AddressBook = None

    def get_children(self):
        return self.__children

    def is_leaf(self):
        return self.__is_leaf

    def set_is_leaf(self, is_leaf):
        self.__is_leaf = is_leaf

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data
