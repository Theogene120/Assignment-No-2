#Python program to take sentence separete into words

def my_function():
    my_dictionary = {}
    sentence = input('Enter sentence:\n')
    words = sentence.split()

    for word in words:
        if word in my_dictionary:
            my_dictionary[word] += 1

        else:
            my_dictionary[word] = 1

    return my_dictionary


result = my_function()
print(f'My dictionary is:{result}')