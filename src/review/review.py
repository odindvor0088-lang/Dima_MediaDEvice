from datetime import datetime

from src.review.status_review import ReviewStatus
from src.review.review_exception import *


class Review:
    """Класс для представления обзора"""
    def __init__(self,
                 title: str,
                 content: str,
                 author: str = "Эксперт",
                 status: ReviewStatus = ReviewStatus.PUBLISHED,
                 date: datetime = None,
                 pros: list[str] = None,
                 cons: list[str] = None) -> None:
        """
        Инициализация объекта Review.

        :param title: заголовок обзора
        :param content: текст обзора
        :param author: автор обзора; по умолчанию — «Эксперт»
        :param status: статус обзора; по умолчанию — ReviewStatus.PUBLISHED
        :type status: ReviewStatus
        :param date: дата создания обзора; если None — устанавливается текущая дата и время
        :param pros: список плюсов устройства; если None — инициализируется пустым списком
        :param cons: список минусов устройства; если None — инициализируется пустым списком
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

        :return: Строковое представление экземпляра класса.
        """
        return (f"Review(title = {self.title!r}, content = {self.content!r}, author = {self.author!r},"
                f" date = {self.date}, pros = {self.pros}, cons = {self.cons} )")

    def __str__(self) -> str:
        """
        Возвращает пользовательское строковое представление объекта Review.

        :return: Описание обзора для пользователя.
        """
        return (f"Создано ревью состоящее из: (title = {self.title}, content = {self.content}, author = {self.author},"
                f" date = {self.date}, pros = {self.pros}, cons = {self.cons} )")

    @property
    def title(self) -> str:
        """
        Возвращает текущий заголовок обзора.

        :return: Заголовок обзора.
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

        :return: Текст обзора.
        """
        return self.__content

    @content.setter
    def content(self, value: str) -> None:
        """
        Устанавливает новый текст обзора.

        :param value: Новый текст обзора.
        :raises ValueError: Если value не является строкой.
        """
        if isinstance(value, str):
            self.__content = value
        else:
            raise ValueError(f'value должен быть str!')

    @property
    def author(self) -> str:
        """
        Возвращает имя автора обзора.

        :return: Имя автора.
        """
        return self.__author

    @author.setter
    def author(self, value: str) -> None:
        """
        Устанавливает имя автора обзора.

        :param value: Новое имя автора.
        :raises ValueError: Если value не является строкой.
        """
        if isinstance(value, str):
            self.__author = value
        else:
            raise TypeError(f'value должен быть str!')

    @property
    def date(self) -> datetime:
        """
        Возвращает дату создания обзора.

        :return: Дата и время создания обзора.
        """
        return self.__date

    @date.setter
    def date(self, new_date: datetime | None) -> None:
        """
        Устанавливает дату создания обзора.
        Если передано None, устанавливается текущая дата и время.

        :param new_date: Новая дата создания обзора.
        :raises ValueError: Если new_date не является экземпляром datetime.
        """
        if new_date is None:
            self.__date = datetime.now()
        elif isinstance(new_date, datetime):
            self.__date = new_date
        else:
            raise ValueError('new_date должна быть экземпляром класса datetime!')


    @property
    def pros(self) -> list[str]:
        """
        Возвращает копию списка плюсов обзора.

        :return: Копия списка плюсов.
        """
        return self.__pros.copy()

    @pros.setter
    def pros(self, list_pros: list[str] | None) -> None:
        """
        Устанавливает новый список плюсов обзора.
        Если передан None, инициализируется пустой список.
        Сохраняется копия списка для инкапсуляции.

        :param list_pros: новый список плюсов
        :raises ValueError: если list_pros не является списком
        """
        if list_pros is None:
            self.__pros = []
        elif isinstance(list_pros, list):
            self.__pros = list_pros.copy()
        else:
            raise ValueError('list_pros не является списком!')


    @property
    def cons(self) -> list:
        """
        Возвращает копию списка минусов обзора.

        :return: Копия списка минусов.
        """
        return self.__cons.copy()

    @cons.setter
    def cons(self, list_cons: list) -> None:
        """
        Устанавливает новый список минусов обзора.
        Если передан None, инициализируется пустой список.
        Сохраняется копия списка для инкапсуляции.

        :param list_cons: Новый список минусов.
        :raises ValueError: Если list_cons не является списком.
        """
        if list_cons is None:
            self.__cons = []
        elif isinstance(list_cons, list):
            self.__cons = list_cons.copy()
        else:
            raise ValueError('list_cons не является списком!')

    @property
    def status(self) -> ReviewStatus:
        """
        Возвращает статус обзора.

        :return: Статус обзора.
        """
        return self.__status

    @status.setter
    def status(self, new_status: ReviewStatus | str) -> None:
        """
        Устанавливает новый статус обзора.

        :param new_status: Новый статус обзора.
        :raises InvalidReviewStatusError: Если new_status не является
                допустимым статусом из ReviewStatus.
        """
        if new_status in ReviewStatus:
            self.__status = new_status    # TODO: ОШИБКА РАЗОБРАТЬ НА ЗАНЯТИИ
        else:
            raise InvalidReviewStatusError(ReviewStatus.to_list(), new_status)

    def add_pro(self, pro_text: str, max_length: int = 200) -> None:
        """
        Добавляет новый плюс в список.
        :param pro_text: Текст плюса.
        :param max_length: Максимальная длина поля.
        """
        self._validate_text(pro_text, "pro_text", max_length)
        self.__pros.append(pro_text)


    def add_con(self, con_text: str, max_length: int = 200) -> None:
        """
        Добавляет новый минус в список.
        :param con_text: Текст минуса.
        :param max_length: Максимальная длина поля.
        """
        self._validate_text(con_text, "con_text", max_length)
        self.__pros.append(con_text)

    def remove_pro(self, index: int) -> None:
        """
        Удаляет плюс по индексу.
        :param index: индекс плюса
         """
        try:
            del self.pros[index]
        except IndexError as ex:
            raise IndexError(f"Индекс {index} выходит за переделы списка. "
                             f"Размер: {len(self.pros)}.") from ex

    def remove_con(self, index: int) -> None:
        """
        Удаляет минус по индексу.
        :param index: индекс минуса
        """
        try:
            del self.cons[index]
        except IndexError as ex:
            raise IndexError(f"Индекс {index} выходит за переделы списка. "
                             f"Размер: {len(self.cons)}.") from ex

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
                raise MissingRequiredFieldReviewError(key)

        return cls(
            title=data['title'],
            content=data['content'],
            author=data.get('author', 'Эксперт'),
            date=data.get('date'),
            pros=data.get('pros'),
            cons=data.get('cons')
        )

    @staticmethod
    def _validate_text(text: str, field_name: str, max_length: int):
        # TODO: РАСПИСАТЬ ДОКУМЕНТАЦИЮ!
        if not isinstance(text, str):
            raise ValueError(f'{field_name.capitalize()} должен быть str, получен '
                             f'{type(text).__name__}!')

        if not text.strip():
            raise EmptyReviewFieldError(field_name)

        if len(text) > max_length:
            raise ReviewTextTooLongError(field_name, len(text), max_length)
