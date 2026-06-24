from src.common.exceptions import *
from src.device.exceptions import *



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

    :raises TextTooLongError: Если текстовое поле превышает допустимую длину.
    """
    if len(value) > max_length:
        raise TextTooLongError(
            f"Поле '{field_name}.{entity}' не должно превышать {max_length} символов, "
            f"сейчас в вашем поле {len(value)} символов"
        )

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
    if year < min_year or year > max_year:
        raise YearOutOfRangeError(
            f"Поле '{field_name}.{entity}' не должно превышать {max_year} и быть меньше {min_year}, "
            f"вы ввели значение {year}"
        )

    return year


def validate_required_fields(
    data: dict,
    required_fields: list[str],
    entity: str,
) -> None:
    """
    Проверяет обязательные ключи в словаре.

    :param data: Словарь с нужными нам ключами.
    :param required_fields: Обязательные поля.
    :param entity:  Имя сущности (класса), к которому относится поле.

    :return: Исходный словарь.
    """
    for field in required_fields:
        if field not in data:
            raise InvalidKey(
                f"Отсутствует обязательное поле '{field}'. "
                f"Обязательные поля: {required_fields}"
            )


def validate_choice(
    value,
    enum_class,
    field_name: str,
    entity: str,
):
    """
    Проверка значения по Enum / StrEnum

    :param value: Проверяемое значение.
    :param enum_class:
    :param field_name:
    :param entity:
    :return:
    """