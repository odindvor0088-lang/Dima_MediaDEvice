from abc import ABC, abstractmethod
from datetime import datetime

from Project_Classes.review import Review

class Device(ABC):
    """Класс для создания устройства"""

    MIN_VOLUME = 0
    MAX_VOLUME = 100
    BATTERY_WARNING_LEVEL = 20
    ALLOWED_CATEGORIES = ["Смартфоны", "Наушники", "Ноутбуки", "Планшеты", "Умные часы"]

    def __init__(self, brand: str, model: str, category: str,  year: int = None,  image: str = None) -> None:
        """
        Инициализация объекта Device

         brand: Брэнд устройства
         model: Модель устройства
         category: Категория устройства
         year: Год выпуска устройства
         image: Разрешение устройстваЫ
        """
        self._brand = brand
        self._model = model
        self.category = category    # присваиваем через свойство
        self.year = year            # присваиваем через свойство
        self._image = None          # присваиваем через свойство
        self._specs = {}
        self._review = None

    @property
    def category(self) -> str:
        """Возвращает текущую категорию."""
        return self._category

    @category.setter
    def category(self, category: str) -> None:
        """
        Принимает новую категорию и обрабатывает её.
        :param category: Новая категория.
        :return: None.
        """
        if category.upper() in self.ALLOWED_CATEGORIES:
            self._category = category
        else:
            print(f'Категории: {category}. Нет в списке! ')

    @property
    def year(self) -> int:
        """Возвращает текущий год модели."""
        return self._year

    @year.setter
    def year(self, year: int) -> None:
        """
        Принимает новый год модели и обрабатывает её.
        :param year: Новое значение годы.
        :return: None.
        """
        if year is None:
            self._year = None
        elif not isinstance(year, int):
            print(f'Год модели {self.model} должен состоять из чисел!')
        elif year < 1990:
            print(f'Год модели {self.model} не может быть раньше 1990!')
        elif year > datetime.now().year:
            print(f'Год модели {self.model} не может быть позже {datetime.now().year}!')
        else:
            self._year = year


    @property
    def image(self) -> str:
        """Возвращает текущий экран модели."""
        return self._image

    @image.setter
    def image(self, image: str) -> None:
        """
        Принимает новый экран модели и обрабатывает её.
        :param image: Новое значение изображения.
        :return: None.
        """
        self._image = image

    @abstractmethod
    def get_device_type(self) -> str:
        """Возвращает текущую категория устройства."""
        pass

    @abstractmethod
    def get_short_description(self) -> str:
        """Возвращает краткое описание устройства (для превью на сайте)."""
        pass

    @property
    def specs(self) -> dict:
        """Возвращает текущие характеристики."""
        return self._specs.copy()

    @property
    def review(self):
        """Возвращает текущий обзор."""
        return self._review

    @review.setter
    def review(self, review: Review) -> None:
        """
            Принимает новое ревью модели и обрабатывает её.
            :param review: Новое значение ревью.
            :return: None.
        """
        if not isinstance(review, Review):
            print(f'должен быть review!')
        else:
            self._review = review

    def add_spec(self, key: str, value: str | int | float) -> None:
        """
            Добавляет и обновляет характеристики в словаре spec.
            Если ключ уже существует, то значение перезаписывается
            :param key: Имя ключа.
            :param value: Значение ключа.
            :return: None.
        """
        self._specs[key] = value

    def remove_spec(self, key: str) -> None:
        """
            Удаляет характеристику по ключу из spec
            :param key: Имя ключа.
            :return: None.
        """
        if key in self._specs:
            del self._specs[key]
        else:
            print(f'ключ не найден!')
            

# Создаем устройство
phone = Device("Apple", "iPhone 13", "Смартфоны", 2021, "iphone.jpg")

# Тест 1: Категория
phone.category = "Смартфоны"
phone.category = "Телефоны"

# Тест 2: Год
phone.year = 1990
phone.year = 1989
phone.year = 2027
phone.year = None

# Тест 3: Заряд батареи
phone.battery_level = 20
phone.battery_level = 19
phone.battery_level = -1
phone.battery_level = 101

# Тест 4: Громкость
phone.current_volume = 0
phone.current_volume = 100
phone.current_volume = -1
phone.current_volume = 101

# Тест 5: Состояние
phone.is_on = True
phone.is_on = True
phone.is_on = False
phone.is_on = False




