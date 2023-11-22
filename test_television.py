import pytest
from television import Television

def test_init():
    tv = Television()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

def test_power():
    tv = Television()
    tv.power()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'
    tv.power()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

def test_mute():
    tv = Television()
    tv.power()
    original_volume = tv.volume
    tv.mute()
    assert tv.is_muted
    assert tv.volume == 0
    tv.mute()
    assert not tv.is_muted
    assert tv.volume == original_volume

def test_channel_up():
    tv = Television()
    tv.power()
    for _ in range(Television.MAX_CHANNEL):
        tv.channel_up()
    assert tv.channel == Television.MAX_CHANNEL
    tv.channel_up()
    assert tv.channel == Television.MIN_CHANNEL
    assert str(tv) == f'Power = True, Channel = {Television.MIN_CHANNEL}, Volume = 0'

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert tv.channel == Television.MAX_CHANNEL
    tv.channel_down()
    assert tv.channel == Television.MAX_CHANNEL - 1
    assert str(tv) == f'Power = True, Channel = {Television.MAX_CHANNEL - 1}, Volume = 0'

def test_volume_up():
    tv = Television()
    tv.power()
    for _ in range(Television.MAX_VOLUME):
        tv.volume_up()
    assert tv.volume == Television.MAX_VOLUME
    tv.volume_up()
    assert tv.volume == Television.MAX_VOLUME
    assert str(tv) == f'Power = True, Channel = 0, Volume = {Television.MAX_VOLUME}'

def test_volume_down():
    tv = Television()
    tv.power()
    for _ in range(Television.MAX_VOLUME + 1):
        tv.volume_down()
    assert tv.volume == Television.MIN_VOLUME
    assert str(tv) == f'Power = True, Channel = 0, Volume = {Television.MIN_VOLUME}'

def test_invalid_operations_when_off():
    tv = Television()
    tv.channel_up()
    assert tv.channel == 0
    tv.channel_down()
    assert tv.channel == 0
    tv.volume_up()
    assert tv.volume == 0
    tv.volume_down()
    assert tv.volume == 0
