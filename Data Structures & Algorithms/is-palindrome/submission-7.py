class Solution:
    def isPalindrome(self, s: str) -> bool:
        i1 = 0
        i2 = len(s) - 1
        while i1 < i2:
            while (i1 < i2 and s[i1] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"):
                i1 += 1;
            while (i1 < i2 and s[i2] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"):
                i2 -= 1;
            print(i1, i2)
            if(s[i1].lower() != s[i2].lower()):
                return False
            i1 += 1;
            i2 -= 1;
        return True