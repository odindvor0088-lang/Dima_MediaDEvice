from enum import StrEnum


class AllowedCategories(StrEnum):
    """
    Перечисление разрешённых категорий устройств.

    Используется для валидации категории при создании экземпляра класса Device.
    Каждая категория представлена в виде строки в верхнем регистре.
    """

    SMARTPHONE = "SMARTPHONE"
    HEADPHONE = "HEADPHONE"
    LAPTOP = "LAPTOP"
    TABLET = "TABLET"
    SMARTWATCH = "SMARTWATCH"

    @classmethod
    def to_list(cls) -> list[str]:
        """ """
        return [str(i) for i in cls]
