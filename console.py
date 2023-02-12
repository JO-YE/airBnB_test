#!/usr/bin/python3
'''Contains the entry point of the command interpreter.'''
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    '''Command line-interpreter.'''
    prompt = '(hbnb) '
    __classes = ['BaseModel']

    def do_quit(self, arg):
        '''To exit the program.
        '''
        return True

    def do_EOF(self, arg):
        '''EOF signal to exit a program.
        '''
        return True

    def emptyline(self):
        '''For an emptyline.'''
        pass

    def do_create(self, agr):
        '''Creates a new instance according to the class given
        '''
        args = agr.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            new_obj = eval(class_name + "()")
            print(new_obj.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
