class ReviewError(Exception):
    """Базовое исключение для всех ошибок связанных с классов Review."""
    ...


class EmptyReviewFieldError(ReviewError):
    """
    Возникает при попытке установить пустое значение в обязательное поле.

    :param field_name: Имя поля, которое не может быть пустым.
    """

    def __init__(self, field_name: str):
        self.field_name = field_name
        super().__init__(f"Поле {self.field_name} не может быть пустым!")


class ReviewTextTooLongError(ReviewError):

    def __init__(self, field_name: str, cur_length: int, max_length: int = 200):
        self.field_name = field_name
        self.cur_length = cur_length
        self.max_length = max_length
        super().__init__(
            f"Поле {self.field_name} превышает {self.max_length}, сейчас символов:"
            f" {self.cur_length}!"
        )


class InvalidReviewStatusError(ReviewError):
    def __init__(self, allowed: list[str], cur_status: str):
        self.allowed = allowed
        self.cur_status = cur_status
        super().__init__(
            f"Недопустимый статус: {self.cur_status}. Допустимые значения "
            f"{", ".join(allowed)}."
        )


class MissingRequiredFieldReviewError(ReviewError):
    def __init__(self, field_name: str):
        self.field_name = field_name
        super().__init__(
            f"Отсутствует обязательное поле: {self.field_name}."
        )

