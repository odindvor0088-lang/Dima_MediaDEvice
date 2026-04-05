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

            title: Заголовок обзора
            content: Текст обзора
            author: Автор обзора (по умолчанию "Эксперт")
            status: ...
            date: Дата создания
            pros: Список плюсов
            cons: Список минусов
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
        """Строковое представление объекта Review."""
        return (f"Review(title = {self.title!r}, content = {self.content!r}, author = {self.author!r},"
                f" date = {self.date}, pros = {self.pros}, cons = {self.cons} )")

    def __str__(self) -> str:
        """Строковое представление объекта Review для пользователя."""
        return (f"Создано ревью состоящее из: (title = {self.title}, content = {self.content}, author = {self.author},"
                f" date = {self.date}, pros = {self.pros}, cons = {self.cons} )")

    @property
    def title(self) -> str:
        """Возвращает текущий заголовок обзора."""
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
        """Возвращает текст обзора."""
        return self.__content

    @content.setter
    def content(self, value: str) -> None:
        """
            Устанавливает новый текст обзора.
            value:
        """
        if isinstance(value, str):
            self.__content = value
            print(f'Текст вашего обзора(Проверьте, всё ли вы правильно указали.): {self.__content}')
        else:
            print(f'Обзор не может состоять только из чисел!')

    @property
    def author(self) -> str:
        """Возвращает имя автора обзора."""
        return self.__author

    @author.setter
    def author(self, value: str) -> None:
        """Устанавливает имя автора."""
        if isinstance(value, str):
            self.__author = value
        print(f'Другие пользователи будут видеть вас под ником: {self.__author}')

    @property
    def date(self) -> datetime:
        """Возвращает дату создания обзора."""
        return self.__date

    @date.setter
    def date(self, new_date: datetime) -> None:
        if new_date is None:
            self.__date = datetime.now()
        elif isinstance(new_date, datetime):
            self.__date = new_date
        else:
            print(f'new_date должна быть экземпляром класса datetime!')


    @property
    def pros(self) -> list[str]:
        """Возвращает КОПИЮ списка"""
        return self.__pros.copy()

    @pros.setter
    def pros(self, list_pros: list[str]) -> None:
        """Сохраняется копия списка для инкапсуляции."""
        if list_pros is None:
            self.__pros = []
        elif isinstance(list_pros, list):
            self.__pros = list_pros.copy()
        else:
            print(f'list_pros должен быть списком строк!')


    @property
    def cons(self) -> list:
        """Сохраняется копия списка для инкапсуляции."""
        return self.__cons.copy()

    @cons.setter
    def cons(self, list_cons: list) -> None:
        """Сохраняется копия списка для инкапсуляции."""
        if list_cons is None:
            self.__cons = []
        elif isinstance(list_cons, list):
            self.__cons = list_cons.copy()
        else:
            print(f'list_cons должен быть списком строк!')

    @property
    def status(self) -> ReviewStatus:
        """

        """
        return self.__status

    @status.setter
    def status(self, new_status: ReviewStatus | str) -> None:
        """

        """
        if new_status in ReviewStatus:
            self.__status = new_status
        else:
            print(f"new_status must be attribute in ReviewStatus!"
                  f"ReviewStatus: {", ".join(ReviewStatus)}")

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
        """Удаляет плюс по индексу."""
        if -len(self.__pros) <= index < len(self.__pros):
            removed = self.__pros.pop(index)
            print(f"Плюс '{removed}' удалён")
        else:
            print(f'Индекс {index} вне диапазона')

    def remove_con(self, index: int) -> None:
        """Удаляет минус по индексу."""
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


