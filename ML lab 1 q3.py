
def matPow(mat, pow):
    result = mat
    for p in range(pow - 1):
        new = []
        for i in range(len(mat)):
            row = []
            for j in range(len(mat)):
                total = 0
                for k in range(len(mat)):
                    total = total + result[i][k] * mat[k][j]
                row.append(total)
            new.append(row)
        result = new
    return result
mat = [[1, 2],
          [3, 4]]
pow = 2
answer = matPow(mat,pow)
print("A^", pow, "=", sep="")
for row in answer:
    print(row)