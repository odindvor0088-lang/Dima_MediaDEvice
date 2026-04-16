from abc import ABC, abstractmethod
from datetime import datetime

from src.review.review import Review
from src.device.allowed_categories import AllowedCategories
from src.device.device_expection import * # TODO: ИСПРАВИТЬ НА ПРЯМОЙ ИМПОРТ

class Device(ABC):
    """Класс для создания устройства"""
    def __init__(self,
                 brand: str,
                 model: str,
                 category: AllowedCategories,
                 year: int = None,
                 image: str = None,
                 specs: dict = None,
                 review: Review = None) -> None:
        """
        Инициализирует объект Device.

        :param brand: Бренд устройства.
        :param model: Модель устройства.
        :param category: Категория устройства.
        :param year: Год выпуска устройства; если None — устанавливается текущий год.
        :param image: Путь или ссылка на изображение устройства; если None — используется значение по умолчанию.
        :param specs: Словарь с техническими характеристиками.
        :param review: Объект отзыва на устройство.
        """
        self.brand = brand
        self.model = model
        self.category = category     # присваиваем через свойство
        self.year = year             # присваиваем через свойство
        self.image = image           # присваиваем через свойство
        self.specs = specs           # присваиваем через свойство
        self.review = review         # присваиваем через свойство

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Device для отладки.

        :return: Строковое представление экземпляра класса.
        """
        return (f"Device(brand = {self.brand!r}, model = {self.model!r}, category = {self.category!r},"
                f" year = {self.year}, image = {self.image}, specs = {self.specs}, review = {self.review} )")

    def __str__(self) -> str:
        """
        Возвращает пользовательское строковое представление объекта Device.

        :return: Описание устройства для пользователя.
        """
        return (f"Создано устройство: (brand = {self.brand!r}, model = {self.model!r}, category = {self.category!r},"
                f" year = {self.year}, image = {self.image}, specs = {self.specs}, review = {self.review} )")


    @property
    def category(self) -> AllowedCategories:
        """
        Возвращает текущую категорию устройства.

        :return: Категория устройства в формате с заглавной буквы.
        """
        return self._category

    @category.setter
    def category(self, category: str) -> None:
        """
        Устанавливает новую категорию устройства.

        Проверяет, что категория есть в списке разрешённых (ALLOWED_CATEGORIES).
        Если категория не найдена, выводится сообщение об ошибке.

        :param category: Новая категория устройства.
        :raises NotCategoryInList: Возникает если категория не разрешена.
        """
        if category.title() in self.ALLOWED_CATEGORIES:
            self._category = category.title()
        else:
            raise NotCategoryInList(category)

    @property
    def year(self) -> int:
        """
        Возвращает год выпуска устройства.

        :return: Год выпуска.
        """
        return self._year

    @year.setter
    def year(self, year: int | None) -> None:
        """
        Принимает новый год модели и обрабатывает её.
        Если передано None, устанавливается текущий год.
        :param year: Новое значение годы.
        :raises FalseYear: Возникает если введена некорректная дата.
        """
        if year is None:
            self._year = datetime.now().year

        if not isinstance(year, (int, type(None))):
            raise ValueError('year должен быть int(None)')

        if year < 1900 or year > datetime.now().year:
            raise FalseYear(year, 1900, datetime.now().year)
        else:
            self._year = year


    @property
    def image(self) -> str | None:
        """
        Возвращает путь/ссылку на изображение устройства.

        :return: Путь или ссылка на изображение.
        """
        return self._image

    @image.setter
    def image(self, new_image: str) -> str | None:
        """
        Принимает новый экран модели и обрабатывает её.
        Если передано None, то будет установлена картинка по умолчанию.
        :param new_image: Новое значение изображения.
        :raises ValueError: Если new_image не str.
        """
        if new_image is None:
            self._image = '/'

        if not isinstance(new_image, (str, type(None))):
            raise ValueError('new_image должен быть str')
        else:
            self._image = new_image



    @property
    def specs(self) -> dict:
        """
        Возвращает копию словаря с техническими характеристиками.

        :return: Копия словаря specs.
        """
        return self._specs.copy()

    @specs.setter
    def specs(self, new_specs: dict) -> None:
        """
            Принимает словарь и обрабатывает его.
            :param new_specs: Новое значение словаря.
            :raises ValueError: Если new_specs не словарь.
        """
        if new_specs is None:
            self._specs = {}

        if not isinstance(new_specs, dict):
            raise ValueError('new_specs должен быть словарём!')
        else:
            self._specs = new_specs.copy()

    @property
    def review(self) -> Review | None:
        """
        Возвращает объект отзыва на устройство.

        :return: Объект Review или None.
        """
        return self._review

    @review.setter
    def review(self, review: Review | None) -> None:
        """
            Принимает новое ревью модели и обрабатывает её.
            :param review: Новое значение ревью.
            :raises NotReviewInClassReview: Если review не экземпляр класса Review.
        """
        if not isinstance(review, (Review, type(None))):
           raise NotReviewInClassReview(review)
        else:
            self._review = review

    @abstractmethod
    def get_device_type(self) -> str:
        """
        Абстрактный метод. Возвращает тип устройства.

        Должен быть реализован в дочерних классах.

        :return: Тип устройства.
        """
        pass

    @abstractmethod
    def get_short_description(self) -> str:
        """Абстрактный метод. Возвращает краткое описание устройства для превью на сайте."""
        pass


    def add_spec(self, key: str, value: str | int | float) -> None:
        """
            Добавляет и обновляет характеристики в словаре spec.
            Если ключ уже существует, то значение перезаписывается
            :param key: Имя ключа.
            :param value: Значение ключа.
        """
        self.specs[key] = value

    def remove_spec(self, key: str) -> None:
        """
            Удаляет характеристику по ключу из spec
            :param key: Имя ключа.
            :raises NotKeyInSpec: Если key это несуществующий ключ.
        """
        if key in self.specs:
            del self.specs[key]
        else:
            raise NotKeyInSpec(key, self.specs)

    @classmethod
    def from_dict(cls, data: dict) -> Device | None:
        """
        Метод обрабатывает словарь с характеристиками
        Если в словаре недопустимый ключ, то код выдаст ошибку

        :param data: СЛОВАРЬ С ХАРАКТЕРИСТИКАМИ МОДЕЛИ.
        """
        true_keys = ['brand', 'model', 'category']
        for key in true_keys:
            if key not in data:
                print(f"неверный ключ '{key}'")
                return None

        if 'review' in data:
            review = Review.from_dict(data['review'])
        else:
            review = None

        return cls(
            brand=data['brand'],
            model=data['model'],
            category=data['category'],
            year=data.get('year'),
            image=data.get('image'),
            specs=data.get('specs'),
            review=review
        )