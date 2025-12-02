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



pass

ur = Ur()


if __name__ == "__main__":
    while True:
        ur.updateTimer()
        print(ur.hour, ur.minute, ur.second)
        time.sleep(1)


