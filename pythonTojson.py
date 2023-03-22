import json
# python dictionary file
print(" How to convert Python file  to JSON file?")
x = {
    "name": "Temesgen",
    "age":26,
    "sex": "male"
}
# To convert python file "x" to JSON file "y"
y = json.dumps(x)
print(type(x))
print("Python dictionary file: "+str(x))
print("JSON file in string form: "+ str(y))

djson = json.dumps({"name":"Mengaye","skill":"problem-solving"})
ljson = json.dumps([12,19,21,27])
sjson = json.dumps((4,6,8,10))

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
