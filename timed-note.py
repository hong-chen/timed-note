import os
from datetime import datetime
from pynput import keyboard

def PRESS(key):
    dtime0 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(dtime0)
    message = input(': ')
    print()
    print(message)
    print()

def RELEASE(key):
    return False

# fname = datetime.now().strftime('timed-note_%Y-%m-%d.txt')
# if os.path.exists(fname):
#     with open(fname, 'r+') as f
# else:
#     with open(fname, 'w') as f

def KEY_MONITORING():
    with keyboard.Listener(on_press=PRESS, on_release=RELEASE) as listener:
        listener.join()

message = ''
print('Hit [Enter] to start ...\n')
while message != 'exit':
    KEY_MONITORING()
    keyboard.Listener.stop
    # if listener.key != keyboard.Key.esc:

    # if message == '':
        # f.write('+\n')
        # f.write('%s\n' % dtime0)
        # print('UTC %s' % datetime.now().strftime('%Y/%m/%d-%H:%M:%S'))
        # message0 = input('message:')
        # f.write('%s\n' % message0)
        # f.write('-\n')
    # else:
        # f.write('+\n')
        # dtime0 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # f.write('%s\n' % dtime0)
        # f.write('%s\n' % message)
        # f.write('-\n')

exit()
