def lcs(S1, S2):
    m, n = len(S1), len(S2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S1[i - 1] == S2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = m, n
    lcs_sequence = []

    while i > 0 and j > 0:
        if S1[i - 1] == S2[j - 1]:
            lcs_sequence.append(S1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs_sequence.reverse()

    print("\nMatriz DP:")
    for row in dp:
        print(row)

    print("\nComprimento da LCS:", dp[m][n])
    print("LCS encontrada: ", ''.join(lcs_sequence))

    return dp[m][n], ''.join(lcs_sequence)

S1 = "AGGTAB"
S2 = "GXTXAYB"
lcs(S1, S2)
