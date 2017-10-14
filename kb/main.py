import uinput
import time

DATA_PATH = '/proc/mouseListener/info'

# device = uinput.Device([
#     uinput.KEY_E,
#     uinput.KEY_H,
#     uinput.KEY_L,
#     uinput.KEY_O,
#     uinput.KEY_C,
#     uinput.KEY_LEFTCTRL,
#     uinput.KEY_BACKSLASH,
#     uinput.KEY_LEFTSHIFT
# ])
# time.sleep(1)


def execute_action():
    print('execute_action')


def next_set():
    print('next_set')


def previous_action():
    print('previous_action')


def next_action():
    print('next_action')


def execute_buffer():
    print('execute_buffer')


def read_data():
    with open(DATA_PATH) as f:
        return int(f.readline()), f.readline().strip()


button_to_command = {
    'LEFT': execute_action,
    'RIGHT': next_set,
    'MIDDLE': execute_buffer,
    'WHEELUP': previous_action,
    'WHEELDOWN': next_action
}
last_id = read_data()[0]
while True:
    current_id, button = read_data()
    if current_id != last_id:
        last_id = current_id
        button_to_command[button]()
    time.sleep(0.1)
