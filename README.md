# Trie (Prefix Tree) Data Structure in Python

This is a Python implementation of a trie data structure, also known as a prefix tree, along with its associated methods for efficient prefix matching. A trie is commonly used to store and search strings based on their prefixes.

## TrieNode Class:
The TrieNode class represents a node in the trie. It has the following attributes:

- `char` - The character stored in the node.
- `children` - A dictionary that stores references to the child nodes. The keys are characters, and the values are corresponding child nodes.
- `is_end_of_word` - A boolean flag that marks the end of a word.

## Trie Class:
The Trie class contains the necessary methods to interact with the trie data structure. It has the following methods:

- `__init__()` - Initializes the trie by creating an empty root node.
- `insert(word)` - Inserts a word into the trie. It iterates over each character in the word, creates child nodes as needed, and marks the last character's node as the end of a word.
- `search(word)` - Searches for a given word in the trie. It traverses the trie, character by character, and checks if the word exists in the trie by verifying the presence of each character. It also checks if the last character's node is marked as the end of a word.
- `starts_with(prefix)` - Checks if any word in the trie starts with the given prefix. It follows a similar logic to the search method, traversing the trie based on the characters in the prefix.

## Usage Example:
To test the implementation, we create a `Trie` instance and perform various operations on it. We insert words into the trie, search for specific words, and check for prefixes. The output will indicate whether words or prefixes are found in the trie.



1. Clone the repository to your local machine using either the HTTPS or SSH URL. You can do this by clicking on the "Code" button on the repository's main page and copying the URL:

```Bash
git clone https://github.com/Reddragon300/Trie_Data_Structure
```

2. Change your current directory to the project's directory.

```Bash
cd Trie_Data_Structure
```
3. Review the project files, including trie.py, which contains the implementation of the trie data structure.
4. Install Python if you haven't already done so. You can download the latest version of Python from the official Python website (https://www.python.org/) and follow the installation instructions.
5. Open a terminal or command prompt and navigate to the project directory.
6. Use a text editor or IDE of your choice to write a Python script that utilizes the trie implementation. For example, you can create a new Python file (main.py) in the project directory and write your code there.
```python
# Create a trie instance
trie = Trie()

# Insert words into the trie using the insert(word) method:
words = ["apple", "banana", "orange"]
for word in words:
    trie.insert(word)
    print(f"Inserted '{word}' into the trie.")

# Search for words using the search(word) method:
search_words = ["apple", "banana", "grape"]
for word in search_words:
    if trie.search(word):
        print(f"'{word}' is found in the trie.")
    else:
        print(f"'{word}' is not found in the trie.")

# Check if any word in the trie starts with a specific prefix using the starts_with(prefix) method:
prefixes = ["app", "ban", "or", "gr"]
for prefix in prefixes:
    if trie.starts_with(prefix):
        print(f"There are words in the trie that start with '{prefix}'.")
    else:
        print(f"No words in the trie start with '{prefix}'.")

# Insert additional words
additional_words = ["application", "bat", "cat", "car", "care"]
for word in additional_words:
    trie.insert(word)
    print(f"Inserted '{word}' into the trie.")

# Test search functionality again
search_words = ["application", "batman", "cat", "careful"]
for word in search_words:
    if trie.search(word):
        print(f"'{word}' is found in the trie.")
    else:
        print(f"'{word}' is not found in the trie.")

# Test starts_with functionality again
prefixes = ["ap", "b", "ca", "co"]
for prefix in prefixes:
    if trie.starts_with(prefix):
        print(f"There are words in the trie that start with '{prefix}'.")
    else:
        print(f"No words in the trie start with '{prefix}'.")
```
8. Save the Python script file in the project directory.
9. In the terminal or command prompt, run the Python script to see the output.
```css
python main.py
```
The program will execute, and you'll see the results of the trie operations based on the code you wrote.


## NOTE:
Remember to ensure that the trie.py file, which contains the Trie class and the TrieNode class, is in the same directory as your Python script or module.

You can customize the code snippet above to suit your specific needs. Enjoy using the trie data structure for efficient prefix matching!
