"""
Suppose you have a dictionary like:

{'a': 1,
 'c': {'a': 2,
       'b': {'x': 5,
             'y' : 10}},
 'd': [1, 2, 3]}
How would you go about flattening that into something like:

{'a': 1,
 'c_a': 2,
 'c_b_x': 5,
 'c_b_y': 10,
 'd': [1, 2, 3]}
"""

def flatten_dict(input, divider="_", output = {}, parent_key = ""):
    # if isinstance(input.values(),
    for key, val in input.items():
        if isinstance(val, dict) != True:
            if parent_key:
                parent_key += key + divider
            else:
                output[key] = val
        else:
            parent_key += key + divider
            flatten_dict(val, divider, output, parent_key)

    # return output
    # print(output)

if __name__ == "__main__":
    input = {'a': 1,
 'c': {'a': 2,
       'b': {'x': 5,
             'y' : 10}},
 'd': [1, 2, 3]}

    print(flatten_dict(input))
