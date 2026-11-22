class solution():
    def twosum(self,nums:list[int], target:int) -> list[int]:
        #create an empty dictionery to store the numbers and their index.
        seen = {}
        #loop through the list getting both index and their values
        for i , num in enumerate(nums):
            complement = target - num
            if complement in seen:
                 return [seen[complement], i]
            seen[num] = i
