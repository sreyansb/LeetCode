#attempt4: TOOK HINT
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equality_eqns = {}
        for first_var,equality,_,second_var in equations:
            if equality == "=":
                if first_var not in equality_eqns:
                    equality_eqns[first_var] = {first_var}
                if second_var not in equality_eqns:
                    equality_eqns[second_var] = {second_var}
                equality_eqns[first_var].add(second_var)
                equality_eqns[second_var].add(first_var)
        
        def find_equality(parent,second_var,visited=set()):
            if parent not in equality_eqns:
                return False
            if second_var in equality_eqns[parent]:
                return True
            ans = False
            for equals in equality_eqns[parent]:
                if equals in visited:
                    continue
                ans = ans or find_equality(equals,second_var,visited|{parent})
            return ans
                
        
        for first_var,equality,_,second_var in equations:
            if equality == "!":
                if first_var == second_var:
                    return False
                if find_equality(first_var,second_var):
                    return False
                if find_equality(second_var,first_var):
                    return False
        return True

#attempt3: WA because didn't take care of a!=a
'''
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equality_eqns = {}
        for first_var,equality,_,second_var in equations:
            if equality == "=":
                if first_var not in equality_eqns:
                    equality_eqns[first_var] = set()
                if second_var not in equality_eqns:
                    equality_eqns[second_var] = set()
                equality_eqns[first_var].add(second_var)
                equality_eqns[second_var].add(first_var)
        
        def find_equality(parent,second_var,visited=set()):
            if parent not in equality_eqns:
                return False
            if second_var in equality_eqns[parent]:
                return True
            ans = False
            for equals in equality_eqns[parent]:
                if equals in visited:
                    continue
                ans = ans or find_equality(equals,second_var,visited|{parent})
            return ans
                
        
        for first_var,equality,_,second_var in equations:
            if equality == "!":
                if find_equality(first_var,second_var):
                    return False
                if find_equality(second_var,first_var):
                    return False
        return True
'''

#attempt2: RuntimeError because key not found
'''
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equality_eqns = {}
        for first_var,equality,_,second_var in equations:
            if equality == "=":
                if first_var not in equality_eqns:
                    equality_eqns[first_var] = set()
                if second_var not in equality_eqns:
                    equality_eqns[second_var] = set()
                equality_eqns[first_var].add(second_var)
                equality_eqns[second_var].add(first_var)
        
        def find_equality(parent,second_var,visited=set()):
            if second_var in equality_eqns[parent]:
                return True
            ans = False
            for equals in equality_eqns[parent]:
                if equals in visited:
                    continue
                ans = ans or find_equality(equals,second_var,visited|{parent})
            return ans
                
        
        for first_var,equality,_,second_var in equations:
            if equality == "!":
                if find_equality(first_var,second_var):
                    return False
                if find_equality(second_var,first_var):
                    return False
        return True
'''

#attempt1: TOOK HINT/CLUE WA
'''
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        equality_eqns = {}
        for first_var,equality,_,second_var in equations:
            if equality == "=":
                if first_var not in equality_eqns:
                    equality_eqns[first_var] = set()
                if second_var not in equality_eqns:
                    equality_eqns[second_var] = set()
                equality_eqns[first_var].add(second_var)
                equality_eqns[second_var].add(first_var)
        
        def find_equality(parent,second_var,visited=set()):
            if second_var in equality_eqns[parent]:
                return True
            for equals in equality_eqns[parent]:
                if equals in visited:
                    continue
                find_equality(equals,second_var,visited|{parent})
            return False
                
        
        for first_var,equality,_,second_var in equations:
            if equality == "!":
                if find_equality(first_var,second_var):
                    return False
        return True
'''
