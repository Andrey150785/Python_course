import json

my_dict = {
    'Anrey': 1985,
    'Boris': 2000,
    'Chris': 1993,
    'a': 10,
    'b':{
    'c': [1, 2, 3]},
    'd': (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    324324: True
}

# print(my_dict)
converted_dict = json.dumps(my_dict)
# print(converted_dict)
loaded_dict = json.loads(converted_dict)
print(type(loaded_dict))