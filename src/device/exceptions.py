class DeviceError(Exception):
    """Базовое исключение для всех ошибок связанных с классов Device."""


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
            f"Недопустимый ключ: {self.key}." f"Допустимые ключи: {self.spec}"
        )


class InvalidKey(Exception):
    """
    Возникает при попытке ввести неверный ключ.

    :param key: Неверный ключ.
    :param list: Список ключей.
    """

    def __int__(self, key: str, list: list):
        """
        Инициализирует исключение с указанием неверного ключа.

        :param key: Неверный ключ.
        :param list: Список ключей.
        """

        self.key = key
        self.list = list

        super().__init__(
            f"Недопустимый ключ: {self.key}." f"Допустимые ключи: {self.list}"
        )
