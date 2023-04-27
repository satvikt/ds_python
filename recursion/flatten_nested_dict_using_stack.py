def flatten_nested_dict(nested):
    stack = list(nested.items())
    ans = {}
    while stack:
        key, val = stack.pop()
        if isinstance(val, dict):
            for sub_key, sub_val in val.items():
                stack.append((f"{key}_{sub_key}", sub_val))
        else:
            ans[key] = val
    return ans

if __name__ == "__main__":
    input = {'a': 1,
 'c': {'a': 2,
       'b': {'x': 5,
             'y' : 10}},
 'd': [1, 2, 3]}
    print(flatten_nested_dict(input))