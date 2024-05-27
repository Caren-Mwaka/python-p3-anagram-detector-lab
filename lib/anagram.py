class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        anagrams = []
        for w in words:
            if sorted(self.word) == sorted(w):
                anagrams.append(w)
        return anagrams

listen = Anagram("listen")
anagrams = listen.match(['enlists', 'google', 'inlets', 'banana'])
print(anagrams)
