import pytest
from src.device.device import Device
from src.device.categories import CategoriesDevice


class TestDevice(Device):
    def get_device_type(self) -> str:
        return "test_device"


    def get_short_description(self) -> str:
        return "Test description"


    @pytest.fixture
    def device(self):
        return TestDevice(
            brand="Samsung",
            model="Galaxy S23",
            category=CategoriesDevice.SMARTPHONE
        )


    def test_specs_set_none(self, device):
        device.specs = None
        assert device.specs == {}

    def test_add_spec(self, device):
        device.add_spec("RAM", "8 GB")
        assert device.specs == {"RAM": "8 GB"}

    def test_remove_spec(self, device):
        device.remove_spec("RAM")
        assert device.specs == {}

    def test_encapsulation(self, device):
        external_specs = {"RAM": "8 GB"}
        device.specs = external_specs
        external_specs["RAM"] = "16 GB"
        assert device.specs == {"RAM": "8 GB"}