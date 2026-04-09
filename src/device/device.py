from abc import ABC, abstractmethod
from datetime import datetime

from src.review.review import Review
from src.device.allowed_categories import AllowedCategories

class Device(ABC):
    """Класс для создания устройства"""
    def __init__(self,
                 brand: str,
                 model: str,
                 category: str,
                 year: int = None,
                 image: str = None,
                 specs: dict = None,
                 review: Review = None) -> None:
        """
        Инициализирует объект Device.

        :param brand: бренд устройства
        :type brand: str
        :param model: модель устройства
        :type model: str
        :param category: категория устройства
        :type category: str
        :param year: год выпуска устройства; если None — устанавливается текущий год
        :type year: int | None
        :param image: путь или ссылка на изображение устройства; если None — используется значение по умолчанию
        :type image: str | None
        :param specs: словарь с техническими характеристиками
        :type specs: dict | None
        :param review: объект отзыва на устройство
        :type review: Review | None
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

        :return: строковое представление экземпляра класса
        :rtype: str
        """
        return (f"Device(brand = {self.brand!r}, model = {self.model!r}, category = {self.category!r},"
                f" year = {self.year}, image = {self.image}, specs = {self.specs}, review = {self.review} )")

    def __str__(self) -> str:
        """
        Возвращает пользовательское строковое представление объекта Device.

        :return: описание устройства для пользователя
        :rtype: str
        """
        return (f"Создано устройство: (brand = {self.brand!r}, model = {self.model!r}, category = {self.category!r},"
                f" year = {self.year}, image = {self.image}, specs = {self.specs}, review = {self.review} )")


    @property
    def category(self) -> str:
        """
        Возвращает текущую категорию устройства.

        :return: категория устройства в формате с заглавной буквы
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category: str) -> None:
        """
        Устанавливает новую категорию устройства.

        Проверяет, что категория есть в списке разрешённых (ALLOWED_CATEGORIES).
        Если категория не найдена, выводится сообщение об ошибке.

        :param category: новая категория устройства
        :type category: str
        :raises: сообщение об ошибке, если категория не разрешена
        """
        if category.title() in self.ALLOWED_CATEGORIES:
            self._category = category.title()
        else:
            print(f'Категории: {category}. Нет в списке! ')

    @property
    def year(self) -> int:
        """
        Возвращает год выпуска устройства.

        :return: год выпуска
        :rtype: int
        """
        return self._year

    @year.setter
    def year(self, year: int | None) -> None:
        """
        Принимает новый год модели и обрабатывает её.
        Если передано None, устанавливается текущий год.
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
    def image(self) -> str | None:
        """
        Возвращает путь/ссылку на изображение устройства.

        :return: путь или ссылка на изображение
        :rtype: str | None
        """
        return self._image

    @image.setter
    def image(self, new_image: str) -> str | None:
        """
        Принимает новый экран модели и обрабатывает её.
        Если передано None, то будет установлена картинка по умолчанию.
        :param new_image: Новое значение изображения.
        :return: Год устройства в виде числа.
        """
        if new_image is None:
            self._image = '/'
        elif not isinstance(new_image, (str, type(None))):
            print(f'Значение экрана должно быть числом или None!')
        else:
            self._image = new_image



    @property
    def specs(self) -> dict:
        """
        Возвращает копию словаря с техническими характеристиками.

        :return: копия словаря specs
        :rtype: dict
        """
        return self._specs.copy()

    @specs.setter
    def specs(self, new_specs: dict) -> None:
        """
            Принимает словарь и обрабатывает его.
            :param new_specs: Новое значение словаря.
            :return: None.
        """
        if new_specs is None:
            self._specs = {}
        elif not isinstance(new_specs, dict):
            print(f'Параметр specs должен быть словарем!')
        else:
            self._specs = new_specs.copy()

    @property
    def review(self) -> Review | None:
        """
        Возвращает объект отзыва на устройство.

        :return: объект Review или None
        :rtype: Review | None
        """
        return self._review

    @review.setter
    def review(self, review: Review | None) -> None:
        """
            Принимает новое ревью модели и обрабатывает её.
            :param review: Новое значение ревью.
            :return: None.
        """
        if not isinstance(review, (Review, type(None))):
           print(f'Ревью должно быть в классе Review или None!')
        else:
            self._review = review

    @abstractmethod
    def get_device_type(self) -> str:
        """
        Абстрактный метод. Возвращает тип устройства.

        Должен быть реализован в дочерних классах.

        :return: тип устройства
        :rtype: str
        """
        pass

    @abstractmethod
    def get_short_description(self) -> str:
        """
        Абстрактный метод. Возвращает краткое описание устройства для превью на сайте.

        Должен быть реализован в дочерних классах.

        :return: краткое описание устройства
        :rtype: str
        """
        pass


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
            print(f'Ключ {key} не найден!')

    @classmethod
    def from_dict(cls, data: dict) -> Device | None:
        """
        Метод обрабатывает словарь с характеристиками
        Если в словаре недопустимый ключ, то код выдаст ошибку

        :param data: СЛОВАРЬ С ХАРАКТЕРИСТИКАМИ МОДЕЛИ
        :return: 'Device'
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