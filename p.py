"""JSON's Lil' Helper"""
import json

with open('results.json', 'r') as f:
    data = f.read()

json_data = json.loads(data)

formatted_output = {}
formatted_array = []

for test in json_data['results']:
   formatted_test = {}
   test_name = test['name']
   ops_per_sec = test['1']['ops_per_sec']
   formatted_test['name'] = test_name
   formatted_test['results'] = { '1': { 'ops_per_sec': ops_per_sec } }
   formatted_array.append(formatted_test)

formatted_output = { 'results': formatted_array }

with open('dashboard.json', 'w') as outfile:
    json.dump(formatted_output, outfile)
