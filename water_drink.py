import time
from plyer import notification
from datetime import datetime

count = 1
name = input("Enter your name: ")
minutes = int(input(f'{name}, after how many each minutes you want to receive water drinking reminder (Please enter minutes in whole numbers): '))


print('Info: It send 2 notifications for the interval you entered.')

while(True):

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    notification.notify(
        title = 'Water Drinking Reminder ' + str(count) + ' at time ' + current_time,
        message = f'Hey {name}, Don\'t forget to drink water',
        app_icon = 'Waterglass.ico',
        timeout = 10,
    )
    count = count + 1
    time.sleep(minutes*60)