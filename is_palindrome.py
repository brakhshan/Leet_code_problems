    def isPalindrome(self, s: str) -> bool:
        chars = []
        for i in s:
            if i.isalnum():
                chars.append(i.lower())
        return chars == chars[::-1]
