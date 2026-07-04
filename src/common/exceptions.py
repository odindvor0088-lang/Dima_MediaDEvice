class AppError(Exception):
    """Базовое исключение для ожидаемых ошибок приложения."""


class ValidationError(AppError):
    """Базовое исключение для ошибок валидации данных."""


class EmptyFieldError(ValidationError):
    """Поле не может быть пустым."""

    def __init__(self, field_name: str,  entity: str):
        """
        Инициализирует исключение с указанием имени проблемного поля.

        :param field_name: Имя поля, вызвавшего ошибку
        :param entity: Имя сущности (класса), к которой относится поле.
        """
        self.field_name = field_name
        self.entity = entity
        super().__init__(f"Поле '{self.entity}.{self.field_name}' не может быть пустым!")


class TextTooLongError(ValidationError):
    """Текстовое поле превышает допустимую длину."""

    def __init__(self, field_name: str, cur_length: int, max_length: int, entity: str):
        """
        Инициализирует исключение с информацией о превышении длины текста.

        :param field_name: Имя поля, в котором превышена длина.
        :param cur_length: Фактическая длина текста.
        :param max_length: Максимально разрешённая длина текста.
        :param entity: Имя сущности (класса), к которой относится поле.
        """
        self.field_name = field_name
        self.cur_length = cur_length
        self.max_length = max_length
        self.entity = entity
        super().__init__(
            f"Поле {self.entity}.{self.field_name} превышает {self.max_length}, сейчас символов:"
            f" {self.cur_length}!"
        )


class MissingRequiredFieldError(ValidationError):
    """В словаре отсутствует обязательное поле."""

    def __init__(self, field_name: str, entity: str):
        """
        Инициализирует исключение с указанием отсутствующего поля.

        :param field_name: Имя обязательного поля, которое не найдено.
        :param entity: Имя сущности (класса), к которой относится поле.
        """
        self.field_name = field_name
        self.entity = entity
        super().__init__(f"Отсутствует обязательное поле: {self.entity}.{self.field_name}.")


class InvalidChoiceError(ValidationError):
    """Значение не входит в список допустимых значений."""

    def __init__(self, field_name: str, entity: str, allowed: list[str], cur_status: str):
        """
        Инициализирует исключение с указанием допустимых и текущего статусов.

        :param field_name: Имя поля, в котором ошибка.
        :param entity: Имя сущности (класса), к которой относится поле.
        :param allowed: Список разрешённых статусов (например, ['PUBLISHED', 'DRAFT', 'ARCHIVED'])
        :param cur_status: статус, который вызвал ошибку
        """
        self.field_name = field_name
        self.entity = entity
        self.allowed = allowed
        self.cur_status = cur_status
        super().__init__(
            f"Ошибка в поле: {self.entity}.{self.field_name} "
            f"Недопустимый статус: {self.cur_status}."
            f"Допустимые статусы: {", ".join(self.allowed)}."
        )


class YearOutOfRangeError(ValidationError):
    """Год выходит за допустимый диапазон."""

    def __init__(self, field_name: str, entity: str, year: int, min_year: int, year_now: int):
        """
        Инициализирует исключение с указанием неверной даты.

        :param field_name: Имя поля, в котором ошибка.
        :param entity: Имя сущности (класса), к которой относится поле.
        :param year: Неверное значение даты.
        :param min_year: Минимальное значение года.
        :param year_now: Текущая дата.
        """
        self.field_name = field_name
        self.entity = entity
        self.year = year
        self.min_year = min_year
        self.year_now = year_now

        super().__init__(
            f"Ошибка в поле: {self.entity}.{self.field_name} "
            f"Недопустимая дата: {self.year}."
            f"Год должен быть в диапазоне между {self.min_year} и {self.year_now}"
        )