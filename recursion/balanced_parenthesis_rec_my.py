def solve(open, close, output, final_output):
    if open == 0 and close == 0:
        final_output.append(output)
        return

    if open != 0:
        op1 = output
        op1 += "("

        solve(open-1, close, op1, final_output)

    if close > open:
        op2 = output
        op2 += ")"
        solve(open, close-1, op2, final_output)



def generate_balanced_parenthesis(n):
    final_output = []
    open = n
    close = n
    output = ""

    solve(open, close, output, final_output)

    return final_output

if __name__ == "__main__":
    n = 3
    print(generate_balanced_parenthesis(n))
