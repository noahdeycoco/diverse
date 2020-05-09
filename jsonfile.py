import json

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'

jsonDataAsPythonValue = json.loads(stringOfJsonData)
print(type(jsonDataAsPythonValue))

jsonDump = json.dumps(stringOfJsonData)
print(jsonDump)
print(type(jsonDump))