#!/usr/bin/python3
"""
Unittests for the Console.py file
"""

import cmd
import pycodestyle
import unittest
import console
import sys
import os
from io import StringIO
from unittest.mock import patch
from models import storage
from models.engine.file_storage import FileStorage
HBNB = console.HBNBCommand


class TestConsole(unittest.TestCase):
    """
    Class to test Console class
    """
    def test_prompt(self):
        """
        Test for the prompt text of the console
        """
        self.assertEqual("(hbnb)", HBNB.prompt)

    def test_empty_line(self):
        """
        Test that no output exists with an empty line and enter
        """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_help_quit(self):
        """
        Test for help of the quit command
        """
        help_text = ("Typing <quit> will exit the console")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("help quit"))
            self.assertEqual(help_text, output.getvalue().strip())

    def test_help_EOF(self):
        """
        Test for help of the EOF command
        """
        help_text = ("Typing <EOF> will exit the console")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("help EOF"))
            self.assertEqual(help_text, output.getvalue().strip())

    def test_help_create(self):
        """
        Test for help of the create command
        """
        help_text = ("Typing <create class_name> will create a new object "
                     "of class class_name, will save it (to the JSON file) "
                     "and will print it's id")
        len_text = 135
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("help create"))
            self.assertEqual(len_text, len(output.getvalue().strip()))

    def test_help_show(self):
        """
        Test for help of the show command
        """
        help_text = ("Typing <show class_name object_id> prints the "
                     "string representation of the object")
        len_text = 89
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("help show"))
            self.assertEqual(len_text, len(output.getvalue().strip()))

    def test_help_destroy(self):
        """
        Test for help of the destroy command
        """
        help_text = ("Typing <destroy class_name object_id> deletes "
                     "that instance and save the change into the JSON file")
        len_text = 106
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("help destroy"))
            self.assertEqual(len_text, len(output.getvalue().strip()))

    def test_help_all(self):
        """
        Test for help of the all command
        """
        help_text = ("Typing <all class_name> prints the string "
                     "representation of all the objects of that "
                     "class. Typing <all> prints the string representation "
                     "of all objects")
        len_text = 167
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("help all"))
            self.assertEqual(len_text, len(output.getvalue().strip()))

    def test_help_update(self):
        """
        Test for help of the update command
        """
        help_text = ("Typing <update class_name object_id attribute_name "
                     "attribute_value> updates that instance by adding or"
                     "updating attribute (saves the change into the JSON"
                     "file). If the attribute value is an string, it must"
                     "be double quoted")
        len_text = 178
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("help update"))
            self.assertEqual(len_text, len(output.getvalue().strip()))

    def test_style_test(self):
        """
        Test if test_console.py passes the pycodestyle style
        """
        style = pycodestyle.StyleGuide()
        console_style_t = style.check_files(['tests/test_console.py'])
        self.assertEqual(console_style_t.total_errors, 0, "Does not com\
        ply with pycodestyle")

    def test_style(self):
        """
        Test if console.py passes the pycodestyle style
        """
        console_style = pycodestyle.StyleGuide().check_files(['console.py'])
        self.assertEqual(console_style.total_errors, 0, "Does not com\
        ply with pycodestyle")

    def test_methods_doc_exists(self):
        """
        Test if the methods in console.py have document\
        ation (test only if they exist)
        """
        self.assertIsNotNone(console.__doc__, "Console doc documentat\
        ion does not exists")
        self.assertIsNotNone(HBNB.do_quit.__doc__, "Console do_quit\
        Documentation does not exists")
        self.assertIsNotNone(HBNB.do_EOF.__doc__, "Console do_EOF\
        Documentation does not exists")
        self.assertIsNotNone(HBNB.emptyline.__doc__, "Console\
        do_emptyline Documentation does not exists")
        self.assertIsNotNone(HBNB.do_create.__doc__, "Console\
        do_create Documentation does not exists")
        self.assertIsNotNone(HBNB.do_show.__doc__, "Console do_show\
        Documentation does not exists")
        self.assertIsNotNone(HBNB.do_destroy.__doc__, "Console\
        do_destroy Documentation does not exists")
        self.assertIsNotNone(HBNB.do_all.__doc__, "Console do_all\
        Documentation does not exists")
        self.assertIsNotNone(HBNB.do_update.__doc__, "Console\
        do_update Documentation does not exists")
        self.assertIsNotNone(HBNB.default.__doc__, "Console default\
        Documentation does not exists")

    def test_methods_doc_length(self):
        """
        Test if the methods documentation in console.py have mo\
        re than 10 letters
        """
        n_con = len(console.__doc__)
        self.assertGreaterEqual(n_con, 10, "Console doc document\
        ation has less than 10 letters")
        n_con_quit = len(HBNB.do_quit.__doc__)
        self.assertGreaterEqual(n_con_quit, 10, "Console do_quit Document\
        ation has less than 10 letters")
        n_con_eof = len(HBNB.do_EOF.__doc__)
        self.assertGreaterEqual(n_con_eof, 10, "Console do_EOF Documentat\
        ion has less than 10 letters")
        n_con_emptyline = len(HBNB.emptyline.__doc__)
        self.assertGreaterEqual(n_con_emptyline, 10, "Console do_emptyline D\
        ocumentation has less than 10 letters")
        n_con_create = len(HBNB.do_create.__doc__)
        self.assertGreaterEqual(n_con_create, 10, "Console do_create Document\
        ation has less than 10 letters")
        n_con_show = len(HBNB.do_show.__doc__)
        self.assertGreaterEqual(n_con_show, 10, "Console do_show Document\
        ation has less than 10 letters")
        n_con_destroy = len(HBNB.do_destroy.__doc__)
        self.assertGreaterEqual(n_con_destroy, 10, "Console do_destroy Doc\
        umentation has less than 10 letters")
        n_con_all = len(HBNB.do_all.__doc__)
        self.assertGreaterEqual(n_con_all, 10, "Console do_all Document\
        ation has less than 10 letters")
        n_con_update = len(HBNB.do_update.__doc__)
        self.assertGreaterEqual(n_con_update, 10, "Console do_update Document\
        ation has less than 10 letters")
        n_con_default = len(HBNB.default.__doc__)
        self.assertGreaterEqual(n_con_default, 10, "Console default Document\
        ation has less than 10 letters")

    def test_HBNBCommand_class_doc_exists(self):
        """
        Test if the console HBNBCommand class in console.py have document\
        ation (test only if it exist)
        """
        self.assertIsNotNone(HBNB.__doc__, "Console HBNBCommand d\
        ocumentation does not exists")

    def test_HBNBCommand_doc_length(self):
        """
        Test if the HBNBCommand documentation in console.py has mo\
        re than 10 letters
        """
        n_con = len(HBNB.__doc__)
        self.assertGreaterEqual(n_con, 10, "Console HBNBCommand document\
        ation has less than 10 letters")

    def test_quit(self):
        """
        Test that the quit command exists
        """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNB().onecmd("quit"))

    def test_EOF(self):
        """
        Tests that the EOF command exists
        """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNB().onecmd("EOF"))

    def test_create_no_class(self):
        """
        Test the console create with no class
        """
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_create_bad_class(self):
        """
        Test the console create with bad class argument
        """
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create BadClass"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_show_no_class(self):
        """
        Test the console show with no class
        """
        expected = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_show_bad_class(self):
        """
        Test the console show with bad class argument
        """
        expected = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show BadClass"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_show_no_id(self):
        """
        Test the console show with User class and id argument missing
        """
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show User"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_show_bad_id(self):
        """
        Test the console show with User class and a bad id argument
        """
        expected = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show User BadUser"))
            self.assertEqual(expected, output.getvalue().strip())

    def test_create_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create User"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "User.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create State"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "State.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create City"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "City.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Amenity"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Amenity.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Place"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Place.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Review"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "Review.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())

    def test_show_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show"))
            self.assertEqual(correct, output.getvalue().strip())
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd(".show()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("MyModel.show()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_missing_id_space_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show BaseModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show User"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show State"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show City"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show Amenity"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show Place"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show Review"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_missing_id_dot_notation(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("BaseModel.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("User.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("State.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("City.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Amenity.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Place.show()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Review.show()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_no_instance_found_space_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show BaseModel 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show User 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show State 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show City 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show Amenity 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show Place 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("show Review 1"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_no_instance_found_dot_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("BaseModel.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("User.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("State.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("City.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Amenity.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Place.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Review.show(1)"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create BaseModel"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "show BaseModel {}".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create User"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(testID)]
            command = "show User {}".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create State"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(testID)]
            command = "show State {}".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Place"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(testID)]
            command = "show Place {}".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create City"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(testID)]
            command = "show City {}".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Amenity"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(testID)]
            command = "show Amenity {}".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Review"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(testID)]
            command = "show Review {}".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

    def test_show_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create BaseModel"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "BaseModel.show({})".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create User"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(testID)]
            command = "User.show({})".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create State"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(testID)]
            command = "State.show({})".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Place"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(testID)]
            command = "Place.show({})".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create City"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(testID)]
            command = "City.show({})".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Amenity"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(testID)]
            command = "Amenity.show({})".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Review"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(testID)]
            command = "Review.show({})".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertEqual(obj.__str__(), output.getvalue().strip())

    def test_destroy_missing_class(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("destroy"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd(".destroy()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_invalid_class(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("destroy MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("MyModel.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_id_missing_space_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("destroy BaseModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("destroy User"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("destroy State"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("destroy City"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("destroy Amenity"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("destroy Place"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("destroy Review"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_id_missing_dot_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("BaseModel.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("User.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("State.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("City.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Amenity.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Place.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Review.destroy()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_invalid_id_space_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("destroy BaseModel 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("destroy User 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("destroy State 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("destroy City 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("destroy Amenity 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("destroy Place 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("destroy Review 1"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_invalid_id_dot_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("BaseModel.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("User.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("State.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("City.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Amenity.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Place.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Review.destroy(1)"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_destroy_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create BaseModel"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "destroy BaseModel {}".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create User"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(testID)]
            command = "show User {}".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create State"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(testID)]
            command = "show State {}".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Place"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(testID)]
            command = "show Place {}".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create City"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(testID)]
            command = "show City {}".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Amenity"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(testID)]
            command = "show Amenity {}".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Review"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(testID)]
            command = "show Review {}".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertNotIn(obj, storage.all())

    def test_destroy_objects_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create BaseModel"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "BaseModel.destroy({})".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create User"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["User.{}".format(testID)]
            command = "User.destroy({})".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create State"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["State.{}".format(testID)]
            command = "State.destroy({})".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Place"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Place.{}".format(testID)]
            command = "Place.destroy({})".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create City"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["City.{}".format(testID)]
            command = "City.destroy({})".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Amenity"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Amenity.{}".format(testID)]
            command = "Amenity.destroy({})".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertNotIn(obj, storage.all())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Review"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["Review.{}".format(testID)]
            command = "Review.destory({})".format(testID)
            self.assertFalse(HBNB().onecmd(command))
            self.assertNotIn(obj, storage.all())

    def test_all_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("all MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("MyModel.all()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_all_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create BaseModel"))
            self.assertFalse(HBNB().onecmd("create User"))
            self.assertFalse(HBNB().onecmd("create State"))
            self.assertFalse(HBNB().onecmd("create Place"))
            self.assertFalse(HBNB().onecmd("create City"))
            self.assertFalse(HBNB().onecmd("create Amenity"))
            self.assertFalse(HBNB().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("all"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())

    def test_all_objects_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create BaseModel"))
            self.assertFalse(HBNB().onecmd("create User"))
            self.assertFalse(HBNB().onecmd("create State"))
            self.assertFalse(HBNB().onecmd("create Place"))
            self.assertFalse(HBNB().onecmd("create City"))
            self.assertFalse(HBNB().onecmd("create Amenity"))
            self.assertFalse(HBNB().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd(".all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())

    def test_all_single_object_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create BaseModel"))
            self.assertFalse(HBNB().onecmd("create User"))
            self.assertFalse(HBNB().onecmd("create State"))
            self.assertFalse(HBNB().onecmd("create Place"))
            self.assertFalse(HBNB().onecmd("create City"))
            self.assertFalse(HBNB().onecmd("create Amenity"))
            self.assertFalse(HBNB().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("all BaseModel"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("all User"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("all State"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("all City"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("all Amenity"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("all Place"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("all Review"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

    def test_all_single_object_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create BaseModel"))
            self.assertFalse(HBNB().onecmd("create User"))
            self.assertFalse(HBNB().onecmd("create State"))
            self.assertFalse(HBNB().onecmd("create Place"))
            self.assertFalse(HBNB().onecmd("create City"))
            self.assertFalse(HBNB().onecmd("create Amenity"))
            self.assertFalse(HBNB().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("User.all()"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("State.all()"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("City.all()"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Amenity.all()"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Place.all()"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Review.all()"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

    def test_update_missing_class(self):
        correct = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("update"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd(".update()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_invalid_class(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("update MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("MyModel.update()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_id_space_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("update BaseModel"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("update User"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("update State"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("update City"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("update Amenity"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("update Place"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("update Review"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_id_dot_notation(self):
        correct = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("BaseModel.update()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("User.update()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("State.update()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("City.update()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Amenity.update()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Place.update()"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Review.update()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_invalid_id_space_notation(self):
        correct = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("update BaseModel 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("update User 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("update State 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("update City 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("update Amenity 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("update Place 1"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("update Review 1"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_invalid_id_dot_notation(self):
        correct = "** no instance found **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("BaseModel.update(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("User.update(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("State.update(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("City.update(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Amenity.update(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Place.update(1)"))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Review.update(1)"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_attr_name_space_notation(self):
        correct = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create BaseModel"))
            testId = output.getvalue().strip()
            testCmd = "update BaseModel {}".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create User"))
            testId = output.getvalue().strip()
            testCmd = "update User {}".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create State"))
            testId = output.getvalue().strip()
            testCmd = "update State {}".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create City"))
            testId = output.getvalue().strip()
            testCmd = "update City {}".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Amenity"))
            testId = output.getvalue().strip()
            testCmd = "update Amenity {}".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Place"))
            testId = output.getvalue().strip()
            testCmd = "update Place {}".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_attr_name_dot_notation(self):
        correct = "** attribute name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create BaseModel"))
            testId = output.getvalue().strip()
            testCmd = "BaseModel.update({})".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create User"))
            testId = output.getvalue().strip()
            testCmd = "User.update({})".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create State"))
            testId = output.getvalue().strip()
            testCmd = "State.update({})".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create City"))
            testId = output.getvalue().strip()
            testCmd = "City.update({})".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Amenity"))
            testId = output.getvalue().strip()
            testCmd = "Amenity.update({})".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Place"))
            testId = output.getvalue().strip()
            testCmd = "Place.update({})".format(testId)
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd(testCmd))
            self.assertEqual(correct, output.getvalue().strip())


class TestHBNBCommand_count(unittest.TestCase):
    """
    Test count method of comand interpreter.
    """

    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_count_invalid_class(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("MyModel.count()"))
            self.assertEqual("0", output.getvalue().strip())

    def test_count_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create BaseModel"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("BaseModel.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create User"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("User.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create State"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("State.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Place"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Place.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create City"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("City.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Amenity"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Amenity.count()"))
            self.assertEqual("1", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNB().onecmd("Review.count()"))
            self.assertEqual("1", output.getvalue().strip())
