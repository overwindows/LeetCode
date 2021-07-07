class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret = list(secret)
        guess = list(guess)
        d = {}
        for n in secret:
            if n in d:
                d[n] +=1
            else:
                d[n] = 1
        
        B = 0

        for n in guess:
            if n in d:
                d[n] -= 1
                B += 1
                if d[n] == 0:
                    d.pop(n)
        
        A = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
        
        B -= A

        return str(A)+'A'+str(B)+'B'
