class Node():
    def __init__(self):
        self.weight = -1
        self.edges = {}

class Trie():
    def __init__(self):
        self.root = Node()

    def insert(self, word, weight=-1):
        node = self.root

        for w in word:
            if (node.weight < weight):
                node.weight = weight

            if (node.edges.has_key(w)):
                node = node.edges[w]
            else:
                node.edges[w] = Node()
                node = node.edges[w]

        if (node.weight < weight):
            node.weight = weight

    def findmax(self, prefix):
        node = self.root

        for c in prefix:
            if (node.edges.has_key(c)):
                node = node.edges[c]
            else:
                return -1
        return node.weight

def main():
    n,t = map(int, raw_input().split())
    trie = Trie()

    for _ in xrange(n):
        s, w = raw_input().split()
        w = int(w)
        trie.insert(s, w)

    for _ in xrange(t):
        prefix = raw_input()
        print trie.findmax(prefix)

main()

"""
https://www.hackerearth.com/practice/data-structures/advanced-data-structures/trie-keyword-tree/practice-problems/algorithm/search-engine/

input:-
2 1
hackerearth 10
hackerrank 9
hacker
"""
