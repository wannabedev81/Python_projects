def hello():
    print("hello")

print(hello)

#hi = hello
#hi()

say = print

say("Hello")

## Higher order functions - - except function as arguments OR returns a function

1.
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(function):

    text = function("Hello")
    print(text)

hello(loud)
hello(quiet)

2.
def devisor(x):
    def dividend(y):
        return y / x
    return dividend

devide = devisor(2)
print(devide(10))