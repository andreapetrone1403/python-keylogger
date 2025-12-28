from pynput.keyboard import Key, Listener

def keylog(key):
    print(key)

with Listener(on_press=keylog) as listener:
    listener.join()