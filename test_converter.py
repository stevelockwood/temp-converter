import pytest
from converter import Converter

class TestConverter:
    def test_constructor(self):
        conv = Converter()
        conv.toCelsius()
        assert conv.converted_temp == -40
        conv.toFahrenheit()
        assert conv.converted_temp == -40

    def test_toCelsius(self):
         conv = Converter()
         conv.setTemp(212)
         conv.toCelsius()
         assert conv.converted_temp == 100

    def test_toFahrenheit(self):
         conv = Converter()
         conv.setTemp(0)
         conv.toFahrenheit()
         assert conv.converted_temp == 32
