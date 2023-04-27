def isValid(param):
    stack = []
    dict = {"]":"[", "}":"{", ")":"("}

    for char in param:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
            return False
    return stack == []


if __name__ == "__main__":

    print(isValid("()[{}]}"))