


class Television:
    min_volume = 0
    max_volume = 2
    
    min_channel = 0
    max_channel = 3
    
    def __init__(self):
        
        self.__status = False
        self.__muted = False
        self.__volume = Television.min_volume
        self.__channel = Television.min_channel
        
        
    def __str__(self):
        return f"Power - {self.__status}, Channel - {self.__channel}, Volume - {self.__volume}"

        
        
    def power(self):
        if self.__status:
            self.__status = False
        else:
            self.__status = True
    
    def mute(self):
        
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.prev_vol = self.__volume
                self.__muted = True
                self.__volume = 0
                
    
    def channel_up(self):
        if self.__status:
            if self.__channel == Television.max_channel:
                self.__channel = Television.min_channel
            else:
                self.__channel += 1
    
    def channel_down(self):
        if self.__status:
            if self.__channel == Television.min_channel:
                self.__channel = Television.max_channel
            else:
                self.__channel -= 1
    
    def volume_up(self):
        if self.__status:
            if self.__muted:
                self.__muted = False  
                self.__volume = self.prev_vol
            if self.__volume < Television.max_volume:
                self.__volume += 1

    def volume_down(self):
        if self.__status:
            if self.__muted:
                self.__muted = False  
                self.__volume = self.prev_vol
            if self.__volume > Television.min_volume:
                self.__volume -= 1
    