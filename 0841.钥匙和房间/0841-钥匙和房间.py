class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = []
        keys.append(0)
        
        while keys:
            key = keys.pop()
            if rooms[key]:
                for k in rooms[key]:
                    keys.append(k)
                rooms[key] = None #visited
        
        for room in rooms:
            if room:
                return False
        return True