"""
map関数はリストのような複数の要素をもったオブジェクト（これをシーケンスと呼びましたね）と
関数を引数として受け取ります。
そしてシーケンスの各要素を、受け取った関数に渡して実行してくれます。
このように関数を受け取る関数を高階関数と呼びます。
"""

item = [1, 2, 3]

def add(n):
    return n + 10

result = list(map(add, item))
print(result)
print(item)

result2 = list(map(lambda n : n+10,item))
print(result2)
