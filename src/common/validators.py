from src.common.exceptions import (
    EmptyFieldError,
    InvalidChoiceError,
    MissingRequiredFieldError,
    TextTooLongError,
    YearOutOfRangeError,
)
from typing import TypeVar
from enum import Enum



def validate_non_empty_string(value: str, field_name: str, entity: str) -> str:
    """
    Проверяет, что переданное значение является непустой строкой.

    :param value: Проверяемое значение.
    :param field_name: Имя поля (для сообщения об ошибке).
    :param entity: Имя сущности (класса), к которому относится поле.

    :return: Исходная строка (С автоматической обрезкой пробелов).

    :raises TypeError: Если value не является строкой.
    :raises EmptyFieldError: Если строка пустая или состоит только из пробелов.
    """

    if not isinstance(value, str):
        raise TypeError(
            f"Поле '{field_name}.{entity}' должно быть str, получен {type(value).__name__}"
        )

    normalized = value.strip()
    if not normalized:
        raise EmptyFieldError(field_name, entity)

    return normalized


def validate_string_length(
    value: str,
    field_name: str,
    entity: str,
    max_length: int,
) -> str:
    """
    Проверяет, что переданное значение не выходит за пределы максимальной длинны.

    :param value: Проверяемое значение.
    :param field_name: Имя поля (для сообщения об ошибке).
    :param entity: Имя сущности (класса), к которому относится поле.
    :param max_length: Максимальная длинна строки.

    :return: Исходная строка.

    :raises TypeError: Если value не является строкой.
    :raises TextTooLongError: Если текстовое поле превышает допустимую длину.
    """
    normalized = validate_non_empty_string(value, field_name, entity)
    if len(normalized) > max_length:
        raise TextTooLongError(field_name, len(normalized), max_length, entity)

    return value


def validate_year_range(
    year: int,
    field_name: str,
    entity: str,
    min_year: int,
    max_year: int,
) -> int:
    """
    Проверяет, что переданное значение не выходит из допустимого диапазона года.

    :param year: Проверяемый год
    :param field_name: Имя поля (для сообщения об ошибке).
    :param entity: Имя сущности (класса), к которому относится поле.
    :param min_year: Минимально допустимый год.
    :param max_year: Максимально допустимый год.

    :return: Исходная строка.

    raises YearOutOfRangeError: Год выходит за допустимый диапазон..
    """
    if not isinstance(year, int):
        raise TypeError(f"Поле '{field_name}.{entity}' должно быть str, получен {type(year).__name__}")

    if year < min_year or year > max_year:
        raise YearOutOfRangeError(field_name, entity, year, min_year, max_year)

    return year


def validate_required_fields(
    field_name: str,
    data: dict,
    required_fields: list[str],
    entity: str,
) -> None:
    """
    Проверяет обязательные ключи в словаре.

    :param field_name: Имя поля.
    :param data: Словарь с нужными нам ключами.
    :param required_fields: Обязательные поля.
    :param entity:  Имя сущности (класса), к которому относится поле.

    :return: Исходный словарь.
    """
    if not isinstance(data, dict):
        raise TypeError(
            f"Параметр 'data' должен быть dict, получен {type(data).__name__}"
        )

    for field in required_fields:
        if field not in data:
            raise MissingRequiredFieldError(field_name, entity)


E = TypeVar("E", bound=Enum)

def validate_choice(
    value: object,
    enum_class: type[E],
    field_name: str,
    entity: str,
) -> E:
    """
        Проверка значения по Enum / StrEnum

        :param value: Проверяемое значение.
        :param enum_class: Класс Enum для проверки.
        :param field_name: Имя поля.
        :param entity: Имя сущности (класса), к которому относится поле.

        :return: Элемент Enum.

        :raises TypeError: Если enum_class не является Enum
        :raises ValueError: Если значение недопустимо для Enum
        """
    if not isinstance(enum_class, type) or not issubclass(enum_class, Enum):
        raise TypeError(
            f"Параметр 'enum_class' должен быть классом Enum, "
            f"получен {type(enum_class).name}"
        )

    try:
        value = enum_class(value)
    except InvalidChoiceError as e:
        allowed = ", ".join(m.value for m in enum_class)
        raise InvalidChoiceError(field_name, entity, value) from e
    else:
        return value