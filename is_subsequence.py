def isSubsequence(self, s: str, t: str) -> bool:
    i = 0
    j = 0
    while i < len(s):
        if j >= len(t):
            return False
        if s[i] == t[j]:
            j = j + 1
            i = i + 1
        else:
            j = j + 1
    return True
