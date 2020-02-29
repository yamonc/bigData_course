# 通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源
def main():
    try:
        with open('test.txt','r',encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定文件！')
    except LookupError:
        print('制定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')


if __name__ == '__main__':
    main()