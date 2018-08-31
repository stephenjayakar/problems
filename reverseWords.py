# reverses the words in the string in place
def reverseWords(s: str) -> str:
    s = list(s)
    N = len(s)
    # first reverse string's characters
    i, j = 0, N - 1
    reverseSubstring(s, i, j)
    i, j = 0, 0
    reverse = False
    # for each word, reverse it
    for index in range(N):
        if s[index] == ' ' and reverse:
            j = index - 1
            reverseSubstring(s, i, j)
            reverse = False
        elif index == N - 1 and reverse:
            j = index
            reverseSubstring(s, i, j)
            reverse = False
        elif not reverse and s[index] != ' ':
            reverse = True
            i = index
    return "".join(s)
    

def reverseSubstring(s, i, j):    
    while i < j:
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        i += 1
        j -= 1
        

string = "hello guys my name is stephen jayakar"
print(string)
string = reverseWords(string)
print(string)
