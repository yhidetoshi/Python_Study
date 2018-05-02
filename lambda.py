# ex1-1 lambda式を使わない場合
def calc(price, tax):
    return price + (price * tax)

payment1 = calc(100, 0.08)
print(payment1)

# ex1-2 lambda式を利用(Goの無名関数)
## lambda 引数:処理内容
payment2 = (lambda price, tax : price + (price * tax))(100, 0.08)
print(payment2)

# ex2
greeting = (lambda : 'hello')()
print(greeting)
