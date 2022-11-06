import json
x = '{"name":"ravi", "age":22, "city":"nagar"}'
y = json.loads(x)
print(y["city"])