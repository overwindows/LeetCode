class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ['+','-','*','/']:
                b = stack.pop()
                a = stack.pop()
                c = 0
                if token == '+':
                    c = a+b
                elif token == '-':
                    c = a-b
                elif token == '*':
                    c = a*b
                elif token == '/':
                    c = int(a/b)
                else:
                    pass
                #print(c)
                stack.append(c)
            else:
                stack.append(int(token))
        
        if stack:
            return stack[-1]
        else:
            return 0

'''
["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
["4", "13", "5", "/", "+"]
["2", "1", "+", "3", "*"]
'''
