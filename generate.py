import random
import sys

def generate_numbers(count, min_val=-100000, max_val=100000):
    return random.sample(range(min_val, max_val+1), count)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 generator.py <count>")
        sys.exit(1)

    n = int(sys.argv[1])
    numbers = generate_numbers(n)
    print(" ".join(map(str, numbers)))
