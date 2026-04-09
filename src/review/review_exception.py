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
        """
        self.field_name = field_name
        super().__init__(f"Поле {self.field_name} не может быть пустым!")


class ReviewTextTooLongError(ReviewError):
    """
        Возникает, когда текст в поле обзора превышает максимально допустимую длину.

        Используется для полей с ограничениями по длине (например, pros/cons — не более 200 символов).

        :param field_name: Имя поля с превышением длины.
        :param cur_length: Текущая длина текста в символах.
        :param max_length: Максимально допустимая длина текста.
    """

    def __init__(self, field_name: str, cur_length: int, max_length: int):
        """
            Инициализирует исключение с информацией о превышении длины текста.

            :param field_name: имя поля, в котором превышена длина
            :param cur_length: фактическая длина текста
            :param max_length: максимально разрешённая длина текста
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
        :param cur_status: текущий (недопустимый) статус, переданный пользователем
    """
    def __init__(self, allowed: list[str], cur_status: str):
        """
            Инициализирует исключение с указанием допустимых и текущего статусов.

            :param allowed: список разрешённых статусов (например, ['PUBLISHED', 'DRAFT', 'ARCHIVED'])
            :param cur_status: статус, который вызвал ошибку
        """
        self.allowed = allowed
        self.cur_status = cur_status
        super().__init__(
            f"Недопустимый статус: {self.cur_status}."
            f"Допустимые статусы: {", ".join(self.allowed)}."
        )


class MissingRequiredFieldReviewError(ReviewError):
    """
        Возникает при отсутствии обязательного поля при создании или обработке обзора.
        Используется, например, при парсинге данных из словаря, когда не хватает ключевых полей.

        :param field_name: имя отсутствующего обязательного поля
    """
    def __init__(self, field_name: str):
        """
            Инициализирует исключение с указанием отсутствующего поля.

            :param field_name: имя обязательного поля, которое не найдено
        """
        self.field_name = field_name
        super().__init__(
            f"Отсутствует обязательное поле: {self.field_name}."
        )

