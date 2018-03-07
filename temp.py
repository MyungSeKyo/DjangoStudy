class Temp:
    __con = "korea"

    def __init__(self, name):
        self.name = name

    @classmethod
    def foo(cls):
        print(cls.name)

    def foo2(self):
        print(self.name)
        print(self.__con)


a = Temp("a")
b = Temp("b")

a.foo()
a.foo2()
b.foo()
b.foo2()

