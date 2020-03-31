def joined_interleave(interleave):  # format
    return "".join(interleave)


def print_single_interleave(s1, s2, inter, row, col, index):  # Recursive print function

    if row == 0 and col == 0:
        print(joined_interleave(inter))

    if row != 0:
        inter[index] = s1[0]
        print_single_interleave(s1[1:], s2, inter, row - 1, col, index + 1)

    if col != 0:
        inter[index] = s2[0]
        print_single_interleave(s1, s2[1:], inter, row, col - 1, index + 1)


def print_interleaves(s1, s2, row, col):
    inter = [''] * (row + col)
    print("\nThe interleavings are:\n")
    print_single_interleave(s1, s2, inter, row, col, 0)


str1 = input("Enter the string str1: ")
str2 = input("Enter the string str2: ")

print_interleaves(str1, str2, len(str1), len(str2))
