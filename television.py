class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Initializes the default settings for the television."""
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__previous_volume = Television.MIN_VOLUME
        self.__volume_display = Television.MIN_VOLUME  # Initialize volume display

    def power(self) -> None:
        """Toggles the power status of the television."""
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Toggles the mute status of the television.
        When muting, the current volume is saved and set to 0.
        When unmuting, the volume is restored to the saved value.
        """
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
        """Increases the channel by one."""
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """Decreases the channel by one."""
        if self.__status:
            self.__channel = (self.__channel - 1) % (Television.MAX_CHANNEL + 1)

    def volume_up(self) -> None:
        """Increases the volume by one, up to the maximum volume."""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
                self.__volume_display = self.__volume

    def volume_down(self) -> None:
        """Decreases the volume by one, down to the minimum volume."""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                self.__volume_display = self.__volume

    @property
    def volume(self) -> int:
        """Returns the current volume of the television."""
        return self.__volume

    @property
    def channel(self) -> int:
        """Returns the current channel of the television."""
        return self.__channel

    @property
    def is_muted(self) -> bool:
        """Returns True if the television is muted, otherwise False."""
        return self.__muted

    def __str__(self) -> str:
        """
        Returns a string representation of the television's status,
        including power status, channel, and volume.
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume_display}'
