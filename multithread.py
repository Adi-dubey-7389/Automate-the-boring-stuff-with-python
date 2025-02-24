import time, datetime

start= datetime.datetime(2029, 10, 31, 0, 0, 0)
while datetime.datetime.now() < start:
    time.sleep(1)

print('Program now starting on Halloween 2029')



