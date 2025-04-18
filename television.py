


class Television:
    """
    A class to simulate the behavior of a Television.
    Allows powering on/off, changing channels, adjusting volume,
    and muting/unmuting.
    """

    min_volume: int = 0
    max_volume: int = 2

    min_channel: int = 0
    max_channel: int = 3

    def __init__(self) -> None:
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.min_volume
        self.__channel: int = Television.min_channel

    def __str__(self) -> str:
        """
        Returns a string of the Power, Channel, and Volume
        """
        return f"Power - {self.__status}, Channel - {self.__channel}, Volume - {self.__volume}"

    def power(self) -> None:
        """
        Toggles power status of tv
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mutes the tv by setting volume to 0 and saving the previous volume
        If already muted, it will unmute
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                if hasattr(self, "_Television__prev_volume"): 
                    #because self.__prev_volume is created in mute method, there is a possibility of it creating an attribute error, so we check to see if the variable exists first before setting self.__volume to it
                    self.__volume = self.__prev_volume
            else:
                self.__prev_volume = self.__volume
                self.__muted = True
                self.__volume = 0

    def channel_up(self) -> None:
        """
        Increments the channel number, wrapping around if at max.
        """
        if self.__status:
            if self.__channel == Television.max_channel:
                self.__channel = Television.min_channel
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decrements the channel number, wrapping around if at min.
        """
        if self.__status:
            if self.__channel == Television.min_channel:
                self.__channel = Television.max_channel
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increases the volume by 1, up to max_volume.
        If muted, unmutes and restores previous volume before incrementing.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                if hasattr(self, "_Television__prev_volume"):
                    self.__volume = self.__prev_volume
            if self.__volume < Television.max_volume:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases the volume by 1, down to min_volume.
        If muted, unmutes and restores previous volume before decrementing.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                if hasattr(self, "_Television__prev_volume"):
                    self.__volume = self.__prev_volume
            if self.__volume > Television.min_volume:
                self.__volume -= 1

