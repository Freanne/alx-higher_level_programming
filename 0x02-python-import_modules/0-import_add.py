a = 1
b = 2
exec(compile(open("add_0.py", "rb").read(), "add_0.py", 'exec'))

result = add(a, b)
print("{} + {} = {}".format(a, b, result))
