class Review:
    def __init__(self, title, content, author, date, pros, cons):
        self.__title = title
        self.__content = content
        self.__author = author
        self.__date = date
        self.__pros = pros
        self.__cons = cons

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self.__title = value
            print(f'Заголовок вашего обзора: {self.__title}')
        else:
            print(f'Заголовок не может быть написан числами!')





