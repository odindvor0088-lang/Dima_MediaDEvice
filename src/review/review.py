from datetime import datetime
from typing import Self

from src.review.status import ReviewStatus
from src.common.validators import (validate_non_empty_string, validate_string_length, validate_choice,
                                   validate_required_fields)


class Review:
    """Класс для представления обзора"""

    def __init__(
        self,
        title: str,
        content: str,
        author: str = "Эксперт",
        status: ReviewStatus = ReviewStatus.PUBLISHED,
        date: datetime | None = None,
        pros: list[str] | None = None,
        cons: list[str] | None = None,
    ) -> None:
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

    @property
    def title(self) -> str:
        """
        Возвращает текущий заголовок обзора.

        :return: Заголовок обзора.
        """
        return self.__title

    @title.setter
    def title(self, value: str) -> None:
        self.__title = validate_non_empty_string(
            value=value,
            field_name="title",
            entity="Review",
        )

    @property
    def content(self) -> str:
        """
        Возвращает текст обзора.

        :return: Текст обзора.
        """
        return self.__content

    @content.setter
    def content(self, value: str) -> None:
        self.__content = validate_string_length(
            value=value,
            field_name="content",
            entity="Review",
            max_length=500,
        )

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
        self.__author = validate_non_empty_string(
            value=value,
            field_name="author",
            entity="Review",
        )

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
        if not isinstance(new_date, (datetime, type(None))):
            raise ValueError("new_date должна быть экземпляром класса datetime!")

        if new_date is None:
            self.__date = datetime.now()
        else:
            self.__date = new_date

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
        if not isinstance(list_pros, (list, type(None))):
            raise ValueError("list_pros не является списком!")

        if list_pros is None:
            self.__pros = []
        elif all(isinstance(i, str) for i in list_pros):
            self.__pros = list_pros.copy()

    @property
    def cons(self) -> list:
        """
        Возвращает копию списка минусов обзора.

        :return: Копия списка минусов.
        """
        return self.__cons.copy()

    @cons.setter
    def cons(self, list_cons: list[str]) -> None:
        """
        Устанавливает новый список минусов обзора.
        Если передан None, инициализируется пустой список.
        Сохраняется копия списка для инкапсуляции.

        :param list_cons: Новый список минусов.
        :raises ValueError: Если list_cons не является списком.
        """
        if not isinstance(list_cons, (list, type(None))):
            raise ValueError("list_cons не является списком!")

        if list_cons is None:
            self.__cons = []
        elif all(isinstance(i, str) for i in list_cons):
            self.__cons = list_cons.copy()

    @property
    def status(self) -> ReviewStatus:
        """
        Возвращает статус обзора.

        :return: Статус обзора.
        """
        return self.__status

    @status.setter
    def status(self, new_status: ReviewStatus | str) -> None:
        self.__status = validate_choice(
            value=new_status,
            enum_class=ReviewStatus,
            field_name="status",
            entity="Review",
        )

    def add_pro(self, pro_text: str) -> None:
        checked_text = validate_string_length(
            value=pro_text,
            field_name="pros",
            entity="Review",
            max_length=200,
        )

        self.__pros.append(checked_text)

    def add_con(self, con_text: str, max_length: int = 200) -> None:
        checked_text = validate_string_length(
            value=con_text,
            field_name="cons",
            entity="Review",
            max_length=200,
        )
        self.__cons.append(checked_text)

    def remove_pro(self, index: int) -> None:
        """
        Удаляет плюс по индексу.
        :param index: индекс плюса
        """
        try:
            del self.__pros[index]
        except IndexError as ex:
            raise IndexError(
                f"Индекс {index} выходит за переделы списка. "
                f"Размер: {len(self.pros)}."
            ) from ex

    def remove_con(self, index: int) -> None:
        """
        Удаляет минус по индексу.
        :param index: индекс минуса
        """
        try:
            del self.__cons[index]
        except IndexError as ex:
            raise IndexError(
                f"Индекс {index} выходит за переделы списка. "
                f"Размер: {len(self.cons)}."
            ) from ex

    @classmethod
    def from_dict(cls, data: dict) -> Self | None:
        validate_required_fields(
        data=data,
        required_fields=["title", "content"],
        entity="Review",
        )


    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Review для отладки.

        :return: Строковое представление экземпляра класса.
        """
        return (
            f"Review(title = {self.title!r}, content = {self.content!r}, author = {self.author!r},"
            f" date = {self.date}, pros = {self.pros}, cons = {self.cons} )"
        )

    def __str__(self) -> str:
        """
        Возвращает пользовательское строковое представление объекта Review.

        :return: Описание обзора для пользователя.
        """
        return (
            f"Создано ревью состоящее из: (title = {self.title},"
            f" content = {self.content}, author = {self.author},"
            f" date = {self.date}, pros = {self.pros}, cons = {self.cons} )"
        )
