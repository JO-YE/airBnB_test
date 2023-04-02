#!/usr/bin/python3

from cmd import Cmd


class MyCmd(Cmd):
    def default(self, line):
        '''Command not recognized.'''
        print("Command not recognized: {}".format(line))

    def do_hello(self, arg):
        print("Hello", arg)

    def do_quit(self, arg):
        '''Quit command to exit the program.'''
        return True
    def do_EOF(self):
        '''End of file signal.'''
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    my_cmd = MyCmd()
    my_cmd.prompt = 'my_cmd> '
    my_cmd.cmdloop('Starting prompt...')
