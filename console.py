#!/usr/bin/python3
"""This is the netry piont of my command interpreter"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.review import Review 
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.state import State 

class HBNBCommand(cmd.Cmd):
    """command interpreter for HBNB"""
    
    prompt = "(hbnb)"

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }


    def emptyline(self):
        """If the line is empty do nothing to it + ENTER"""
        pass
    
    def do_quit(self, arg):
        """quit command when you wnat to exit the program"""
        return True

    def do_EOF(SELF, arg):
        """this is a command you use if you want to exit the program"""
        print()
        return True

    def do_create(self, arg):
        """here we are creating a new instance of a class"""
        if not arg:
            print("** class name missing **")
            return
        
        args = arg.split()

        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[class_name]()
        new_instance.save()

        print(new_instance.id)

    def do_show(self, arg):
        """Show the string representation of an instance."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]

        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        print(objects[key])

    def do_destroy(self,arg):
        """deletes an instance based on the class name"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist**")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]

        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        del objects[key]
        storage.save()

    def do_all(self, arg):
        """prints all instances of a class"""
        objects = storage.all()

        if arg:
            args = arg.split()
            class_name = args[0]

            if class_name not in self.classes:
                print("** class doesn't exist **")
                return

            result = []

            for key, obj in objects.items():
                if key.startswith(class_name + "."):
                    result.append(str(obj))

            print(result)

        else:
            result = []

            for obj in objects.values():
                result.append(str(obj))

            print(result)

    def do_update(self, arg):
        """Update an instance with a new attribute value."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]

        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]

        instance = objects[key]

        old_value = getattr(instance, attribute_name, None)

        if isinstance(old_value, int):
            attribute_value = int(attribute_value)
        elif isinstance(old_value, float):
            attribute_value = float(attribute_value)

        setattr(instance, attribute_name, attribute_value)

        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
