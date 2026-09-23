class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_char_counts = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            str_char_counts[tuple(count)].append(s)
        return list(str_char_counts.values())