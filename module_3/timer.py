from datetime import datetime, timedelta
import os

if __name__ == '__main__':
    os.system("cls")
    while True:
        try:
            start = int(input("Please input start time in 24-hour format 0-23:> "))
            if start < 0 or start > 23:
                print("Incorrect input '{}' start value should be between 0 and 23".format(start))
            else:
                timer = int(input("Please input timer value in hours:> "))
                time = datetime(1970, 1, 1, start, 0, 0)
                fire = time + timedelta(hours=timer)
                print("Start time is {} timer will fire in {} hours at {}.".format(time.strftime("%H:%M"), timer, fire.strftime("%H:%M")))
                break
        except:
            print("Can't parse value, please try again")