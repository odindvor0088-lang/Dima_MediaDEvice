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


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        self.__author = value
        print(f'Другие пользователи будут видеть вас под ником: {self.__author}')


    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value


    @property
    def pros(self):
        return self.__pros.copy()

    @pros.setter
    def pros(self, value):
        self.__pros.append(value)



    @property
    def cons(self):
        return self.__cons.copy()

    @cons.setter
    def cons(self, value):
        self.__cons.append(value)



