# WAP to rename the key of a dictionary
dict = {
    'key1' : 'Suraj',
    'key2' : 'Arya' 
}

dict['key3'] = dict.pop('key1')
print(dict)