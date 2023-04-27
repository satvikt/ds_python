"""
For the given encoding scheme => A=1,B=2...Z=26, given a sequence of digits, find the number of valid letter combinations that can be decoded from them.

E.g. "123" gives ABC(1&2&3), LC(12 & 3) and AW(1&23)
"121" gives ABA(1&2&1), LA(12&1) and AT(1&21)
"12345" gives ABCDE(1&2&3&4&5), LCDE(12&3&4&5) and AWDE(1&23&4&5)

Note that the combinations should be such that all the digits are consumed. Partial consumption is not allowed.
For example, 12345 gives A(1), W(23) and NULL(45). Hence, AW is discarded.

Constraints
1. 0s are allowed. But there are no leading/trailing/2 or more successive zeroes in between

Input Type = String
Return Type - Int

Doubt
-----
in case of 102, is AB(1&02) allowed or discarded due to 0??

The program below allows this combination, otherwise any sequence with 0 would have NIL count.
And what would have been the point of allowing 0 (as a middle element) in the first place?

Baki, one valid is JB (10&2)

"""


def get_digits(string):
    lis = []
    num = int(string)
    while num > 0:
        lis.append(num%10)
        num = num // 10
    lis.reverse()
    return lis


def decode(string):
    lis = get_digits(string)
    if 0 in lis:
        count = 0 # single digits can't be cast into a valid combination
    else:
        count = 1

    i,j = 0,0

    # maintain a sliding window of length 2 as the max encoding allowed is 26 (for Z)
    window = []

    while j < len(lis):
        window.append(lis[j])
        if j-i+1 < 2:
            j += 1
        elif j-i+1 == 2: # we hit the required window size. Maintain it
            if lis[i] == 0: # check for leading zero
                continue
            temp_num = int("".join(str(x) for x in window))
            window = window[1:]
            if temp_num < 26:
                count += 1

            i += 2  # can't overlap successive windows
            j += 2
        # else:
        #     window.pop(i)
        #     i +=1


    # while()
    print(count)



if __name__ == "__main__":
    # decode("123")
    decode("12112")
    # decode("12345")
    # decode("1203")
