# rename-multiple-files

# Function copied from public gist
# https://gist.github.com/aljgom/81e8e4ca9584b481523271b8725448b8


# Usage: example

 * Create python script that imports rename_files, and then add small function to take file name and return desired file name.
 
 
#!/bin/env python3
from rename_files import confirm_and_rename,test_print_diffs

def mv_9s_to_dir(name):
    ''' remove '9s-' from start of all files and directories '''
    if name.startswith('9s-'):
        return name[2:]
    else:
        return name

confirm_and_rename(mv_9s_to_dir) 
