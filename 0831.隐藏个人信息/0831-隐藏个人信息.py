class Solution:
    def maskPII(self, S: str) -> str:
        if '@' in S:
            S = S.lower()
            name, address = S.split('@')
            new_name = name[0]+'*****'+name[-1]
            return new_name+'@'+address
        else:
            nums = []
            for c in S:
                if c >= '0' and c<='9':
                    nums.append(c)
            
            local = '***-***-'+''.join(nums[-4:])
            if len(nums) > 10:
                inter = len(nums[:-10])*'*'
                final = inter+'-'+local
                if S[0] == '+' or S[0] == '-':
                    final =  S[0]+final
                else:
                    final = '+'+final
                return final
            else:
                return local
                
        