import threading, time
print('Start of program.')

def takeANap():
    time.sleep(5)
    print('Wake up!')

thread = threading.Thread(target=takeANap)
thread.start()

print('End of program.')
