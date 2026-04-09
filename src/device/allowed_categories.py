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