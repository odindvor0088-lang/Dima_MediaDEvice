from abc import ABC, abstractmethod
from datetime import datetime


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
        self.brand = brand
        self.model = model
        self.category = category
        self.year = year
        self.image = image
        self._specs = {}
        self._review = None
        self.battery_level = 100
        self.current_volume = 50
        self.is_on = False

    @property
    def category(self) -> str:
        """Возвращает текущую категорию."""
        return self.category

    @category.setter
    def category(self, category: str) -> None:
        """
        Принимает новую категорию и обрабатывает её.
        :param category: Новая категория.
        :return: None.
        """
        if category.title() not in self.ALLOWED_CATEGORIES:
            print(f'Категории: {category}. Нет в списке! ')
        else:
            self.category = category

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
        current_year = datetime.now().year
        min_value = 1990
        if year is None:
            self._year = None
            return
        if not isinstance(year, int) and year >= min_value:
            print(f'Год модели {self.model} должен состоять из чисел!')
            return
        if year < min_value:
            print(f'Год модели {self.model} не может быть раньше {min_value}!')
        elif year > current_year:
            print(f'Год модели {self.model} не может быть позже {current_year}!')
        else:
            self._year = year


    @property
    def image(self) -> str:
        """Возвращает текущий экран модели."""
        return self.image

    @image.setter
    def image(self, image: str) -> None:
        """
        Принимает новый экран модели и обрабатывает её.
        :param image: Новое значение изображения.
        :return: None.
        """
        self.image = image

    @property
    def battery_level(self) -> int:
        """Возвращает текущий заряд модели."""
        return self.battery_level

    @battery_level.setter
    def battery_level(self, battery_level: int) -> None:
        """
        Принимает новый заряд модели и обрабатывает её.
        :param battery_level: Новое значение заряда.
        :return: None.
        """
        if not isinstance(battery_level, int):
            print(f'Заряд модели должен состоять из чисел!')
        elif battery_level < 0:
            print(f'Заряд модели не может быть меньше 0!')
        elif battery_level > 100:
            print(f'Заряд модели не может быть больше 100!')
        else:
            self.battery_level = battery_level

    @property
    def current_volume(self) -> int:
        """Возвращает текущую громкость модели."""
        return self.current_volume

    @current_volume.setter
    def current_volume(self, current_volume: int) -> None:
        """
        Принимает новую громкость модели и обрабатывает её.
        :param current_volume: Новое значение уровня звука.
        :return: None.
        """
        if not isinstance(current_volume, int):
            print(f'Громкость модели должен состоять из чисел!')
        elif current_volume < 0:
            print(f'Громкость модели не может быть меньше 0!')
        elif current_volume > 100:
            print(f'Громкость модели не может быть больше 100!')
        else:
            self.current_volume = current_volume

    @property
    def is_on(self) -> bool:
        """Возвращает текущее состояние модели."""
        return self.is_on

    @is_on.setter
    def is_on(self, is_on: bool) -> None:
        """
                Принимает новое состояние модели и проверяет ее.
                :param is_on: Новое состояние модели.
                :return: None.
                """
        if not isinstance(is_on, bool):
            print(f'Состояние должно быть булевым значением (True/False)!')
        else:
            self.is_on = is_on

    @abstractmethod
    def play(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass

    @abstractmethod
    def get_device_type(self) -> str:
        #Возвращает текущую категория устройства
        pass

    @property
    def specs(self) -> dict:
        """Возвращает текущие характеристики."""
        return self.specs.copy()



