def anagrams(word):
    if len(word) < 2:
        yield word
    else:
        # tmp = []
        for i, letter in enumerate(word):
            if letter not in word[:i]:
                for j in anagrams(word[:i] + word[1+i:]):
                   yield j+letter
        # return tmp


if __name__ == "__main__":
    # print(anagrams("aabc"))
    for i in anagrams("aac"):
        print(i)