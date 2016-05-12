# Derek Prince

import io
# import os
import shutil # Used in favor of os because it will make+delete the file as opposed to rename/move for directories not shared on a single disk. os will fail.
import sys # command line arguments. Options, really.
# getopt vs argparse?
# argparse is probably a better choice but I prefer C so I might just stick with getopt
# nevermind: optparse is love, optparse is life. Had a lovely tour of some parsing modules though.
from optparse import OptionParser

parser = OptionParser()
# I don't know why it took me so long to realize this is just OptionParser *parser = new OptionParser(). Without the actual pointer.
parser.add_option("-i", "--input", dest="input_file", help="input file name", metavar="INFILE")
parser.add_option("-r", "--restore", help="restores default skin file") # keep copy or keep track of theirs? Would require checking .ref
parser.add_option("-q", "--quiet", action="store_false", dest="verbose", default="True")
# More than two required options is probably a pain in the ass. How to handle locations?
# Default locations?
# ../<inputfile>?
# /dir/path/to/std/output/<outfile>?
# outfile will always be the same since SteamVR doesn't actually support different skins and looks for one name.
(options, args) = parser.parse_args()


# CL parse
# check locations valid
# handle errors
# open the .ref file if necessary
# move shit
# update .ref
# close .ref
# echo completion?
# log?
# log. (append, don't overwrite. Maybe add an option to refresh logs for the crazy people. Then again they can just delete the file, another one will be created anyhow.)
