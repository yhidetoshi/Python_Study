# ex1-1 lambda式を使わない場合
def calc(price, tax):
    return price + (price * tax)

payment1 = calc(100, 0.08)
print(payment1)

# ex1-2 lambda式を利用(Goの無名関数)
## lambda 引数:処理内容
payment2 = (lambda price, tax : price + (price * tax))(100, 0.08)
print(payment2)

# ex2 引数なし
greeting = (lambda : 'hello')()
print(greeting)

# ex3
prices = [100, 1000, 10000]
paymentList = list(map(lambda price: price * 1.08, prices))
print(paymentList)

# ex4
myfunc = lambda x:x ** 2
print(myfunc(5))
print(myfunc(7))

# ex5
l1 = [(7, 2), (3, 4), (5, 5), (10, 3)]
l2 = sorted(l1, key=lambda x:x[1])
print(l2)
