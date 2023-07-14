# Implement a trie (prefix tree) data structure and its associated methods for efficient prefix matching.


class TrieNode:  # Define the TrieNode class

    def __init__(self, char):
        self.char = char  # Initialize the character stored in the node.
        # Initialize the children dictionary to store the children of the node.
        self.children = {}
        # Initialize the end of word boolean to mark the end of a word.
        self.is_end_of_word = False


class Trie:  # Define the Trie class

    def __init__(self):
        self.root = TrieNode(None)  # Initialize the root node of the trie.

    def insert(self, word):
        current = self.root  # Initialize the current node to the root node.
        for char in word:  # Iterate through each character in the word.
            # If the character is not in the children dictionary of the current node, add it.
            if char not in current.children:
                current.children[char] = TrieNode(char)
            # Update the current node to the child node.
            current = current.children[char]
        current.is_end_of_word = True  # Mark the end of the word.

    def search(self, word):
        current = self.root  # Initialize the current node to the root node.
        for char in word:  # Iterate through each character in the word.
            if char not in current.children:
                # If the character is not in the children dictionary of the current node, return False.
                return False
            # Update the current node to the child node.
            current = current.children[char]
        # Return True if the end of the word is marked, otherwise return False.
        return current.is_end_of_word

    def starts_with(self, prefix):  # Define the starts_with method.
        current = self.root  # Initialize the current node to the root node.
        for char in prefix:  # Iterate through each character in the prefix.
            if char not in current.children:
                return False
            current = current.children[char]
        # Return True if the prefix is found, otherwise return False.
        return True
