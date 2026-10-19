class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {} # [0] * 26 : ["act", "cat"]
        for i in strs:
            arr = [0] * 26
            for j in i:
                arr[ord(j) - ord('a')] += 1
            key = tuple(arr)
            if key in freq:
                freq[key].append(i)
            else:
                freq[key] = [i]
        return list(freq.values())