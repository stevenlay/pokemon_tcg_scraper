class Expansion:
    def __init__(self, name, url, series, start, end, has_pad=False):
        self.__name = name
        self.__url = url
        self.__series = series
        self.__start = start
        self.__end = end
        self.__has_pad = has_pad

    def get_name(self):
        return self.__name

    def get_url(self):
        return self.__url

    def get_series(self):
        return self.__series

    def get_start(self):
        return self.__start

    def get_end(self):
        return self.__end

    def has_pad(self):
        return self.__has_pad
