#Python program make dictionary from the string entered by user
def dictionary_from_string():
    my_dictionary = {}
    key_list = []
    value_list = []

    while True:
        my_str = input('Enter string or "done" to end: ')
        if my_str.lower() == 'done':
            break
        key_list.append(my_str)
        value_list.append(len(my_str))

    for key, value in zip(key_list, value_list):
        my_dictionary[key] = value

    return my_dictionary


result = dictionary_from_string()
print(f'My dictionary is: {result}')
