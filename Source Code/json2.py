import json
with open('d:/program/person.json') as f:
  data = json.load(f)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data)
