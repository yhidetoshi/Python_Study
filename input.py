#N = input()
#print(N)

# 半角スペース区切りの場合
"""
input1, input2, input3 = map(int, input().split())
print(input1, input2, input3)
"""

# 入力回数を指定して、改行して数を回数分入力する
N = int(input())

list=[]
for i in range(N):
    list.append(int(input()))

print(list)
