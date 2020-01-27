def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True if num != 1 else False


if __name__ == '__main__':
    print(is_prime(11))
