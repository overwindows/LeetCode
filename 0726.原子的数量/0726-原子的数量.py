class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        atoms_dict = {}
        formula = list(formula)

        def countOfAtoms_flat(f):
            d = {}
            N = len(f)
            i = 0
            _name = None
            _cnt = None
            for i in range(N):
                if f[i] >= 'A' and f[i] <= 'Z':
                    if _name:
                        atom_name = _name
                        if atom_name not in d:
                            d[atom_name] = 0
                        if _cnt:
                            d[atom_name] += int(_cnt)
                            _cnt = None
                        else:
                            d[atom_name] += 1
                    _name = f[i]
                elif f[i] >= 'a' and f[i] <= 'z':
                    _name += f[i]
                else:
                    assert f[i] >= '0' and f[i] <= '9'
                    if _cnt:
                        _cnt += f[i]
                    else:
                        _cnt = f[i]
            if _name:
                atom_name = _name
                if atom_name not in d:
                    d[atom_name] = 0
                if _cnt:
                    d[atom_name] += int(_cnt)
                    _cnt = None
                else:
                    d[atom_name] += 1
            
            return d

        N = len(formula)
        buf = []
        stack = []
        i = 0
        while i < N:
            if formula[i] == '(':
                if buf:
                    _d = countOfAtoms_flat(buf)
                    buf = []
                    stack.append(_d)
                    # print(_d)
                stack.append('(')
                i += 1
            elif formula[i] == ')':
                if buf:
                    _d = countOfAtoms_flat(buf)
                    buf = []
                    stack.append(_d)
                    # print(_d)
                i += 1
                _cnt = ''
                while i < N and formula[i] >= '0' and formula[i] <= '9':
                    _cnt += formula[i]
                    i += 1
                if _cnt:
                    count = int(_cnt)
                else:
                    count = 1
                # print(count)
                # print(stack)
                tmp_array = []
                while True: 
                    obj=stack.pop()
                    if obj == '(':
                        break
                    new_d = {}
                    for k,v in obj.items():
                        new_d[k] = count * v
                    tmp_array.append(new_d)
                stack.extend(tmp_array)
                # print(stack)
            else:
                buf.append(formula[i])
                i += 1
        if buf:
            # print(buf)
            _d = countOfAtoms_flat(buf)
            # print(_d)
            buf = []
            stack.append(_d) 
        ## Merge
        # print(stack)
        while stack:
            obj = stack.pop()
            for k,v in obj.items():
                if k not in atoms_dict:
                    atoms_dict[k] = 0
                atoms_dict[k] += v              

        count_of_atoms = ''
        sorted_keys = sorted(atoms_dict.keys())
        # print(atoms_dict)
        # print(sorted_keys)
        for k in sorted_keys:
            count_of_atoms += k
            if atoms_dict[k] > 1:
                count_of_atoms += str(atoms_dict[k])
        
        return count_of_atoms

"""
"H2O"
"Mg(OH)2"
"K4(ON(SO3)2)2"
"Be32"
"""