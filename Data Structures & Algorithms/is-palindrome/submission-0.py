class Solution:
    def isPalindrome(self, s: str) -> bool:
        key = "".join(c.lower() for c in s if c.isalnum())
        start = 0
        end = len(key)-1

        while start <= end:
            if key[start] != key[end]:
                return False
            start +=1
            end -=1
        return True
        