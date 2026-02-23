from abc import ABC, abstractmethod

class MediaDevice(ABC):

    MAX_VOLUME = 100
    MIN_VOLUME = 0
    BATTERY_WARNING_LEVEL = 20
    manufacturer_country = "Russia"

    def __init__(self, brand, model, battery_level, current_volume):
        self.brand = brand
        self.model = model
        self._is_on = False
        self._battery_level = battery_level
        self._current_volume = current_volume

    @abstractmethod
    def play(self):
        """начать воспроизведение"""
        pass

    @abstractmethod
    def stop(self):
        """остановить воспроизведение"""
        pass

    @abstractmethod
    def get_device_type(self):
        """возвращает тип устройства"""
        pass

    def power_on(self):
        self._is_on = True
        print(" Устройство включено")

    def power_off(self):
        self._is_on = False
        print("Устройство выключено")

    def charge(self):
        if self._battery_level == self.BATTERY_WARNING_LEVEL:
            print("Поставьте устройство на зарядку! (Уровень батареи 20%)")

    def adjust_volume(self, level):
        my_volume = level
        if my_volume > self.MAX_VOLUME:
            print("Уровень звука не может быть больше 100!")
        elif my_volume < self.MIN_VOLUME:
            print("Уровень звука не может быть меньше 0!")
        else:
            print("Уровень звука установлен.")

    def __str__(self):
        return f"{self.brand} {self.model} {self._battery_level} {self._is_on} {self._current_volume}"

    @staticmethod
    def check_battery_health(quantity_cycles):
        if quantity_cycles >= 90:
            print("Состояние батареи отличное")
        elif quantity_cycles >= 70:
            print("Состояние батареи хорошее")
        elif quantity_cycles >= 40:
            print("Состояние батареи среднее")
        else:
            print("Состояние батареи плохое. Поменяйте батарею")

    @classmethod
    def from_dict(cls, data):
        return cls(
            brand=data.get("brand"),
            model=data.get("model"),
            current_volume=data.get("current_volume", 0),
            battery_level=data.get("battery_level", 0),
        )

    @property
    def is_on(self):
        """Геттер для is_on"""
        return self._is_on


    @property
    def battery_level(self):
        """Геттер для battery_level"""
        return self._battery_level

    @battery_level.setter
    def battery_level(self, value):
        """Сеттер для battery_level"""
        self._is_on = True
        if value < 0:
            print("Значение батареи не может быть меньше 0")
        elif value > 100:
            print("Значение батареи не может быть больше 100")
        self._battery_level = value
        print(f"Заряд батареи: {self._battery_level}%")

        if self._battery_level == 0 and self._is_on:
            self._is_on = False
            print("Устройство выключилось из-за разрядки")

    @property
    def current_volume(self):
        """Геттер для current_volume"""
        return self._current_volume

    @current_volume.setter
    def current_volume(self, value):
        """Сеттер для current_volume"""
        self._is_on = True
        if not isinstance(value, (int, float)):
            print("Уровень заряда должен быть числом")
        if value > self.MAX_VOLUME:
            print("Громкость не может быть выше 100")
        elif value < self.MIN_VOLUME:
            print("Громкость не может быть ниже 0")
        elif value >= 70:
            print("Данная громкость может навредить вашему здоровью!")

        self._current_volume = value
        print(f"Громкость на устройстве: {self._current_volume}")
