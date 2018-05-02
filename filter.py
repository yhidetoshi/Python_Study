# 条件にあった要素のみを抽出する

item = [1, 2, 3]

output = list( filter(lambda n:n%2==1,item) )
print(output)
