class Trie:
    def __init__(self):
        self.child = dict()
        self.count = 0

    def insert(self, str):
        current = self
        for ch in str:
            current.count += 1
            if ch not in current.child:
                current.child[ch] = Trie()

            current = current.child[ch]
        current.count += 1

    def search(self, str):
        current = self
        for ch in str:
            if ch == "?":
                return current.count
            if ch not in current.child:
                return 0
            current = current.child[ch]
        return current.count


def solution(words, queries):
    TrieRoot = [Trie() for _ in range(10000)]
    ReTrieRoot = [Trie() for _ in range(10000)]
    answer = []

    for str in words:
        TrieRoot[len(str) - 1].insert(str)
        ReTrieRoot[len(str) - 1].insert(str[::-1])

    for str in queries:
        if str[0] != "?":
            answer.append(TrieRoot[len(str) - 1].search(str))
        else:
            answer.append(ReTrieRoot[len(str) - 1].search(str[::-1]))
    return answer