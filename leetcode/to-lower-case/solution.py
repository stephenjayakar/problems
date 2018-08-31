class Solution:
    def toLowerCase(self, stringVal: str) -> str:
        def isUpperCase(char: str) -> bool:
            ordinal = ord(char)
            return ordinal >= ord('A') and ordinal <= ord('Z')

        def upperToLower(char: str) -> str:
            delta = ord('a') - ord('A')
            return chr(ord(char) + delta)

        returnVal = []
        for char in stringVal:
            returnVal.append(upperToLower(char)) if isUpperCase(char) else returnVal.append(char)
        return "".join(returnVal)


s = Solution()
print(s.toLowerCase("Ajay"))
print(s.toLowerCase("ASDF"))