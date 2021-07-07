# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
    
    def next(self) -> int:
        _nestedList = self.nestedList
        while not _nestedList[0].isInteger():
            _nestedList = _nestedList[0].getList()
        val = _nestedList[0].getInteger()
        _nestedList.pop(0)
        # print(self.nestedList)
        return val
        
    def hasNext(self) -> bool:
        if not self.nestedList:
            return False
        if self.nestedList[0].isInteger():
            return True
        else:
            while self.nestedList:
                if self.nestedList[0].isInteger():
                    _nestedList = [self.nestedList[0]]
                else:
                    _nestedList = self.nestedList[0].getList()
                i = NestedIterator(_nestedList)
                if i.hasNext():
                    return True 
                else:
                    self.nestedList.pop(0)
                    # if self.nestedList[0].isInteger():
                    #     _nestedList = [self.nestedList[0]]
                    # else:
                    #     _nestedList = self.nestedList[0].getList()
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())