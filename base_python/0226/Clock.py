from time import sleep, localtime, time


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法
        :param hour:时
        :param minute:分
        :param second:秒
        """
        self._hour = hour
        self._minute = minute
        self._seconde = second

    @classmethod
    def now(cls):
        """
        类中定义类方法
        :return:
        """
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._seconde += 1
        if self._seconde == 60:
            self._seconde = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._seconde)


def main():
    # 通过类方法创建对象并获取系统时间

    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
