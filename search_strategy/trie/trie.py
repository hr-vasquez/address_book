from search_strategy.trie.trie_node import TrieNode

class Trie:
    def __init__(self):
        self.__root = TrieNode()

    def insert(self, string, data):
        current_node = self.__root
        for char in string:
            if char not in current_node.get_children():
                current_node.get_children()[char] = TrieNode()
            current_node = current_node.get_children()[char]
        current_node.set_is_leaf(True)
        current_node.set_data(data)

    def search(self, term):
        current_node = self.__root
        for char in term:
            if char in current_node.get_children():
                current_node = current_node.get_children()[char]
            else:
                return []

        results = []
        self._search_leaf(results, current_node)

        return results

    def _search_leaf(self, results, node):
        if node.is_leaf():
            results.append(node.get_data())
        else:
            for key, value in node.get_children().items():
                self._search_leaf(results, node.get_children()[key])