import json


x = '{"name": "Ion", "age": 30, "city": "Iasi"}'
y = json.loads(x)
print(y, type(y))

# convert json to str
z = json.dumps(y)
print(z, type(z))

# a = json.dumps['mere', 'pere']
a = 'hello'
# a = 42
# a = 31.75
# a = True
print(a, json.dumps(a), type(a))