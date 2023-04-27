def generate_rec(output, open, close, final):
    if open == 0 and close == 0:
        final.append(output)
        # print(final)
        return

    if open != 0:
        op1 = output
        op1 += "("
        generate_rec(op1, open-1, close, final)

    if close > open:
        op2 = output
        op2 += ")"
        generate_rec(op2, open, close-1, final)

    # return final

def generate_balanced_parenthesis(n):
    final = []
    open = n
    close = n
    output = ""
    generate_rec(output, open, close, final)

    return final


if __name__ == "__main__":
    n = 3
    print(generate_balanced_parenthesis(n))