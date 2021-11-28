#!/bin/env python3
from rename_files import confirm_and_rename,test_print_diffs

def mv_to_github(name):
    if name.startswith('github-') and name != 'github':
        return f"github/{name[7:]}"
    return name

def mv_9s_to_dir(name):
    if name.startswith('9s-'):
        return name[2:]
    else:
        return name

# test_print_diffs()
confirm_and_rename(mv_to_github)
confirm_and_rename(mv_9s_to_dir)