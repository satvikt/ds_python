from data_structures.Stack import MyStack


def delete(s, k):
    if s.size() == 0:
        return

    return solve(s, k)


def solve(s,k):
    if k == 1:
        s.pop()
        return
    temp = s.pop()
    solve(s, k - 1)
    s.push(temp)
    return


if __name__ ==  "__main__":

    s = MyStack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    # s.push(5)

    k = s.size()//2 + 1

    delete(s,k)

    for i in range(s.size()):
        print(s.pop())