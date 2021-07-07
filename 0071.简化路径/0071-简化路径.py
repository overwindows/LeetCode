class Solution:
    def simplifyPath(self, path: str) -> str:
        abs_path = path.split('/')
        can_path = []
        for path in abs_path:
            if not path:
                continue
            if path == '.':
                continue
            if path == '..': 
                if can_path:
                    can_path.pop()
                continue
            can_path.append(path)
        
        if can_path:
            return '/'+'/'.join(can_path) 
        else:
            return '/'       