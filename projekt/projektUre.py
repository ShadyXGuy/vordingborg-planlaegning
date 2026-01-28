import time


class Ur:
    def __init__(self):
        self.updateTimer()

    def updateTimer(self):
        self.year = time.localtime().tm_year
        self.month = time.localtime().tm_mon
        self.day = time.localtime().tm_mday
        self.hour = time.localtime().tm_hour
        self.minute = time.localtime().tm_min
        self.second = time.localtime().tm_sec

class StopUr():
    def __init__(self):
        self.startTime = time.time()

    def timeDif(self):
        current = time.time()
        return round(current - self.startTime,2)


# lav timestamp når bruges IKKE i klassen (kig evt round for at afrounde til 2 cifre hvis behov)

class Alarm(Ur):
    def __init__(self):
        super().__init__()
        self.alarm_hour = None
        self.alarm_minute = None
        self.alarm_day = None
        self.enable = False

    #tager input til set dag time minut alarmen bruger (i instance)
    def setTime(self,day,hour,minute):
        if day is None or hour is None or minute is None:
            self.enable = False
            return
        self.alarm_day = int(day)
        self.alarm_hour = int(hour)
        self.alarm_minute = int(minute)
        self.enable = True
    #checks if trigger
    def check(self):
        self.updateTimer()
        return (
                self.enable and
                self.hour == self.alarm_hour and
                self.minute == self.alarm_minute and
                self.day == self.alarm_day
        )

pass


#instance til test
ur = Ur()
stopur = StopUr()
alarm = Alarm()

alarm.setTime(7,10,55)


if __name__ == "__main__":
    while True:
        ur.updateTimer()
        print(ur.hour, ur.minute, ur.second)
        print(stopur.timeDif())
        time.sleep(1)





