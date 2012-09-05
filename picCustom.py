'''
This Python script that allows you to quickly rename a large set of
images contained in the same directory.

Example:
- The images "asdf.jpg", "893t.jpg", etc... are in your directory.
- They are all images taken at the same concert.
- You can use this script to rename them "my_concert - 001.jpg",
"my_concert - 002.jpg", "my_concert - 003.jpg", etc...
'''

import os
import re
import shutil
import urllib

def getLocalPics(basedir):
	# Settings
	# - fixed image name = (newString + delim + count + typeOut)
	newString = "new_image"		# fixed image base string
	delim = ""				# delimiter
	count = 1				# image number
	pad = 2					# image number's zero padding
	typeIn = ".jpg" 			# filetype of images to fix
	typeOut = ".jpg" 			# filetype of fixed images
	
	# Work
	destDir = createFolder(basedir)
	dirContents = os.listdir(basedir)
	print "\nADDING NEW PICTURES:\n",
	for name in dirContents:
		match = re.search(r'.+(\.\w+)', name)
		if match and match.group(1) == typeIn:
			fixedName = newString + delim + format(count, "0%dd" % pad) + typeOut
			shutil.copy2(basedir + "\\" + name, destDir + "\\" + fixedName)
			print "  " + str(count) + ") " + fixedName
			count += 1
	print "\nTO FOLDER:\n  %s\n" % destDir


def createFolder(basedir):
	fixedDir = basedir + "\\fixed pics"
	if not os.path.isdir(fixedDir):
		os.mkdir(fixedDir)
		print "\nCREATING FOLDER TO STORE FIXED PICTURES:\n  %s\n" % fixedDir
	return fixedDir


if __name__ == "__main__":
	picDir = "C:\pic_customizer"	# directory containing the images to rename
	getLocalPics(picDir)
