# 读写文本文件要读写二进制文件  复制图片文件的功能
def main():
    try:
        with open('avatar.png', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        # 复制到这里
        with open('temp.png', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定文件无法打开')
    except IOError:
        print('读写文件时发生错误')
    print('程序执行结束')


if __name__ == '__main__':
    main()