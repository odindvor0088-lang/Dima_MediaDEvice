from abc import ABC, abstractmethod


class Device(ABC):

    MIN_VOLUME = 0
    MAX_VOLUME = 100
    BATTERY_WARNING_LEVEL = 20
    ALLOWED_CATEGORIES = ["Смартфоны", "Наушники", "Ноутбуки", "Планшеты", "Умные часы"]

    def __init__(self, brand: str, model: str, category: str,  year: int = None,  image = None) -> None:
        self.brand = brand
        self.model = model
        self.category = category
        self.year = year
        self.image = image

    @property
    def category(self) -> str:
        """Возвращает текущую категорию."""
        return self.category

    @category.setter
    def category(self, category: str) -> None:
        """Принимает новую категорию и обрабатывает её."""
        if category.upper() not in self.ALLOWED_CATEGORIES:
            print(f'Категории: {category}. Нет в списке ')
        elif not isinstance(category, str):
            print(f'Категория должна состоять из букв!')
        else:
            self.category = category


    @property
    def year(self) -> int:
        """Возвращает текущий год модели."""
        return self.year

    @year.setter
    def year(self, year: int) -> None:
        """Принимает новый год модели и обрабатывает её."""
        if not isinstance(year, int):
            print(f'Год модели {self.model} должен состоять из чисел!')
        else:
            self.year = year

    @property
    def image(self) -> str:
        """Возвращает текущий экран модели."""
        return self.image

    @image.setter
    def image(self, image: str) -> None:
        """Принимает новый экран модели и обрабатывает её."""
        self.image = image


