from plyer import notification 
import time 
if __name__ == "__main__":
  while True:
    notification.notify(
        title = "it's 9 p.m.",
        message = "time to sleep. you have to wake up early in the morning",
        #app_icon=r"C:\Users\DELL\Downloads\icon.ico",
        timeout = 5)
    time.sleep(4) 
  
