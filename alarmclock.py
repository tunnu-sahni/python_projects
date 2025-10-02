# import datetime
# import time
# import winsound

# def alarm(set_time):
#     while True:
#         current_time = datetime.datetime.now().strftime("%H:%M:%S")

#         print("current time:",current_time, end="\r")

#         if current_time == set_time:
#             print("\nwake up time to get up: ")

#         for i in range(5):
#             winsound.Beep(1000,1000)
#             break
#         time.sleep(1)

# set_time = input("enter alarm time (HH:MM:SS): ")

# alarm(set_time)





import datetime
import time
import winsound

def alarm(set_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H: %M: %S")
        print("current time = set_time", end="\r")

        if current_time == set_time:
          print("\n wake up to get up:")

        for i in range(5):
         winsound.Beep(1000,1000)
         break
        time.sleep(1)

set_time = input("enter the time:")
alarm(set_time)


    


