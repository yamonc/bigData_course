class Picture:
    def __init__(self,data):
        self.__dict__=data


    def __str__(self):
        return ("picture: id:%s author:%s width:%s height:%s url:%s download_url:%s" % (self.id, self.author, self.width, self.height, self.url, self.download_url))


    def __getitem__(self, item):
        return self.__dict__

