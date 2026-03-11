from abc import ABC, abstractmethod
from datetime import datetime

from Project_Classes.review import Review

class Device(ABC):
    """Класс для создания устройства"""
    ALLOWED_CATEGORIES = ["Смартфоны", "Наушники", "Ноутбуки", "Планшеты", "Умные часы"]

    def __init__(self, brand: str, model: str, category: str,  year: int = None,  image: str = None, specs: dict = None, review: Review = None) -> None:
        """
        Инициализация объекта Device

         brand: Брэнд устройства
         model: Модель устройства
         category: Категория устройства
         year: Год выпуска устройства
         image: Разрешение устройстваЫ
        """
        self.brand = brand
        self.model = model
        self.category = category    # присваиваем через свойство
        self.year = year            # присваиваем через свойство
        self.image = None          # присваиваем через свойство
        self.specs = specs
        self.review = None

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
        if category.title() in self.ALLOWED_CATEGORIES:
            self._category = category.title()
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
            self._year = datetime.now().year
        elif not isinstance(year, (int, type(None))):
            print(f'Год модели {self.model} должен состоять из чисел и не быть None!')
        elif year < 1900 or year > datetime.now().year:
            print(f'Недопустимое значение года модели!')
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
        return self._specs

    @specs.setter
    def specs(self, specs: dict) -> None:
        """
            Принимает новое ревью модели и обрабатывает её.
            :param review: Новое значение ревью.
            :return: None.
        """
        self._specs = specs

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

    @property
    def specs(self):
        """<UNK> <UNK> <UNK>."""
        return self._specs


    def add_spec(self, key: str, value: str | int | float) -> None:
        """
            Добавляет и обновляет характеристики в словаре spec.
            Если ключ уже существует, то значение перезаписывается
            :param key: Имя ключа.
            :param value: Значение ключа.
            :return: None.
        """
        self.specs[key] = value

    def remove_spec(self, key: str) -> None:
        """
            Удаляет характеристику по ключу из spec
            :param key: Имя ключа.
            :return: None.
        """
        if key in self.specs:
            del self.specs[key]
        else:
            print(f'ключ не найден!')







