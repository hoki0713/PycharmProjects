from contacts.controller import Controller

if __name__ == '__main__':
    def print_menu():
        print('0. Exit')
        print('1. Add Contacts')
        print('2. Find by name')
        print('3. Show all list')
        print('4. Delete by name')
        return input('Menu\n')


    app = Controller()
    while 1:
        menu = print_menu()
        if menu == '1':
            app.register(input('이름\n'),
                         input('연락처\n'),
                         input('이메일\n'),
                         input('주소\n'))

        if menu == '2':
            print(app.search(input('이름\n')))

        if menu == '3':
            print(app.list())

        if menu == '4':
            app.remove(input('이름\n'))

        if menu == '0':
            break
