class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for s in strs:
            char_freqs = [0]*26
            for c in s: 
                c_freq_index = ord(c)-ord('a')
                char_freqs[c_freq_index] += 1
    
            anagram_groups[tuple(char_freqs)].append(s)
        
        return list(anagram_groups.values())

                


        
        