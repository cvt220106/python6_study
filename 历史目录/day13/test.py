# @Author : 杨佳杰
# @Time   : 2022/6/13 10:51
# @File   : test.py
def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    m = len(mat)
    n = len(mat[0])
    if r * c != m * n:
        return mat
    reshape = [[0 for _ in range(c)] for _ in range(r)]
    mat = [j for x in mat for j in x]
    k = 0
    for i in range(r):
        for j in range(c):
            reshape[i][j]=mat[k]
            k+=1
    return reshape

list1=[[1,2,3],[4,5,6]]
print(matrixReshape(list1,3,2))