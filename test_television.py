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
    assert tv.volume == original_volume
    tv.mute()
    assert not tv.is_muted
    assert tv.volume == original_volume

def test_channel_up():
    tv = Television()
    tv.power()
    original_channel = tv.channel
    tv.channel_up()
    assert tv.channel == original_channel + 1
    # Test for maximum channel limit
    tv.channel = tv.max_channel
    tv.channel_up()
    assert tv.channel == tv.max_channel

def test_channel_down():
    tv = Television()
    tv.power()
    original_channel = tv.channel
    tv.channel_down()
    assert tv.channel == original_channel - 1
    # Test for minimum channel limit
    tv.channel = tv.min_channel
    tv.channel_down()
    assert tv.channel == tv.min_channel

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert 'Volume = 1' in str(tv)
    tv.volume_up()
    assert 'Volume = 2' in str(tv)
    tv.volume_up()
    assert 'Volume = 2' in str(tv)


def test_volume_down():
    tv = Television()
    tv.power()
    original_volume = tv.volume
    tv.volume_down()
    assert tv.volume == original_volume - 1
    # Test for minimum volume limit
    tv.volume = tv.min_volume
    tv.volume_down()
    assert tv.volume == tv.min_volume

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
