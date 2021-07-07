class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lens = [len(word) for word in words]
        mat = []
        _maxWidth = maxWidth
        line = []

        for i in range(len(words)):
            if line:
                if _maxWidth == 0:
                    mat.append(line)
                    line = []
                    line.append(words[i])
                    _maxWidth = maxWidth - lens[i]
                else:
                    assert _maxWidth > 0, _maxWidth

                    if _maxWidth > lens[i]:
                        line.append(words[i])
                        _maxWidth -= (lens[i]+1)
                    else:
                        mat.append(line)
                        line = []
                        line.append(words[i])
                        _maxWidth = maxWidth - lens[i]
            else:
                line.append(words[i])
                _maxWidth = maxWidth - lens[i]
        if line:
            mat.append(line)

        # print(mat)
        res = []
        for i in range(len(mat)-1):
            s = ''
            r = mat[i]

            _width = maxWidth
            
            n = len(r) - 1
            
            for x in r:
                _width -= len(x)
            
            if n > 0:
                m = _width // n
            else:
                m = 0
                s = r[0] + ' '*_width
            
            space = [0] * n
            w = _width
            for i in range(1,n+1):
                space[-i] = w // (n-i+1)
                w = w - w // (n-i+1)
            # print(space)
            # print(r)
            for i in range(n):
                s += (r[i] + ' ' * space[i])
            
            if n > 0:
                s += r[-1]
            res.append(s)
        
        _width = maxWidth
        s = ' '.join(mat[-1])
        n = len(s)
        s += ' '*(_width-n)

        res.append(s)

        return res

'''
["This", "is", "an", "example", "of", "text", "justification."]
16
["What","must","be","acknowledgment","shall","be"]
16
["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
20
'''