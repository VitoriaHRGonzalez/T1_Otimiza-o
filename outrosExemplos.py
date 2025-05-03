# # Código do item C:

def lcs_recursive(S1, S2, m, n):
    if m == 0 or n == 0:
        return 0
    if S1[m - 1] == S2[n - 1]:
        return 1 + lcs_recursive(S1, S2, m - 1, n - 1)
    else:
        return max(lcs_recursive(S1, S2, m - 1, n),
                   lcs_recursive(S1, S2, m, n - 1))


# # Código do item D:

def lcs_dp(S1, S2):
    m, n = len(S1), len(S2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if S1[i-1] == S2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

# Código do intem f:
import time

def lcs_verbose(S1, S2):
    m, n = len(S1), len(S2)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    iter_count = 0

    start = time.time()

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            iter_count += 1
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
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    lcs_sequence.reverse()

    end = time.time()

    print("\nMatriz DP:")
    for row in dp:
        print(row)

    print("\nComprimento da LCS:", dp[m][n])
    print("LCS encontrada:", ''.join(lcs_sequence))
    print("Iteracoes:", iter_count)
    print(f"Tempo: {end - start:.6f} segundos")

    return dp[m][n], ''.join(lcs_sequence)

S1 = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
S2 = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
lcs_verbose(S1, S2)


# Código do intem g:

import time

def lcs_instrumented(S1, S2):
    m, n = len(S1), len(S2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    iter_count = 0
    start = time.time()

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            iter_count += 1
            if S1[i - 1] == S2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    end = time.time()
    print(f"Iteracoes: {iter_count}")
    print(f"Tempo: {end - start:.6f} segundos")
    return dp[m][n]

S1 = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
S2 = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
resultado = lcs_instrumented(S1, S2)
print("Comprimento da LCS:", resultado)

