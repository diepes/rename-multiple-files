# Example replacement functions and usage, imports rename_files.py, 
# rename_functions files can be placed in different directories and reference rename_files.py
import sys
sys.path.insert(0, 'path-where-rename_files.py-is')
from rename_files import confirm_and_rename
import re


''' Replacement functions: '''
def dots_with_spaces(name):
    # if ' ' in name else name.replace(".", " ")
    return name.replace(".", " ")


def replace(name, *args):
    return name.replace(args[0], args[1])


def cap_sentence(s):
    return ' '.join(w[:1].upper() + w[1:] for w in s.split(' '))


def reorder(name):
    # orders tv shows with format s0e1
    try:
        title, ep, rest = re.split(r'(?: )(S0.*?)(?: )', name)  # uses spaces to match, but ignores them for result
        name = "{} {} {}".format(ep.lower(), title, rest)
    except Exception:
        print('** reordering "{}" failed'.format(f))
    return name


def remove_blu_ray(name):
    return name.replace("BluRay ", '').replace("Bluray ", '').replace('BRRip ', '')


confirm_and_rename(replace, 'a', "Test")
confirm_and_rename(dots_with_spaces)
confirm_and_rename(remove_blu_ray)
confirm_and_rename(cap_sentence)
confirm_and_rename(reorder)

