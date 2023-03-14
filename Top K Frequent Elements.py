class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1


        print(freq)

        # able to extract both key and value from frequency using freq.items()
        # max = -sys.maxsize - 1
        # for k, v in freq.items(): 
        #     if v > max:
        #         max = v

        sorted_freq = dict(sorted(freq.items(), key = lambda kv: kv[1], reverse = True))
        print(sorted_freq)
        res = []
        j = 1
        for key, val in sorted_freq.items():
            if j <= k:
                res.append(key)
            j += 1
    
        return res
        