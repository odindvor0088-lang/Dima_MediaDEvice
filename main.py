from abc import ABC, abstractmethod

class MediaDevice(ABC):

    MAX_VOLUME = 100
    MIN_VOLUME = 0
    BATTERY_WARNING_LEVEL = 20
    manufacturer_country = "Russia"

    def __init__(self, brand, model, battery_level, is_on, current_volume):
        self.brand = brand
        self.model = model
        self._is_on = is_on
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
            brand=data["brand"],
            model=data["model"],
            is_on=data["is_on"],
            current_volume=data["current_volume"],
            battery_level=data["battery_level"],
        )
    @property
    def get_is_on(self):
        """Геттер для is_on"""
        return self._is_on
    @get_is_on.setter
    def is_on(self, value):
        """Сеттер для is_on"""
        self._is_on = value
        print(f"Устройство включено")

    @property
    def get_battery_level(self):
        """Геттер для battery_level"""
        return self._battery_level

    @get_battery_level.setter
    def get_battery_level(self, value):
        """Сеттер для battery_level"""
        self._battery_level = value
        print(f"Заряд батареи: {self._battery_level}%")

        if self._battery_level == 0 and self._is_on:
            self._is_on = False
            print("Устройство выключилось из-за разрядки")

    @property
    def get_current_volume(self):
        """Геттер для current_volume"""
        return self._current_volume

    @get_current_volume.setter
    def get_current_volume(self, value):
        """Сеттер для current_volume"""
        if value >= 70:
            print("Данная громкость может навредить вашему здоровью!")

        self._current_volume = value
        print(f"Громкость на устройстве: {self._current_volume}")
