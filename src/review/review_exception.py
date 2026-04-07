class ReviewError(Exception):
    """Базовое исключение для всех ошибок связанных с классов Review."""
    ...


class EmptyReviewFieldError(ReviewError):
    """
    Возникает при попытке установить пустое значение в обязательное поле.

    :param field_name: Имя поля, которое не может быть пустым.
    """

    def __init__(self, field_name: str):
        """
            Инициализирует исключение с указанием имени проблемного поля.

            :param field_name: имя поля, вызвавшего ошибку
            :type field_name: str
        """
        self.field_name = field_name
        super().__init__(f"Поле {self.field_name} не может быть пустым!")


class ReviewTextTooLongError(ReviewError):
    """
        Возникает, когда текст в поле обзора превышает максимально допустимую длину.

        Используется для полей с ограничениями по длине (например, pros/cons — не более 200 символов).

        :param field_name: имя поля с превышением длины
        :type field_name: str
        :param cur_length: текущая длина текста в символах
        :type cur_length: int
        :param max_length: максимально допустимая длина текста (по умолчанию — 200)
        :type max_length: int
    """

    def __init__(self, field_name: str, cur_length: int, max_length: int = 200):
        """
            Инициализирует исключение с информацией о превышении длины текста.

            :param field_name: имя поля, в котором превышена длина
            :type field_name: str
            :param cur_length: фактическая длина текста
            :type cur_length: int
            :param max_length: максимально разрешённая длина текста
            :type max_length: int
        """
        self.field_name = field_name
        self.cur_length = cur_length
        self.max_length = max_length
        super().__init__(
            f"Поле {self.field_name} превышает {self.max_length}, сейчас символов:"
            f" {self.cur_length}!"
        )


class InvalidReviewStatusError(ReviewError):
    """
        Возникает при попытке установить недопустимый статус обзора.

        Проверяет соответствие переданного статуса допустимым значениям из перечисления ReviewStatus.

        :param allowed: список допустимых статусов
        :type allowed: list[str]
        :param cur_status: текущий (недопустимый) статус, переданный пользователем
        :type cur_status: str
    """
    def __init__(self, allowed: list[str], cur_status: str):
        """
            Инициализирует исключение с указанием допустимых и текущего статусов.

            :param allowed: список разрешённых статусов (например, ['PUBLISHED', 'DRAFT', 'ARCHIVED'])
            :type allowed: list[str]
            :param cur_status: статус, который вызвал ошибку
            :type cur_status: str
        """
        self.allowed = allowed
        self.cur_status = cur_status
        super().__init__(
            f"Недопустимый статус: {self.cur_status}."

        )


class MissingRequiredFieldReviewError(ReviewError):
    """
        Возникает при отсутствии обязательного поля при создании или обработке обзора.

        Используется, например, при парсинге данных из словаря, когда не хватает ключевых полей.

        :param field_name: имя отсутствующего обязательного поля
        :type field_name: str
    """
    def __init__(self, field_name: str):
        """
            Инициализирует исключение с указанием отсутствующего поля.

            :param field_name: имя обязательного поля, которое не найдено
            :type field_name: str
        """
        self.field_name = field_name
        super().__init__(
            f"Отсутствует обязательное поле: {self.field_name}."
        )

