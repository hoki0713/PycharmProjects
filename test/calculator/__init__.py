from calculator.controller import Controller

if __name__ == '__main__':
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