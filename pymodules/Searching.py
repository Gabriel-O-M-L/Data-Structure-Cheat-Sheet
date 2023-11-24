class stringSearch:
    def KMP(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: int
        """
        if not pattern:
            return 0
        if not text:
            return -1
        next = self.getNext(pattern)
        i, j = 0, 0
        while i < len(text) and j < len(pattern):
            if j == -1 or text[i] == pattern[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == len(pattern):
            return i - j
        return -1

    def BooyerMoore(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: int
        """
        if not pattern:
            return 0
        if not text:
            return -1
        last = self.buildLast(pattern)
        n, m = len(text), len(pattern)
        i = m - 1
        j = m - 1
        while i < n:
            if text[i] == pattern[j]:
                if j == 0:
                    return i
                else:
                    i -= 1
                    j -= 1
            else:
                lo = last[ord(text[i])]
                i = i + m - min(j, 1 + lo)
                j = m - 1
        return -1


