#HIGHEST ALTITUDE 17432

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        altitude = 0
        highest = 0

        for i in range(len(gain)):
            altitude += gain[i]
            if altitude > highest:
                highest = altitude
        return highest