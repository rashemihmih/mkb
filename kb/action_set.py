import uinput

from action import Click, Shift


class ActionSet:
    pos = 0

    def __init__(self, name, actions):
        self.name = name
        self.actions = actions

    def selected_action(self):
        return self.actions[self.pos]

    def next_action(self):
        self.pos += 1
        if self.pos >= len(self.actions):
            self.pos = 0
        return self.selected_action()

    def previous_action(self):
        self.pos -= 1
        if self.pos < 0:
            self.pos = len(self.actions) - 1
        return self.selected_action()


class Letters(ActionSet):
    def __init__(self):
        super().__init__('Letters', [
            Click('a', uinput.KEY_A),
            Click('b', uinput.KEY_B),
            Click('c', uinput.KEY_C),
            Click('d', uinput.KEY_D),
            Click('e', uinput.KEY_E),
            Click('f', uinput.KEY_F),
            Click('g', uinput.KEY_G),
            Click('h', uinput.KEY_H),
            Click('i', uinput.KEY_I),
            Click('j', uinput.KEY_J),
            Click('k', uinput.KEY_K),
            Click('l', uinput.KEY_L),
            Click('m', uinput.KEY_M),
            Click('n', uinput.KEY_N),
            Click('o', uinput.KEY_O),
            Click('p', uinput.KEY_P),
            Click('q', uinput.KEY_Q),
            Click('r', uinput.KEY_R),
            Click('s', uinput.KEY_S),
            Click('t', uinput.KEY_T),
            Click('u', uinput.KEY_U),
            Click('v', uinput.KEY_V),
            Click('w', uinput.KEY_W),
            Click('x', uinput.KEY_X),
            Click('y', uinput.KEY_Y),
            Click('z', uinput.KEY_Z)
        ])


class CapitalLetters(ActionSet):
    def __init__(self):
        super().__init__('Capital Letters', [
            Shift('A', uinput.KEY_A),
            Shift('B', uinput.KEY_B),
            Shift('C', uinput.KEY_C),
            Shift('D', uinput.KEY_D),
            Shift('E', uinput.KEY_E),
            Shift('F', uinput.KEY_F),
            Shift('G', uinput.KEY_G),
            Shift('H', uinput.KEY_H),
            Shift('I', uinput.KEY_I),
            Shift('J', uinput.KEY_J),
            Shift('K', uinput.KEY_K),
            Shift('L', uinput.KEY_L),
            Shift('M', uinput.KEY_M),
            Shift('N', uinput.KEY_N),
            Shift('O', uinput.KEY_O),
            Shift('P', uinput.KEY_P),
            Shift('Q', uinput.KEY_Q),
            Shift('R', uinput.KEY_R),
            Shift('S', uinput.KEY_S),
            Shift('T', uinput.KEY_T),
            Shift('U', uinput.KEY_U),
            Shift('V', uinput.KEY_V),
            Shift('W', uinput.KEY_W),
            Shift('X', uinput.KEY_X),
            Shift('Y', uinput.KEY_Y),
            Shift('Z', uinput.KEY_Z)
        ])
