def main():
    prices = {
        'AAPL': 198.11,
        'cym': 122.22,
        'yyh': 113.11,
        'IBM': 231.11,
        'FB': 22
    }
    # 大于100的数字构成一个新的词典
    prices2 = {key: value for key, value in prices.items() if value > 100}
    print(prices2)


if __name__ == '__main__':
    main()
