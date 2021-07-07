class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1:
            return str2
        if not str2:
            return str1
        if len(str1) > len(str2) and str1.startswith(str2):
            #print(str2, str1[len(str2):])
            return self.gcdOfStrings(str2, str1[len(str2):])
        elif str2.startswith(str1):
            return self.gcdOfStrings(str1, str2[len(str1):])
        else:
            return ""


            