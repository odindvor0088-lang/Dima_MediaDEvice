from enum import StrEnum


class ReviewStatus(StrEnum):
    """
    Перечисление статусов обзора.

    Определяет возможные статусы, в которых может находиться обзор.
    Используется для валидации и категоризации состояния обзоров в системе.
    Каждый статус представлен в виде строки в верхнем регистре.
    """

    PUBLISHED = "PUBLISHED"
    DRAFT = "DRAFT"
    ARCHIVED = "ARCHIVED"

    @classmethod
    def to_list(cls) -> list[str]:
        # TODO: РЕАЛИЗОВАТЬ ДОКУМЕНТАЦИЮ!!!
        return [str(i) for i in cls]
