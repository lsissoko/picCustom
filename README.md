picCustom
=========

Python script that allows you to quickly copy and rename a large set of images.

I wrote this with concert and event pictures in mind but it would work for other filetypes.

#####Settings
- The `typeIn` variable lets you limit the target files to a single filetype
- The remaining variables will determine the new images' prefix: `newString + delim + count + typeOut`

#####Example
```
newString = "Logic14May2013"  # fixed image base string
delim = "_"                   # delimiter
count = 20                    # starting number for fixed images
pad = 2                       # zero padding for fixed image numbers
typeIn = ".jpg"               # filetype of images to fix
typeOut = ".jpg"              # filetype of fixed images
```

The settings above turn ["IMG001.jpg", "IMG002.png", "IMG003.jpg"] into ["Logic14May2013_20.jpg", "Logic14May2013_21.jpg"].
- Note that `typeIn = ".jpg"` kept the second image, a ".png" file, from being renamed.
