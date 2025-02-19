import time
print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch.\nPress Ctrl-C to quit.')
input()
print('Started')
start=time.time()
last= start
lap=1

try:
    while True:
        input()
        lapTime = round(time.time() - last, 2)
        totalTime = round(time.time() - start, 2)
        print('Lap #%s: %s (%s)' % (lap, totalTime, lapTime), end='')
        lap+= 1
        last = time.time() 
except KeyboardInterrupt:
    print('\nDone.')























