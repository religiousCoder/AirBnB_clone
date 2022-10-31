#!/usr/bin/python3
"""This module defines the entry point of the command interpreter.

It defines one class, `HBNBCommand()`, which sub-classes the `cmd.Cmd` class.
This module defines abstractions that allows us to manipulate a powerful
storage system (FileStorage / DB). This abstraction will also allow us to
change the type of storage easily without updating all of our codebase.

It allows us to interactively and non-interactively:
    - create a data model
    - manage (create, update, destroy, etc) objects via a console / interpreter
    - store and persist objects to a file (JSON file)

Typical usage example:

    $ ./console
    (hbnb)

    (hbnb) help
    Documented commands (type help <topic>):
    ===========================================
    EOF  create show destroy update help  quit

    (hbnb)
    (hbnb) quit
    $
"""
import re
import cmd
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place

objects_dict = {'BaseModel': BaseModel, 'User': User, 'State': State,
                'City': City, 'Amenity': Amenity, 'Place': Place, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program'
        exit()

    def do_EOF(self, arg):
        'EOF command to catch errors'
        print()
        return True

    def emptyline(self, arg):
        """ Overides Cmd builtin emptyline method

        """
        pass

    def do_create(self, arg):
        'Creates a new instance of BaseModel Ex: `create BaseModel`'
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        get_obj = objects_dict.get(args[0], None)
        if get_obj is None:
            print("** class doesn't exist **")
            return
        new_obj = get_obj()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        ''' Prints the string representation of an instance based on 
            the class name and id. Ex: `show BaseModel 1234-1234-1234`
        '''
        args = arg.split()

        if len(args) == 0:
            print('** class name missing **')
            return
        get_obj = objects_dict.get(args[0], None)
        if get_obj is None:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print('** instance id missing **')
            return

        all_instance = storage.all()
        key = f"{args[0]}.{args[1]}"
        req_instance = all_instance.get(key, None)
        if req_instance is None:
            print('** no instance found **')
            return
        print(req_instance)

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id
           Ex: `destroy BaseModel 1234-1234-1234`
        '''
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        get_obj = objects_dict.get(args[0], None)
        if get_obj is None:
            print("** class doesn't exist **")
        if len(args) == 1:
            print('** instance id missing **')
            return

        key = f'{args[0]}.{args[1]}'
        del_instance = storage.all().pop(key, None)
        if del_instance == None:
            print('** no instance found **')
            return
        storage.save()

    def do_all(self, arg):
        'Prints all string representation of all instances'
        args = arg.split()
        if not len(args):
            instance = storage.all()
            print([str(instance[key])for key in instance])
            return
        else:
            get_obj = objects_dict.get(args[0], None)

        if get_obj is None:
            print("** class doesen't exist **")
            return
        instance = storage.all()
        print([str(instance[key]) for key in instance
               if key.split('.')[0] == get_obj.__name__])

    def do_update(self, arg):
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        get_obj = objects_dict.get(args[0], None)
        if get_obj is None:
            print("** class doesn't exist **")
        if len(args) == 1:
            print('** instance id missing **')
            return
        all_instance = storage.all()
        key = f'{args[0]}.{args[1]}'
        req_instance = all_instance.get(key, None)
        if req_instance is None:
            print('** no instance found **')
        if len(args) == 2:
            print('** attribute name missing **')
            return
        elif len(args) == 3:
            print('** value missing **')
            return
        pattern = re.compile(r'"')
        match_1 = pattern.findall(args[3])
        if match_1:
            args[3] = args[3].split('"')[1]
        if len(args) > 4:
            match_2 = pattern.findall(args[4])
            if match_1 and match_2:
                args[4] = args[4].split('"')[0]
                args[3] += ' ' + args[4]
        setattr(req_instance, args[2], args[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
