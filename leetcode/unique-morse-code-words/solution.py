letterToMorse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
asciiStart = 97

def wordToMorse(word: str) -> str:
    representation = []
    for char in word:
        index = ord(char) - asciiStart
        representation.append(letterToMorse[index])
    return "".join(representation)

class Solution:
    def uniqueMorseRepresentations(self, words: list) -> int:
        representations = set()
        for word in words:
            representations.add(wordToMorse(word))
        return len(representations)


S = Solution()
print(S.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
