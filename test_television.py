import pytest
import television
from main import *


class TestTelevision:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test__init__(self):
        assert Television.__str__(self.tv) == f"Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"

    def test_power(self):
        Television.power(self.tv)
        assert Television.__str__(self.tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"
        Television.power(self.tv)
        assert Television.__str__(self.tv) == f"Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"

    def test_volume_up(self):
        Television.power(self.tv)
        Television.volume_up(self.tv)
        assert Television.__str__(self.tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME + 1}"

    def test_mute(self):
        Television.power(self.tv)
        Television.volume_up(self.tv)
        Television.mute(self.tv)
        assert Television.__str__(self.tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = 0"
        Television.mute(self.tv)
        assert Television.__str__(self.tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME + 1}"
        Television.power(self.tv)
        Television.mute(self.tv)
        assert Television.__str__(self.tv) == f"Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"
        Television.mute(self.tv)
        assert Television.__str__(self.tv) == f"Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"

    def test_volume_down(self):
        Television.power(self.tv)
        Television.volume_down(self.tv)
        assert Television.__str__(self.tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"

    def test_channel_up(self):
        Television.channel_up(self.tv)
        assert Television.__str__(self.tv) == f"Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"
        Television.power(self.tv)
        Television.channel_up(self.tv)
        assert Television.__str__(self.tv) == f"Power = True, Channel = {Television.MIN_CHANNEL + 1}, Volume = {Television.MIN_VOLUME}"
        Television.channel_up(self.tv)
        Television.channel_up(self.tv)
        Television.channel_up(self.tv)
        assert Television.__str__(self.tv) == f"Power = True, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"

    def test_channel_down(self):
        Television.channel_down(self.tv)
        assert Television.__str__(self.tv) == f"Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"
        Television.power(self.tv)
        Television.channel_down(self.tv)
        assert Television.__str__(self.tv) == f"Power = True, Channel = {Television.MAX_CHANNEL}, Volume = {Television.MIN_VOLUME}"

    def test__str__(self):
        assert Television.__str__(self.tv) == f"Power = False, Channel = {Television.MIN_CHANNEL}, Volume = {Television.MIN_VOLUME}"