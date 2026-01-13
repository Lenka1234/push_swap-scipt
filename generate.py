import random
import sys

INT_MIN = -2147483648
INT_MAX = 2147483647
ULLONG_MAX = 18446744073709551615


def generate_numbers(count, min_val=-100000, max_val=100000):
    return random.sample(range(min_val, max_val + 1), count)


def edge_cases():
    return [INT_MIN, INT_MIN + 1, -1, 0, 1, INT_MAX - 1, INT_MAX]


def overflow_cases():
    return [INT_MIN - 1, -259, 32, INT_MAX, 0, INT_MAX + 1]


def big_overflow():
    return [
        25,
        -0,
        ULLONG_MAX,
        13,
        -1259,
        7,
    ]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 generate.py <count|edge|overflow|big_overflow>")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "edge":
        nums = edge_cases()
        print(" ".join(map(str, nums)))

    elif mode == "overflow":
        nums = overflow_cases()
        print(" ".join(map(str, nums)))

    elif mode == "big_overflow":
        nums = big_overflow()
        print(" ".join(map(str, nums)))

    else:
        n = int(mode)
        nums = generate_numbers(n)
        print(" ".join(map(str, nums)))
