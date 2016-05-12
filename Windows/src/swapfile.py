# Derek Prince
# May 2016
import io
# import os
import shutil # Used in favor of os because it will make+delete the file as opposed to rename/move for directories not shared on a single disk. os will fail.
import sys # command line arguments. Options, really.
# getopt vs argparse?
# argparse is probably a better choice but I prefer C so I might just stick with getopt
# nevermind: optparse is love, optparse is life. Had a lovely tour of some parsing modules though.
from optparse import OptionParser
def main():
    parser = OptionParser(version="%prog 0.1")
    # I don't know why it took me so long to realize this is just OptionParser *parser = new OptionParser(). Without the actual pointer.
    parser.add_option("-f", "--file", action="store", type="string", dest="input_file", default="", help="name of file to swap", metavar="FILE")
    parser.add_option("-q", "--quiet", action="store_false", dest="verbose", default="True", help="Suppresses output") # might add ! for no logging
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default="True", help="Prints output")
    def restore(option, opt_str, value, parser):
        return
    parser.add_option("-r", "--restore", action="callback", callback=restore, help="restores default skin file") # keep copy or keep track of theirs? Would require checking .ref
    # a benefit of keeping track of .ref is that any Steam updates would be accounted for implicitly
    [...]
    # More than two required options is probably a pain in the ass. How to handle locations?
    # Default locations?
    # ../<skin>?
    # /dir/path/to/std/output/<outfile>?
    # outfile will always be the same since SteamVR doesn't actually support different skins and looks for one name.
    (options, args) = parser.parse_args()
    if len(args) < 1
        if options.input_file == "":
            parser.error("No input file found")
        else
            parser.error("No arguments supplied")
    [...]

if __name__ == "__main__":
    main()
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
