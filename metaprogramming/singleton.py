# A metaclass that enforces a Singleton pattern for classes.


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class TestClass(metaclass=Singleton):
    pass


a = TestClass()
b = TestClass()
# compare that a and b objects of the same class and the same instance
if a is b:
    print("a and b are the same")
