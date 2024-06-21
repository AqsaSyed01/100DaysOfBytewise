def lcs(X, Y):
    m = len(X)
    r = len(Y)
    
    # Create a 2D array to store the lengths of LCS
    L = [[0] * (r + 1) for i in range(m + 1)]
    
    # Build the L array in bottom-up fashion
    for i in range(m + 1):
        for j in range(r + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    
    # Length of the LCS
    length_of_lcs = L[m][r]
    
    # Create a list to store the LCS
    lcs_string = [''] * length_of_lcs
    i = m
    j = r
    
    # Start from the bottom right corner and store characters in lcs_string
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_string[length_of_lcs - 1] = X[i - 1]
            i -= 1
            j -= 1
            length_of_lcs -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    return ''.join(lcs_string)

# Take input strings from the user
X = input("Enter the first string: ")
Y = input("Enter the second string: ")

# Get the LCS
result = lcs(X, Y)
print(f"The Longest Common Subsequence is: {result}")
