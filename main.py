def hanoi(n, start, end):
    if n == 1:
        print('%i to %i' % (start, end))
    else:
        temp = 6 - (start + end)
        hanoi(n - 1, start, temp)
        print('%i to %i' % (start, end))
        hanoi(n - 1, temp, end)


def main():
    hanoi(3, 1, 3)


if __name__ == "__main__":
    main()
