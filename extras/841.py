class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        #check first pos map keys there
        #next position check map to see if we have the next key
        keys = set([0])
        for i in range(len(rooms)):
            if i not in keys:
                return False
            print(rooms[i])
            for j in range(len(rooms[i])):
                # print(rooms[i][j])
                keys.add(rooms[i][j])
        print(keys)
        return True
            