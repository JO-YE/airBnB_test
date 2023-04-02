#!/usr/bin/python3
'''Contains the entry point of the command interpreter.'''
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''Command line-interpreter.'''
    prompt = '(hbnb) '
    __classes = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place',
                'Review']
# created a private class attribute to store the classes we have in our project.

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

    def do_create(self, arg):
        '''Creates a new instance according to the class given
        '''
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.__classes:
# refering to the class instance created
            print("** class doesn't exist **")
        else:
            class_name = args[0] # index 0
            new_obj = eval(class_name + "()")
            print(new_obj.id)

    def do_show(self, arg):
        '''Prints the string representation of an instance based
        on the class name and id.
        '''
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        elif f'{args[0]}.{args[1]}' not in storage.all():
            print('** no instance found **')
        else:
            print(storage.all()[f'{args[0]}.{args[1]}'])

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id
        '''
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        elif f'{args[0]}.{args[1]}' not in storage.all():
            print('** no instance found **')
        else:
            del storage.all()[f'{args[0]}.{args[1]}']
            storage.save()

    def do_all(self, arg):
        '''Prints all string representation of all instances based
        or not on the class name
        '''
        args = arg.split()
        if len(args) == 0:
            print([str(value) for value in storage.all().values()])
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            stor = storage.all().items()
            print([str(v) for k, v in stor if k.startswith(args[0])])

    def do_update(self, arg):
        '''Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file)
        '''
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        elif f'{args[0]}.{args[1]}' not in storage.all():
            print('** no instance found **')
        elif len(args) == 2:
            print('** attribute name missing **')
        elif len(args) == 3:
            print('** value missing **')
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
