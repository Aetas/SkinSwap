# Derek Prince

import io
# import os
import shutil # Used in favor of os because it will make+delete the file as opposed to rename/move for directories not shared on a single disk. os will fail.
import sys, getopt # command line arguments. Options, really.
# getopt vs argparse?
# argparse is probably a better choice but I prefer C so I might just stick with getopt


# CL parse
# check locations valid
# handle errors
# open the .ref file if necessary
# move shit
# update .ref
# close .ref
# echo completion?
# log?
# log. (append, don't overwrite)
