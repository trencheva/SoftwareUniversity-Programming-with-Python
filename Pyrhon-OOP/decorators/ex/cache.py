def cache(func):
    def wrapper(n):
        if not wrapper.log.get(n):
            result = func(n)
            wrapper.log[n] = result

        return wrapper.log[n]

    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)