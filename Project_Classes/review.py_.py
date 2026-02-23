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


    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        if isinstance(value, str):
            self.__content = value
            print(f'Текст вашего обзора(Проверьте, всё ли вы правильно указали.): {self.__content}')
        else:
            print(f'Обзор не может состоять только из чисел!')





