class VSC:

    def execute(self):
        print('Compiling')
        print('Running')


class MyEditors:

    def execute(self):
        print('Spell Check')
        print('Convention Check')
        print('Compiling')
        print('Running')


class Laptop:

    def __init__(self):
        print('Creating a new laptop')


    def code(self, ide):
        ide.execute()


ide = VSC()

lab1 = Laptop()

lab1.code(ide)