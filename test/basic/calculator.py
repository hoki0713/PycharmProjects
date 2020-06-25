class Model:
    def __init__(self):
        self._num1 = 0
        self._num2 = 0
        self._opcode = ''

    @property
    def num1(self) -> int: return self._num1

    @num1.setter
    def num1(self, num1): self._num1 = num1

    @property
    def num2(self) -> int: return self._num2

    @num2.setter
    def num2(self, num2): self._num2 = num2

    @property
    def opcode(self) -> str: return self._opcode

    @opcode.setter
    def opcode(self, opcode): self._opcode = opcode


class Controller:
    def __init__(self):
        pass

    def calc(self, num1, num2, opcode):
        model = Model()
        model.num1 = num1
        model.num2 = num2
        model.opcode = opcode

        service = Service(model)

        if opcode == '+': result = service.add()
        if opcode == '-': result = service.sub()
        if opcode == '/': result = service.div()
        if opcode == '*': result = service.multi()

        return result


class Service:
    def __init__(self, payload):
        self._num1 = payload.num1
        self._num2 = payload.num2
        pass

    def add(self):
        return self._num1 + self._num2

    def sub(self):
        return self._num1 - self._num2

    def div(self):
        return self._num1 / self._num2

    def multi(self):
        return self._num1 * self._num2


def print_menu():
    print('0. Exit')
    print('1. Calculator')
    return input('Menu\n')


while 1:
    menu = print_menu()
    if menu == '0': break
    if menu == '1':
        app = Controller()
        print('Run Calculator')
        num1 = int(input('First Number\n'))
        opcode = input('Operator\n')
        num2 = int(input('Second Number\n'))

        result = app.calc(num1, num2, opcode)
        print('Result: %d' % result)
