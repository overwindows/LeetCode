import functools
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        vocab = []
        words = list(set(words))
        #print(words)
        words.sort(key=functools.cmp_to_key(lambda x,y: len(y)-len(x)))
        #print(words)
        for word in words:
            contained = False
            for v in vocab:
                if v.endswith(word):
                    contained = True
                    break
            if not contained:
                vocab.append(word)
        if vocab:
            return len('#'.join(vocab))+1
        else:
            return 0

'''
["time", "atime", "btime"]
["time", "me", "bell"]
[]
["time","tfboys"]
'''