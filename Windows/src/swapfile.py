# Derek Prince
# May 2016
# I have a poor understanding of Python's scope structure so this is rather spaghetti looking with definitions and variable locations
# At best I can say it follows RAII but it doesn't really take advantage of it.
# I might clean it up, I might not. Python doesn't do much for me, honestly. The best thing about it is optparse.
import io
import os, shutil # shutil is used because it plays nice with moving between disks
import sys # command line arguments. Options, really.
import datetime # for logging
# nevermind: optparse is love, optparse is life. Had a lovely tour of some parsing modules though.
from optparse import OptionParser
def main():
    parser = OptionParser(version="%prog 0.1")
    # I don't know why it took me so long to realize this is just OptionParser *parser = new OptionParser(). Without the actual pointer.
    parser.add_option("-f", "--file", action="store", type="string", dest="input_file", default="", help="name of file to swap", metavar="FILE")
    parser.add_option("-q", "--quiet", action="store_false", dest="verbose", default="True", help="Suppresses output") # might add ! for no logging
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default="True", help="Prints output")
    parser.add_option("--install_path", action="store", type="string", dest="install_loc", default="", help="set non-default SteamVR skin path", metavar="INSTALLDIR")
    parser.addoption("--source_path", action="store", type="string", dest="source_loc", default="",help="set non-default Skins folder path", metavar="SOURCEDIR")
    def restore(option, opt_str, value, parser):
        reference = open(".ref", "r+")
        log = open(".log", "a")
        last_texture = reference.read()
        if last_texture == "onepointfive_texture.PNG":
            return
        srcdir = os.getcwd() + '\\skins\\onepointfive_texture.PNG'
        shutil.copy2(srcdir, 'C:\\Program Files (x86)\\Steam\\SteamApps\\common\\SteamVR\\resources\\rendermodels\\vr_controller_vive_1_5\\onepointfive_texture.PNG')
        return

    parser.add_option("--restore", action="callback", callback=restore, help="restores default skin file") # keep copy or keep track of theirs? Would require checking .ref
    # a benefit of keeping track of .ref is that any Steam updates would be accounted for implicitly
    def clear(option, opt_str, value, parser):
        log = open(".log", "w")
        log.seek(0)
        log.truncate()
        return
    parser.add_option("--clear", action="callback", callback=clear, help="clears the log file")
    [...]
    # ../skins/<new_texture.PNG>?
    # "C:\\Program Files (x86)\\Steam\\SteamApps\\common\\SteamVR\\resources\\rendermodels\\vr_controller_vive_1_5\\onepointfive_texture.PNG
    # outfile will always be the same since SteamVR doesn't actually support different skins and looks for one name.
    (options, args) = parser.parse_args()
    if len(args) < 1:
        parser.error("No arguments supplied")
    [...]
    # start magic
    if options.file != "":
        log = open(".log", "a")
        log.write("\n\n %s", %datetime.now())
        reference = open(".ref", "r+")
        srcdir = os.getcwd() + '\\skins\\'
        if options.source_loc == "":
            options.source_loc = srcdir + options.file
        else:
            options.source_loc += '\\' + options.file # this is a bit static and dumb for my tastes but I'd rather have a functioning program to work with
        if options.install_loc == "":
            options.install_loc = 'C:\\Program Files (x86)\\Steam\\SteamApps\\common\\SteamVR\\resources\\rendermodels\\vr_controller_vive_1_5\\onepointfive_texture.PNG'
        # move the current texture
        dethroned_texture = reference.read()
        log.write("\n Texture in %s: %s" %(options.install_loc, dethroned_texture))
        dethroned_texture_path = srcdir + dethroned_texture
        shutil.move(options.install_loc, dethroned_texture_path)
        log.write("\n Moved %s to ./skins/" %dethroned_texture)
        # copy and rename new file to SteamVR texture location
        shutil.copy2(options.source_loc, options.install_loc)
        low.write("\n Moved %s to %s" %(options.source_loc, options.install_loc))
        # update .ref
        reference.write(options.file)
        reference.truncate()
        log.write("\n Updated reference file to contain %s" %options.file)
        # close files when done
        reference.close()
        log.close()

if __name__ == "__main__":
    main()
