class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d = {}
        N = len(accounts)

        for i in range(N):
            emails = accounts[i][1:]
            M = len(emails)

            for j in range(M):
                if emails[j] in d:
                    d[emails[j]].append(i)
                else:
                    d[emails[j]] = [i]
        
        group = []
        for _, v in d.items():
            group.append(set(v))


        grp_num = len(group)
        i = 0
        
        while i < grp_num:
            while True:
                tbd = []
                j = i+1
                while j < grp_num:
                    if group[i] & group[j]:
                        group[i] |= group[j]
                        tbd.append(group[j])
                    j += 1
                
                for item in tbd:
                    group.remove(item)
                
                if len(tbd) == 0:
                    break
                else:
                    grp_num -= len(tbd)
            i += 1
        
        # print(group)
        new_accounts = []
        for sub in group:
            new_account = []
            name = None
            for i in sub:
                new_account.extend(accounts[i][1:])
                name = accounts[i][0]
            new_account=list(set(new_account))
            new_account.sort()
            new_accounts.append([name]+new_account)
        return new_accounts
             

