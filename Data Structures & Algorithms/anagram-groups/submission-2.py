class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # similar to anagrams
        # fixed array with freq
        # then map strings to that freq
        # unique freq get their own key
        freq = {}

        for word in strs:
            arr = [0] * 26
            for char in word:
                arr[ord(char) - ord('a')] += 1

            key = tuple(arr)
            if key in freq:
                freq[key].append(word)
            else:
                freq[key] = [word]
            
        return list(freq.values())