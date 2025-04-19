class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Sets the default of the tv settings
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """
        Turns the tv off if it was on, and on if it was off
        """
        if self.__status == True:
            self.__status = False
        else:
            self.__status = True

    def mute(self):
        """
        Mutes/unmutes the tv depending on previous settings
        """
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self):
        """
        Increases the channel by 1; if channel is at max, it goes to min
        """
        if self.__status == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """
        Decreases the channel by 1; if channel is at min, it goes to max
        """
        if self.__status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        """
        Increases the volume by 1; if volume is at max, it stays the same
        """
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            else:
                self.__volume += 1

    def volume_down(self):
        """
        Decreases the volume by 1; if volume is at min, it stays the same
        """
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
            if self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume -= 1

    def __str__(self):
        """
        Sets string formatting to list the power, channel, and volume settings; if muted, volume = min volume
        """
        if self.__muted == True:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"