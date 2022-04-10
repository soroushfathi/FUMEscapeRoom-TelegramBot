from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S").split(':')
print(current_time)
