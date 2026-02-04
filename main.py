from abc import ABC, abstractmethod

class MediaDevice(ABC):

    MAX_VOLUME = 100
    MIN_VOLUME = 0
    BATTERY_WARNING_LEVEL = 20
    manufacturer_country = "Russia"

    def init(self, brand, model, battery_level, is_on, current_volume):
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