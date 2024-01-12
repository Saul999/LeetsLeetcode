class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #  1  2  3
        # [2, 3, 4]

        print(len(numbers))
        print(numbers[1])
        """
        for i  in range(len(numbers) -1):
            for j in range(len(numbers) -1):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
                j+=1
            i+= 1


        print(numbers)
        """
        l, r = 0, (len(numbers) - 1)
        if len(numbers) - 1 <= 2:
            return l + 1, r + 1
        while l < r:
            print(l)
            print(r)
            if numbers[r] >= target:
                r -= 1
            if numbers[l] + numbers[r] == target:
                return l + 1, r + 1

        print(r)
