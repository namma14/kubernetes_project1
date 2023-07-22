import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title = "Please Drink water",
        message = "As per  U.S. National Academies of Sciences, Engineering, and Medicine.About 15.5 cups (3.7 liters) of fluids a day for men is required.Drink Up!!!!",
        app_icon = "C:\\Users\\Viajy\\Desktop\\python\\PractiseSet_Youtube_CodewithHarry\\icon.ico",
        timeout=5
    )