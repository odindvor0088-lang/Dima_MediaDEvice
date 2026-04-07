from datetime import datetime

from src.review.status_review_enum import ReviewStatus
from src.review.review_exception import *


class Review:
    """Класс для представления обзора"""
    def __init__(self, title: str, content: str, author: str = "Эксперт",
                 status: ReviewStatus = ReviewStatus.PUBLISHED,
                 date: datetime = None,
                 pros: list[str] = None,
                 cons: list[str] = None) -> None:
        """
        Инициализация объекта Review.

        :param title: заголовок обзора
        :type title: str
        :param content: текст обзора
        :type content: str
        :param author: автор обзора; по умолчанию — «Эксперт»
        :type author: str
        :param status: статус обзора; по умолчанию — ReviewStatus.PUBLISHED
        :type status: ReviewStatus
        :param date: дата создания обзора; если None — устанавливается текущая дата и время
        :type date: datetime | None
        :param pros: список плюсов устройства; если None — инициализируется пустым списком
        :type pros: list[str] | None
        :param cons: список минусов устройства; если None — инициализируется пустым списком
        :type cons: list[str] | None
        """
        # Используем property
        self.title = title
        self.content = content
        self.author = author
        self.status = status
        self.date = date
        self.pros = pros
        self.cons = cons

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Review для отладки.

        :return: строковое представление экземпляра класса
        :rtype: str
        """
        return (f"Review(title = {self.title!r}, content = {self.content!r}, author = {self.author!r},"
                f" date = {self.date}, pros = {self.pros}, cons = {self.cons} )")

    def __str__(self) -> str:
        """
        Возвращает пользовательское строковое представление объекта Review.

        :return: описание обзора для пользователя
        :rtype: str
        """
        return (f"Создано ревью состоящее из: (title = {self.title}, content = {self.content}, author = {self.author},"
                f" date = {self.date}, pros = {self.pros}, cons = {self.cons} )")

    @property
    def title(self) -> str:
        """
        Возвращает текущий заголовок обзора.

        :return: заголовок обзора
        :rtype: str
        """
        return self.__title

    @title.setter
    def title(self, value: str) -> None:
        """
        Устанавливает заголовок.

        :param value: Новый текст заголовка.
        :raises TypeError: Если value не является строкой.
        :raises EmptyReviewFieldError: Если value пустая строка или состоит только из пробелов.
        :return: None.
        """
        if not isinstance(value, str):
            raise TypeError(f"Заголовок должен быть str, получен {type(value).__name__}")

        if value.strip():
            self.__title = value
        else:
            raise EmptyReviewFieldError("title")

    @property
    def content(self) -> str:
        """
        Возвращает текст обзора.

        :return: текст обзора
        :rtype: str
        """
        return self.__content

    @content.setter
    def content(self, value: str) -> None:
        """
         Устанавливает новый текст обзора.

        :param value: новый текст обзора
        :type value: str
        :raises ValueError: если value не является строкой
        """
        if isinstance(value, str):
            self.__content = value
            print(f'Текст вашего обзора(Проверьте, всё ли вы правильно указали.): {self.__content}')
        else:
            print(f'Обзор не может состоять только из чисел!')

    @property
    def author(self) -> str:
        """
        Возвращает имя автора обзора.

        :return: имя автора
        :rtype: str
        """
        return self.__author

    @author.setter
    def author(self, value: str) -> None:
        """
        Устанавливает имя автора обзора.

        :param value: новое имя автора
        :type value: str
        """
        if isinstance(value, str):
            self.__author = value
        print(f'Другие пользователи будут видеть вас под ником: {self.__author}')

    @property
    def date(self) -> datetime:
        """
        Возвращает дату создания обзора.

        :return: дата и время создания обзора
        :rtype: datetime
        """
        return self.__date

    @date.setter
    def date(self, new_date: datetime) -> None:
        """
                Устанавливает дату создания обзора.

                Если передано None, устанавливается текущая дата и время.

                :param new_date: новая дата создания обзора
                :type new_date: datetime | None
                :raises ValueError: если new_date не является экземпляром datetime
                """
        if new_date is None:
            self.__date = datetime.now()
        elif isinstance(new_date, datetime):
            self.__date = new_date
        else:
            print(f'new_date должна быть экземпляром класса datetime!')


    @property
    def pros(self) -> list[str]:
        """
        Возвращает копию списка плюсов обзора.

        :return: копия списка плюсов
        :rtype: list[str]
        """
        return self.__pros.copy()

    @pros.setter
    def pros(self, list_pros: list[str]) -> None:
        """
        Устанавливает новый список плюсов обзора.

        Если передан None, инициализируется пустой список. Сохраняется копия списка для инкапсуляции.

        :param list_pros: новый список плюсов
        :type list_pros: list[str] | None
        :raises ValueError: если list_pros не является списком
        ."""
        if list_pros is None:
            self.__pros = []
        elif isinstance(list_pros, list):
            self.__pros = list_pros.copy()
        else:
            print(f'list_pros должен быть списком строк!')


    @property
    def cons(self) -> list:
        """
        Возвращает копию списка минусов обзора.

        :return: копия списка минусов
        :rtype: list[str]
        """
        return self.__cons.copy()

    @cons.setter
    def cons(self, list_cons: list) -> None:
        """
        Устанавливает новый список минусов обзора.

        Если передан None, инициализируется пустой список. Сохраняется копия списка для инкапсуляции.

        :param list_cons: новый список минусов
        :type list_cons: list[str] | None
        :raises ValueError: если list_cons не является списком
        """
        if list_cons is None:
            self.__cons = []
        elif isinstance(list_cons, list):
            self.__cons = list_cons.copy()
        else:
            print(f'list_cons должен быть списком строк!')

    @property
    def status(self) -> ReviewStatus:
        """
        Возвращает статус обзора.

        :return: статус обзора
        :rtype: ReviewStatus
        """
        return self.__status

    @status.setter
    def status(self, new_status: ReviewStatus | str) -> None:
        """
        Устанавливает новый статус обзора.

        :param new_status: новый статус обзора
        :type new_status: ReviewStatus | str
        :raises ValueError: если new_status не является допустимым статусом из ReviewStatus
        """
        if new_status in ReviewStatus:
            self.__status = new_status
        else:
            print(f"new_status must be attribute in ReviewStatus!")

    def add_pro(self, pro_text: str) -> None:
        """
        Добавляет новый плюс в список.
        :param pro_text: текст плюса
        """
        if not isinstance(pro_text, str):
            print(f'Плюс должен быть строкой!')
        elif not pro_text.strip():
            print(f'Плюс не может быть пустой строкой!')
        elif len(pro_text) > 200:
            print(f'Текст плюса слишком длинный')
        else:
            self.__pros.append(pro_text)
            print(f'Ваш плюс добавлен✅')

    def add_con(self, con_text: str) -> None:
        """
        Добавляет новый минус в список.
        :param con_text: текст минуса
        """
        if not isinstance(con_text, str):
            print(f'Минус должен быть строкой!')
        elif not con_text.strip():
            print(f'Минус не может быть пустой строкой!')
        elif len(con_text) > 200:
            print(f'Текст минуса слишком длинный')
        else:
            self.__pros.append(con_text)
            print(f'Ваш минус добавлен✅')

    def remove_pro(self, index: int) -> None:
        """
        Удаляет плюс по индексу.
        :param index: индекс плюса
         """
        if -len(self.__pros) <= index < len(self.__pros):
            removed = self.__pros.pop(index)
            print(f"Плюс '{removed}' удалён")
        else:
            print(f'Индекс {index} вне диапазона')

    def remove_con(self, index: int) -> None:
        """
        Удаляет минус по индексу.
        :param index: индекс минуса
        """
        if -len(self.__cons) <= index < len(self.__cons):
            removed = self.__cons.pop(index)
            print(f"Минус '{removed}' удалён")
        else:
            print(f'Индекс {index} вне диапазона')

    @classmethod
    def from_dict(cls, data: dict) -> Review | None:
        """
        Метод обрабатывает словарь с характеристиками
        Если в словаре недопустимый ключ, то код выдаст ошибку

        :param data: СЛОВАРЬ С ХАРАКТЕРИСТИКАМИ МОДЕЛИ
        :return: 'Device'
        """
        true_keys = ['title', 'content']
        for key in true_keys:
            if key not in data:
                print(f"неверный ключ '{key}'")
                return None

        return cls(
            title=data['title'],
            content=data['content'],
            author=data.get('author', 'Эксперт'),
            date=data.get('date'),
            pros=data.get('pros'),
            cons=data.get('cons')
        )


