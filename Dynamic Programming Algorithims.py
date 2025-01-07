# Dynamic Programming for Longest Palindrome Subsequence: O(n^2)

def longestPalindromeSubsequence(s: str):
    length = len(s)
    table = [[""] * length for _ in range(length)] #Dynamic Programming Table
    for i in range(length):
        table[i][i] = s[i]
    for l in range(2, length + 1):
        for i in range(length - l + 1):
            j = i + l - 1
            if s[i] == s[j]:
                table[i][j] = s[i] + table[i + 1][j - 1] + s[j]
            else:
                if len(table[i + 1][j]) > len(table[i][j - 1]):
                    table[i][j] = table[i + 1][j]
                else:
                    table[i][j] = table[i][j - 1]
    return table[0][length - 1]

# Test:

print(longestPalindromeSubsequence('banana'))
print(longestPalindromeSubsequence('character'))
print(longestPalindromeSubsequence('million'))
print(longestPalindromeSubsequence('amazing'))
print(longestPalindromeSubsequence('ghost'))

# Printing neatly with Dynamic Programming: O(logn^2):

def printNeatly(text, max):
    words = text.split()
    length = len(words)
    word_lengths = [len(word) for word in words]
    spaces = [[0] * length for _ in range(length)]
    for i in range(length):
        spaces[i][i] = max - word_lengths[i]
        for j in range(i + 1, length):
            spaces[i][j] = spaces[i][j - 1] - word_lengths[j] - 1
    line_cost = [[0] * length for _ in range(length)]
    for i in range(length):
        for j in range(i, length):
            if spaces[i][j] < 0:
                line_cost[i][j] = float('inf')
            elif j == length - 1:
                line_cost[i][j] = 0
            else:
                line_cost[i][j] = spaces[i][j] ** 3
    cost = [0] * (length + 1)
    breaks = [0] * (length + 1)
    for i in range(length - 1, -1, -1):
        cost[i], breaks[i] = min((line_cost[i][j] + cost[j + 1], j) for j in range(i, length))
    i = 0
    while i < length:
        print(' '.join(words[i:breaks[i] + 1]))
        i = breaks[i] + 1
        
#Test
        
printNeatly("Dynamic programming is not that difficult.", 15)
printNeatly("Algorithm is my favorite subject.", 16)
printNeatly("The weather is very nice today. I'm glad it's not raining", 15)
printNeatly("It's a bummer when it rains, I don't like wearing a rain coat. How about you?", 20)




    
    
    
    
    