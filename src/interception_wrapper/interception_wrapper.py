from time import sleep
from win32.win32api import GetSystemMetrics
from interception_py.interception import *
from interception_py.stroke import *
from interception_py.consts import *
from utils import *

# get screen size
_screen_width = GetSystemMetrics(0)
_screen_height = GetSystemMetrics(1)

@singleton
class _InterceptionWrapper:
    context = None
    mouse = 0
    keyboard = 0
    last_mouse_stroke = None
    pressed_mouse_button = None
    last_kbd_stroke = None

    def __init__(self):
        self.context = interception()
        for i in range(MAX_DEVICES):
            if interception.is_mouse(i):
                self.mouse = i
                break
        for i in range(MAX_DEVICES):
            if interception.is_keyboard(i):
                self.keyboard = i
                break

    def _send_mouse_stroke(self, stroke):
        self.context.send(self.mouse, stroke)

    def _send_keyboard_stroke(self, stroke):
        self.context.send(self.keyboard, stroke)

    def release_key(self, keycode):
        k_stroke = key_stroke(keycode, interception_key_state.INTERCEPTION_KEY_UP.value, 0)
        self.context.send(self.keyboard, k_stroke)

    def press_key(self, keycode):
        k_stroke = key_stroke(keycode, interception_key_state.INTERCEPTION_KEY_DOWN.value, 0)
        self.context.send(self.keyboard, k_stroke)

    def mouse_move(self, x, y, flag="absolute"):
        mstroke = mouse_stroke(mouse_button_state["left"]["up"],
                               mouse_flag[flag],
                               0,
                               to_hexadecimal(_screen_width, x),
                               to_hexadecimal(_screen_height, y),
                               0)
        self.context.send(self.mouse, mstroke)

    def click_mouse_with_coordinates(self, x, y, button="left", flag="absolute"):
        mstroke = mouse_stroke(mouse_button_state[button]["down"],
                               mouse_flag[flag],
                               0,
                               to_hexadecimal(_screen_width, x),
                               to_hexadecimal(_screen_height, y),
                               0)
        self.context.send(self.mouse, mstroke)
        sleep(0.2)
        mstroke.state = mouse_button_state[button]["up"]
        self.context.send(self.mouse, mstroke)

    def press_mouse_key(self, button="left"):
        m_stroke = mouse_stroke(
            mouse_button_state[button]["down"],
            interception_mouse_flag.INTERCEPTION_MOUSE_MOVE_RELATIVE.value,
            0,
            int(0xFFFF * 0),
            int(0xFFFF * 0),
            0)
        self._send_mouse_stroke(m_stroke)
        self.last_mouse_stroke = m_stroke
        self.pressed_mouse_button = button

    def release_mouse_key(self):
        if self.last_mouse_stroke is not None and self.pressed_mouse_button is not None:
            self.last_mouse_stroke.state = mouse_button_state[self.pressed_mouse_button]["up"]
            self._send_mouse_stroke(self.last_mouse_stroke)


interception_wrapper = _InterceptionWrapper()