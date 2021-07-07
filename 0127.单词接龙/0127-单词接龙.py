class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        endWordIndex = wordList.index(endWord)

        # create index
        index = {}
        for ix in range(len(wordList)):
            word = wordList[ix]
            for i in range(len(word)):
                _key = list(word)
                _key[i] = '#'
                _key = ''.join(_key)

                if _key in index:
                    index[_key].append(ix)
                else:
                    index[_key] = [ix]
        
        #print(index)

        BFS = []
        BFS.append(beginWord)
        BFS.append(None)

        dup = set()
        dup.add(beginWord)
        cnt = 0
        find = False
        while BFS:
            word = BFS.pop(0)
            if word is None:
                cnt += 1
                if BFS:
                    BFS.append(None)
                continue
            
            if word == endWord:
                find = True
                cnt += 1
                break

            for i in range(len(word)):
                _key = list(word)
                _key[i] = '#'
                _key = ''.join(_key)

                if _key in index:
                    for ix in index[_key]:
                        if wordList[ix] not in dup:
                            BFS.append(wordList[ix])
                            dup.add(wordList[ix])
            
        
        if find:
            return cnt
        else:
            return 0
        



             
'''
"hit"
"cog"
["hot","hit","cog","dot","dog"]
'''