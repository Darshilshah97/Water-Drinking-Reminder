import time
from plyer import notification
from datetime import datetime

count = 1
time_interval = int(input('Please enter the time interval(in seconds)  you want to receive water drinking notification.'))
print('Info: It send 2 notifications for the interval you entered.')

while(count < 3):

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    notification.notify(
        title = 'Water Drinking Reminder ' + str(count) + ' at time ' + current_time,
        message = 'Hey Darshil, Don\'t forget to drink water',
        app_icon = 'Waterglass.ico',
        timeout = 10,
    )
    count = count + 1
    time.sleep(time_interval)