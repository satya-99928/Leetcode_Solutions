from collections import Counter
import math

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        count = Counter(s)
        
        # 1. Quick validation checks
        odd_chars = [char for char, freq in count.items() if freq % 2 == 1]
        if len(odd_chars) > 1:
            return ""
            
        mid_char = odd_chars[0] if odd_chars else ""
        
        # 2. Setup the half pool frequencies
        pool_counts = {char: freq // 2 for char, freq in count.items() if freq // 2 > 0}
        distinct_chars = sorted(pool_counts.keys())
        total_chars = sum(pool_counts.values())
        
        # 3. Precompute factorials up to length of half_pool to run in O(1)
        fact = [1] * (total_chars + 1)
        for i in range(1, total_chars + 1):
            fact[i] = fact[i-1] * i
            
        # 4. Compute total combinations using a fast denominator product loop
        denom = 1
        for freq in pool_counts.values():
            denom *= fact[freq]
        
        total_perms = fact[total_chars] // denom
        if k > total_perms:
            return ""
            
        # 5. Fast state-based permutation matching
        left_half = []
        remaining_len = total_chars
        
        for _ in range(total_chars):
            for char in distinct_chars:
                if pool_counts[char] > 0:
                    # Combinatorial optimization: perms = (remaining_len - 1)! / (∏ freq!)
                    # We look at what happens if we reduce the frequency of 'char' by 1
                    freq = pool_counts[char]
                    
                    # New perms = (total_perms * freq) // remaining_len
                    current_perms = (total_perms * freq) // remaining_len
                    
                    if k <= current_perms:
                        left_half.append(char)
                        pool_counts[char] -= 1
                        total_perms = current_perms
                        remaining_len -= 1
                        break
                    else:
                        k -= current_perms
                        
        left_str = "".join(left_half)
        return left_str + mid_char + left_str[::-1]