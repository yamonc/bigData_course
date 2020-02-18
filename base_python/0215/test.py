class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test.__bar()
    print(test.__foo)


if __name__ == "__main__":
    main()
