    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in reversed(s):
            if i == " ":
                if count>0:
                    return count
            else:
                count += 1 
        return count
