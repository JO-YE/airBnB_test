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
        storage.save()

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
        else:
            obj_class = args[0]
            obj_id = args[1]
            obj_key = obj_class + '.' + obj_id
            attri_name = args[2]
            attri_value = args[3]
            obj = storage.all()[obj_key]

            if attri_value[0] == '"':
                attri_value = attri_value[1:-1] #slicing

            if hasattr(obj, attri_name): # checks if the object has an attribute
                type_value = type(getattr(obj, attri_name))
                # returns the value of the attribute
                if type_value in [str, float, int]:
                    attri_value = type_value(attri_value)
                    setattr(obj, attri_name, attri_value)
            else:
               setattr(obj, attri_name, attri_value)
            storage.save()

    def default(self, arg):
        '''Update your command interpreter to retrieve all instances
        of a class by using <class name>.all()
        '''
        args= arg.split('.')
        if args[0] in self.__classes:
            if args[1] == 'all()':
                self.do_all(args[0])
            elif args[1] == 'count()':
                stor = storage.all().items()
                lists = [v for k, v in stor if k.startswith(args[0])]
# startswith is an inbuilt fxn in python
                print(len(lists))
            elif args[1].startswith('show'):
                id_ = args[1].split('"')[1]
                self.do_show(f"{args[0]} {id_}")
            elif args[1].startswith('destroy'):
                id_d = args[1].split('"')[1]
                self.do_destroy(f"{args[0]} {id_d}")
            elif args[1].startswith('update'):
                split_ = args[1].split('(')
                split_ = split_[1].split(')')
                if '{' in split_[0]: # of a dic is present
                    split_ = split_[0].split(", {")
                    id_ = split_[0].strip('"')
                    dic_ = '{' + split_[1]
                    dic_ = eval(dic_)

                    for k, v in dic_.items():
                        self.do_update(f"{args[0]} {id_} {k} {v}")
                else:
                    # if no dic is passed
                    split_ = split_[0].split(", ")
                    id_ = split_[0].strip('"')
                    attr_name = split_[1].strip('"')
                    attr_value = split_[2].strip('"')

                    self.do_update(f"{args[0]} {id_} {attr_name} {attr_value}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
