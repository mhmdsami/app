def curryAdd(a):
    def add(b):
        return a + b
    return add

res = curryAdd(22)(93)
print(res)
