import csv
import random
from datetime import datetime, timedelta

apps = ['WhatsApp', 'Facebook', 'Instagram']
start_date = datetime.today() - timedelta(days=29)

with open('screen_time_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'App', 'ScreenTimeMinutes', 'Notifications', 'TimesOpened'])
    
    for i in range(30):
        date = (start_date + timedelta(days=i)).strftime('%Y-%m-%d')
        for app in apps:
            screen_time = random.randint(10, 180)
            notifications = random.randint(1, 50)
            times_opened = random.randint(1, 30)
            writer.writerow([date, app, screen_time, notifications, times_opened])
