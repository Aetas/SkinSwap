# SkinSwap
A weird name - it's just for swapping texture files (skins) for a Vive wand. And an excuse to do file things in Python because I need practice. Python. Bleh.

The simplicity of this program makes me think a bash script would be faster and simpler to implement than Python but I should probably get the experience anyhow. Plus, lets be honest, I'd rather do this in C++ or Rust anyhow. Which is utterly overkill for this. (Maybe a good exercise in qt though...)

However, since I don't plan on ever using my Vive with steam on Linux (Steam targets Debian, not RHEL. Lots of hassle.) I have misgivings about fleshing out a full bash script with options. Plus, Python is excessively easy to use in a Linux environment so it's kinda stupid to do two implementations. Though bash is coming to Windows...

I kinda want to try layering python on top of c to sort startup commands purely because I can rather than I need to. Which is a classic "add features before you have a program" thing to do.

I might also use a settings file to load a user-defined file location. Might make the program needlessly fat though. Maybe a launch option to load settings file, otherwise default install location?
