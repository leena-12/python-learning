from datetime import datetime

now = datetime.now()

print(now)
print(now.date())
print(now.time())
print(now.strftime("%d-%m-%Y"))
print(now.strftime("%d-%m-%Y %H:%M:%S"))