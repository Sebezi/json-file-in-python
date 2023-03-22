import json
#JSON data
print("\033c")  # to remove path
jsonFile = '{"name": "Temesgen", "age": "1"}'
print(type(jsonFile))
print("JSON file: "+jsonFile)

#To convert JSON to python dictionary file
pythonFile = json.loads(jsonFile)
print(type(pythonFile))
print("python file:"+str(pythonFile ))