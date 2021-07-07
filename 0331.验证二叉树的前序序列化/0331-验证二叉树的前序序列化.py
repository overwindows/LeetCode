class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(',')
        if preorder[-1] != '#':
            return False
        def _isValid(preorder):
            if not preorder:
                return False

            if preorder.pop(0) == '#':
                return True
            
            if  _isValid(preorder) and _isValid(preorder):
                return True
            
            return False

        ret = _isValid(preorder)

        if ret and not preorder:
            return True
        else:
            return False
'''
"9,3,4,#,#,1,#,#,2,#,6,#,#"
"1,#"
"9,#,#,1"
"#"
"1,#,#"
"1,#,3"
'''