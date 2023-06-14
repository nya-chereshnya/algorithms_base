
text_1 = str(input())
text_2 = str(input())

# D = [[0 for i in range(len(text_1)+1)] for i in range(len(text_2))+1]


def show_m(m):
    for i in range(len(m)):
        print(m[i])
    print()


def edit_test_BU(A, B):
    D = [[0 for i in range(len(text_1)+1)] for j in range(len(text_2)+1)]
    for i in range(len(text_1)+1):
        # print(i)
        D[0][i] = i
    for j in range(len(text_2)+1):
        # print(j)
        D[j][0] = j

    for i in range(1, len(text_1)+1):
        for j in range(1, len(text_2)+1):
            # c = 1 if A[i-1] == B[j-1] else 0
            # show_m(D)
            # print(i, j)
            ins = D[j][i - 1] + 1
            rem = D[j - 1][i] + 1
            sub = D[j - 1][i - 1] + (1 if text_1[i-1] != text_2[j-1] else 0)
            D[j][i] = min(ins, rem, sub)
    # show_m(D)
    return D


print(edit_test_BU(text_1, text_2)[-1][-1])

# for i in range(1, len(text_2)+1):
#     for j in range(1, len(text_1)+1):
#         edit_dist_TD(i, j)
# print(matrix)

# show_m()
# print(matrix[-1][-1])
