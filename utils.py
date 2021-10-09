from interception_py.consts import *

mouse_button_state = {
    "left": {
        "up": interception_mouse_state.INTERCEPTION_MOUSE_LEFT_BUTTON_UP.value,
        "down": interception_mouse_state.INTERCEPTION_MOUSE_LEFT_BUTTON_DOWN.value,
    },
    "right": {
        "up": interception_mouse_state.INTERCEPTION_MOUSE_RIGHT_BUTTON_UP.value,
        "down": interception_mouse_state.INTERCEPTION_MOUSE_RIGHT_BUTTON_DOWN.value,
    },
    "middle": {
        "up": interception_mouse_state.INTERCEPTION_MOUSE_MIDDLE_BUTTON_UP.value,
        "down": interception_mouse_state.INTERCEPTION_MOUSE_MIDDLE_BUTTON_DOWN.value,
    },
}

mouse_flag = {
    "absolute": interception_mouse_flag.INTERCEPTION_MOUSE_MOVE_ABSOLUTE.value,
    "relative": interception_mouse_flag.INTERCEPTION_MOUSE_MOVE_RELATIVE.value
}

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

def to_hexadecimal(screen_side: int, i: int):
    return int((0xFFFF / screen_side) * i)