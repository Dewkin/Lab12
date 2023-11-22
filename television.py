class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__previous_volume = Television.MIN_VOLUME
        self.__volume_display = Television.MIN_VOLUME

    def power(self) -> None:
        self.__status = not self.__status

    def mute(self) -> None:
        if self.__status:
            if not self.__muted:
                self.__previous_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
                self.__volume_display = Television.MIN_VOLUME
            else:
                self.__volume = self.__previous_volume
                self.__volume_display = self.__previous_volume
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        if self.__status:
            self.__channel = (self.__channel - 1) % (Television.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                self.__volume_display = self.__volume

    def volume_down(self) -> None:
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                self.__volume_display = self.__volume

    @property
    def volume(self) -> int:
        return self.__volume

    @property
    def channel(self) -> int:
        return self.__channel

    @property
    def is_muted(self) -> bool:
        return self.__muted

    def __str__(self) -> str:
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume_display}'
