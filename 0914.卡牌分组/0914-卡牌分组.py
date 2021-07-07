class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        card = {}
        for d in deck:
            if d not in card:
                card[d] = 0
            card[d] += 1
        
        X = []
        for k,v in card.items():
            X.append(v)
        if not X:
            return True
        
        if len(X) > 1:
            print(X)
            gcd = math.gcd(X[0],X[1])
            for i in range(2,len(X)):
                gcd = math.gcd(gcd, X[i])
                if gcd == 1:
                    return False
            if gcd > 1:
                return True
            else:
                return False
        else:
            if X[0] < 2:
                return False
            return True
            '''
            x = X[0]
            # print(x)
            if x < 2:
                return False
            else:
                print(x)
                for i in range(2,int(x**0.5+1)+1):
                    # print(i)
                    if x % i == 0:
                        return True
                return False
            '''
'''
[1,2,3,4,4,3,2,1]
[1,1,1,2,2,2,3,3]
[1]
[1,1]
[1,1,2,2,2,2]
[1,1,1,1,1,0,0,0]
'''
