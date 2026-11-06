class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""

        # Frequency map for characters required by t
        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        window = {}
        have = 0
        need = len(count_t)

        # Result trackers: [length, l_idx, r_idx]
        res = [-1, -1]
        res_len = float("inf")

        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            # Only increment 'have' when exact required frequency is first met
            if char in count_t and window[char] == count_t[char]:
                have += 1

            # Shrink from the left while window satisfies all requirements
            while have == need:
                # Update minimum window record
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res = [l, r]

                # Discard s[l] from window
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        l_idx, r_idx = res
        return s[l_idx : r_idx + 1] if res_len != float("inf") else ""