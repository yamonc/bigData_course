# 把一个列表或者一个字典中的数据保存到文件中 数据以JSON格式进行保存
# dump - 将Python对象按照JSON格式序列化到文件中
# dumps - 将Python对象处理成JSON格式的字符串
# load - 将文件中的JSON数据反序列化成对象
# loads - 将字符串的内容反序列化成Python对象
import json


def main():
    mydict = {
        'name': '陈亚萌',
        'age': 22,
        'qq': 123456,
        'friend': ['杨永慧', '李元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 188},
            {'brand': 'Audi', 'max_speed': 200},
            {'brand': 'Benz', 'max_speed': 122},
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成')


if __name__ == '__main__':
    main()
