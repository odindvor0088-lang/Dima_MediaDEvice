from abc import ABC, abstractmethod

class MediaDevice(ABC):

    MAX_VOLUME = 100
    MIN_VOLUME = 0
    BATTERY_WARNING_LEVEL = 20
    manufacturer_country = "Russia"

    def __init__(self, brand, model, battery_level, is_on, current_volume):
        self.brand = brand
        self.model = model
        self.is_on = is_on
        self.battery_level = battery_level
        self.current_volume = current_volume

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
        self.is_on = True
        print(" Устройство включено")

    def power_off(self):
        self.is_on = False
        print("Устройство выключено")

    def charge(self):
        if self.battery_level == self.BATTERY_WARNING_LEVEL:
            print("Поставьте устройство на зарядку! (Уровень батареи 20%)")

    def adjust_volume(self, level):
        my_volume = level
        if my_volume > self.MAX_VOLUME:
            print("Уровень звука не может быть больше 100!")
        elif my_volume < self.MIN_VOLUME:
            print("Уровень звука не может быть меньше 0!")
        else:
            print("Уровень звука установлен.")

    def str(self):
        return f"{self.brand} {self.model} {self.battery_level} {self.is_on} {self.current_volume}"

    @staticmethod
    def check_battery_health(cycles):
        my_cycles = list(map(int, cycles))
        if my_cycles[0] >= 90:
            print("Состояние батареи отличное")
        elif my_cycles[0] >= 70:
            print("Состояние батареи хорошее")
        elif my_cycles[0] >= 40:
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