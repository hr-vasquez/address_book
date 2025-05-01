from operator import index

import pandas as pd

from model.address_book import AddressBook
from search_strategy.trie.trie import Trie

df = pd.read_excel('./data/PhoneBookDataset.xlsx', sheet_name="Representatives")

def get_data_list():
    return [
        AddressBook(row.Name, row.Phone, row.Address)
        for row in df.itertuples(index=False)
    ]

def get_sorted_data_by_name():
    return [
        AddressBook(row.Name, row.Phone, row.Address)
        for row in df.sort_values(by="Name").itertuples(index=False)
    ]

def get_sorted_data_by_phone():
    return [
        AddressBook(row.Name, row.Phone, row.Address)
        for row in df.sort_values(by="Phone").itertuples(index=False)
    ]

def get_sorted_data_by_address():
    return [
        AddressBook(row.Name, row.Phone, row.Address)
        for row in df.sort_values(by="Address").itertuples(index=False)
    ]

def get_sorted_trie_by_name():
    trie = Trie()
    for row in df.sort_values(by="Name").itertuples(index=False):
        trie.insert(row.Name, AddressBook(row.Name, row.Phone, row.Address))
    return trie

def get_sorted_trie_by_phone():
    trie = Trie()
    for row in df.sort_values(by="Phone").itertuples(index=False):
        trie.insert(row.Phone, AddressBook(row.Name, row.Phone, row.Address))
    return trie

def get_sorted_trie_by_address():
    trie = Trie()
    for row in df.sort_values(by="Address").itertuples(index=False):
        trie.insert(row.Address, AddressBook(row.Name, row.Phone, row.Address))
    return trie
