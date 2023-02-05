from base import log

@log(level="debug")
def hello(name: str = "world"):
    print("hello " + name)


hello("james")
