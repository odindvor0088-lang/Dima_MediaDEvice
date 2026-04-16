class DeviceError(Exception):
    """Базовое исключение для всех ошибок связанных с классов Device."""

class NotCategoryInList(DeviceError):
    """
    Возникает при попытке установить неверную категорию.
    
    :param category: Неверное значение категории.
    """
    def __init__(self, category: str, allow_list: list[str]):
        """
        Инициализирует исключение с указанием неверной категории.

        :param category: Неверное значение категории.
        """
        self.category = category
        self.allow_list = allow_list

        super().__init__(
            f"Недопустимый статус: {self.category}."
            f"Допустимые статусы: {", ".join(self.allow_list)}."
        )

class FalseYear(Exception):
    """
    Возникает при попытке установить неверную категорию.

    :param year: Неверное значение даты.
    :param min_year: Минимальное значение года.
    :param year_now: Текущая дата.
    """
    def __init__(self, year: int, min_year: int, year_now: int):
        """
        Инициализирует исключение с указанием неверной даты.

        :param year: Неверное значение даты.
        :param min_year: Минимальное значение года.
        :param year_now: Текущая дата.
        """
        self.year = year
        self.min_year = min_year
        self.year_now = year_now

        super().__init__(
            f"Недопустимая дата: {self.year}."
            f"Год должен быть в диапазоне между {self.min_year} и {self.year_now}"
        )

class NotReviewInClassReview(Exception):
    """
    Возникает при попытке установить новое ревью которого нет в кдассе Review.

    :param review: Неверное ревью.
    """
    def __int__(self, review):
        """
        Инициализирует исключение с указанием неверного ревью.

        :param review: Неверное ревью.
        """
        self.review = review

        super().__init__(
            f"Недопустимое ревью(должен быть экземпляром класса Review): {self.review}."
        )

class NotKeyInSpec(Exception):
    """
       Возникает при попытке удалить характеристику по неверному ключу.

       :param key: Неверный ключ.
       :param spec: Словарь характеристик.
       """

    def __int__(self, key: str, spec: dict):
        """
        Инициализирует исключение с указанием неверного ключа.

        :param key: Неверный ключ.
        :param spec: Словарь характеристик.
        """

        self.key = key
        self.spec = spec

        super().__init__(
            f"Недопустимый ключ: {self.key}."
            f"Допустимые ключи: {self.spec}"
        )