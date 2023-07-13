

def string_reverse1(in_str: str) -> str:
    out_str = ''
    for i in range(-1, -len(in_str)-1, -1):
        out_str += in_str[i]
    return out_str


def string_reverse2(in_str: str) -> str:
    in_list = list(in_str)
    in_list.reverse()
    out_str = ''.join(in_list)
    return out_str


if __name__ == '__main__':
    input = 'reverse this'

    out1 = string_reverse1(input)
    print(f"Reverse1: {out1}")

    out2 = string_reverse2(input)
    print(f"Reverse2: {out2}")
