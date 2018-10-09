import time
import os
import select
import re
import difflib
from itertools import zip_longest
import __main__


# os.chdir("enter path here")
print("Working path:", os.getcwd())


def color(text, which):
    # other type of coloring here (backgrounds only?) https://stackoverflow.com/a/21786287/3577695
    if which == 'test':     # print all colors, and exit function
        for i in range(1,100):
            print('\\033['+str(i)+'m' , '\033['+str(i)+'m' + 'xxxxx' + '\033[0m' )
        return

    options = {
       'red'        : '\033[31m',
       'green'      : '\033[32m',
       'yellow'     : '\033[93m',
       'blue'       : '\033[34m',
       'purple'     : '\033[95m',
       'cyan'       : '\033[96m',
       'darkcyan'   : '\033[36m',
       'bold'       : '\033[1m',
       'underline'  : '\033[4m',
       'END'        : '\033[0m',
    }
    return options[which] + text + options['END']


def color_print(c, *args):
    print(*[color(arg, c) for arg in args])


def print_diffs(name, new_name):
    """
    Prints file names, with differences colored
    :param name:
    :param new_name:
    :return:
    """
    d = difflib.Differ()
    result = list(d.compare([name], [new_name]))

    # for line in result:
    #     print(line)

    changes = [[name, ''], [new_name, '']]
    curr = -1
    for line in result:
        if curr == -1:
            curr += 1
            changes[curr][0] = line     # save string
        elif curr > -1:
            if line[0] in ['+', '-', ' ']:
                curr += 1
                changes[curr][0] = line     # save string
            else:
                changes[curr][1] = line          # save changes

    for i, change in enumerate(changes):
        ret = []
        for c, dif in zip_longest(change[0][2:], change[1][2:]):
            if c is None:
                c = ''
            if dif == '+' or [dif, i] == ['^', 1]:
                c = color(c, 'green')
            elif dif == '-' or [dif, i] == ['^', 0]:
                c = color(c, 'red')
            ret.append(c)
        print(''.join(ret))
    print()


def test_print_diffs():
    def test(name, a, b):
        color_print('yellow', name, '\n ', a, '\n ', b)
        print_diffs(a, b)

    print(color('testing print_diffs', 'purple'))

    test('equal (we never use this)',
         'hello there',
         'hello there')
    test('remove',
         'hello there@',
         'hello there')
    test('add',
         'hello there',
         '@hello there')
    test('change',
         'hello there@',
         'hello@@here ')
    test('remove and add',
         'hello there@',
         '@hello there')
    test('remove, add and change',
         'hello there@',
         '@hello@there')

#test_print_diffs()  , quit()


def process_files(new_name_handler, func, *args):
    """
    Finds changes in files, makes them or prints
    :param new_name_handler: name and new_name will be passed to this
    :param func: Used to get new_name
    :param args: arguments passed to func
    :return:
    """
    no_changes = True
    for file_name in os.listdir():
        # Extension if it's not a directory
        name, ext = os.path.splitext(file_name) if not os.path.isdir(file_name) else (file_name, '')
        if file_name == os.path.basename(__main__.__file__):  # skip this script
            continue
        new_name = func(name, *args)
        if name != new_name:
            new_name_handler(file_name, new_name+ext)
            no_changes = False
    return no_changes


def confirm_and_rename(func, *args):
    """
    Wrapper function to confirm if renaming should be done for changes by func
    :param func: function to be run, returns what replacement would be
    :param args: arguments that would be sent to func
    """
    color_print('yellow', '*** Running', func.__name__, *args if args else '')
    no_changes = process_files(print_diffs, func, *args)        # Print diffs
    if no_changes:
        print('Creates no changes')
    elif input('Make Changes? ') != 'y':
        print('No Changed Saved.')
    else:
        process_files(os.rename, func, *args)
        print('Replaced.')
    print()


def print_names():
    print('Files:')
    for file_name in os.listdir():
        if file_name == os.path.basename(__main__.__file__):  # skip this script
            continue
        print(file_name)
    print()


print_names()