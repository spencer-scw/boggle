class TreeNode:
    def __init__(self, letter):
        self.letter = letter
        self.terminal = False
        self.children = {}

    def __getitem__(self, key):
        return self.children[key]

    def get(self, key):
        return self.children.get(key)
            

class BoggleDictionary:
    def __init__(self, language = 'words'):
        f = ''.join(['/usr/share/dict/', language])
        words = open(f, 'r')
        self.word_tree = TreeNode('')

        for word in words.readlines():
            word = word.strip()
            current_node = self.word_tree
            for letter in word:
                if current_node.children.get(letter) is None:
                    current_node.children[letter] = TreeNode(letter)
                current_node = current_node.children[letter]
            current_node.terminal = True

    def __getitem__(self, key):
        curr_node = self.word_tree
        for letter in key:
            if curr_node.get(letter) is not None:
                curr_node = curr_node.get(letter)
            else:
                return None
            
        return curr_node
            
        
