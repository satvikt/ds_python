"""
Given an sorted but infinite list of 0s and 1s, return the first occurrence of 1 in it (or last occurrence, if all 1s are before 0s)
"""


if __name__ == "__main__":
    list = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]

    print(list[0:"".join(str(i) for i in list).find('1')])