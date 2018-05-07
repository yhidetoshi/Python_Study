class Person(object):
    """
    __init__ はインスタンスが生成されたときに呼ばれる(コンストラクタのようなもの)
    person = Person('hide')で呼び出され、 name=hideが格納される
    """
    def __init__(self, name):
        self.name = name
    def greet(self):
        print ("my name is %s" % self.name)

# インスタンスオブジェクト
person = Person('hide')

print(person.name)
person.greet()
