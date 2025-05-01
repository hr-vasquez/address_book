from types import MappingProxyType

from model.algorithm_enum import Algorithm
from search_strategy.linear_search_algorithm import LinearSearch
from search_strategy.binary_search_algorithm import BinarySearch
from search_strategy.trie_search_algorithm import TrieSearch

search_algorithms = {}
# To make it read only
_search_algorithms_view = MappingProxyType(search_algorithms)

def register_search_algorithm(name):
    def wrapper(func):
        search_algorithms[name] = func
        return func
    return wrapper

def get_search_algorithms():
    return _search_algorithms_view

@register_search_algorithm(Algorithm.LINEAR.value)
def linear_search():
    return LinearSearch()

@register_search_algorithm(Algorithm.BINARY.value)
def binary_search():
    return BinarySearch()

@register_search_algorithm(Algorithm.TRIE.value)
def trie_search():
    return TrieSearch()
