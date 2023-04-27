def bitCount(int_type):
    count = 0
    while(int_type):
        int_type &= int_type - b'1'
        count += 1
    return(count)

if __name__ == "__main__":
    bitCount(b'11111111111000000000')