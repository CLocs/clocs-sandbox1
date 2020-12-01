answers = {
    'kittensnettik': True,
    'abutuba': True,
    'a butt tuba': True,
    'farkllai': False,
    'dkaiekk i37348**': False,
    'IIIIIIIIIIIIIIIIIIIIIIIII': True
}


def palindrome_checker(in_str: str) -> bool:
    str2 = ''.join(in_str.split())

    max_comparisons = int(len(str2) / 2)

    for i in range(0, max_comparisons):
        if str2[i] != str2[-1 - i]:
            return False

    return True


def palindrome_checker_2(in_str: str):
    # Ignore Whitespace
    str2 = ''.join(in_str.split())

    # Method 1: Reverse and equal
    palindrome = False
    str2_rev = str2[::-1]
    if str2 == str2_rev:
        palindrome = True

    palindrome = False
    # Method 2: Check forwards and backwards at the same time
    for i in range(0, len(str2)):
        # Forward accumulate sub-str
        fwd_str = in_str[0:i + 1]
        # Backward accumulate sub-str
        rev_str = in_str[-1:len(in_str) - i]
        print(f'REV: {rev_str}\tFWD: {fwd_str}')

        # [0, 1, 2, 3]
        # i = 1
        # fwd: 0:1 --> 0 : i+1
        # bwd: 3:2 --> -1 : len-i
        # Check forward-backward are equal
        if fwd_str == rev_str:
            palindrome = True
        else:
            # If any asymmetry, then it aint a palindrome
            break
    return palindrome


if __name__ == '__main__':
    # Unit test-ish. Whatchu know about TDD?
    for string, answer in answers.items():
        if palindrome_checker(string) == answer:
            print('Good Job')
        else:
            print('Try Again')
