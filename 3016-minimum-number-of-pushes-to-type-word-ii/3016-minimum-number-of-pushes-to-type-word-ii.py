class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}

        for ch in word:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        arr = list(freq.values())
        arr.sort(reverse=True)

        ans = 0

        for i in range(len(arr)):
            ans += arr[i] * (i // 8 + 1)

        return ans