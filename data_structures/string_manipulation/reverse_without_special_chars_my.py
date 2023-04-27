def reverse_special(param):
    index = -1

    for i in range(len(param)-1, int(len(param)/2), -1):
        # index += 1
        # if param[index].isalpha() and param[i].isalpha():
        #     temp = param[index]
        #     param[index] = param[i]
        #     param[i] = temp
        #
        if param[i].isalpha():
            temp = param[i]
            while True:
                index += 1
                if param[index].isalpha():
                    param[i] = param[index]
                    param[index] = temp
                    break
    return param


if __name__ == "__main__":
    str = "Ab,c,de!$"
    print("input: ", str)
    output = reverse_special(list(str))
    print("output: ", "".join(output))
