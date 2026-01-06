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

class StopUr(Ur):
    def __init__(self):
        super().__init__()
        self.startTime = time.time()

    def timeDif(self):
        current = time.time()
        return current - self.startTime
# lav timestamp når bruges IKKE i klassen (kig evt round for at afrounde til 2 cifre hvis behov)



pass


#instance til test
ur = Ur()
stopur = StopUr()

#test
if __name__ == "__main__":
    while True:
        ur.updateTimer()
        print(ur.hour, ur.minute, ur.second)
        print(stopur.timeDif())
        time.sleep(1)


