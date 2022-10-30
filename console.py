# !/usr/bin/env python3
""" A Command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program'
        exit()
    def do_EOF(self, arg):
        'EOF command to catch errors'
        print()
        return True
    def do_create(self, arg):
        'Creates a new instance of BaseModel Ex: `create BaseModel`'
        args = arg.split()
        if len(args) == 0:
            print('** class name missing **')
        elif args[0] != BaseModel.__name__:
            print("** class doesn't exist **")
        elif args[0] == BaseModel.__name__:
            new_obj = BaseModel()
            new_obj.save()
            print(new_obj.id)
        
    def do_emptyline(self, arg):
        pass
    
    def do_show(self, arg):
        ''' Prints the string representation of an instance based on 
            the class name and id. Ex: `show BaseModel 1234-1234-1234`
        '''
        args = arg.split()
        
        if len(args) == 0:
            print('** class name missing **')
            return
        elif args[0] != BaseModel.__name__:
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
        elif args[0] != BaseModel.__name__:
            print("** class doesn't exist **")
        if len(args) == 1:
           print('** instance id missing **')
           return
        
        key = f'{args[0]}.{args[1]}'
        req_instance = storage.all().pop(key, None)
        if req_instance == None:
            print('** no instance found **')
            return
        storage.save()
        
        
        
        
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()

