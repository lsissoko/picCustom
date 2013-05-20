
import os
import re
import shutil
import urllib

def renamePics(basedir):
	# Settings ( fixed image name = (newString + delim + count + typeOut) )
	newString = "new_image"			# fixed image base string
	delim = ""				# delimiter
	count = 1				# starting number for fixed images
	pad = 2					# zero padding for fixed image numbers
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
	renamePics("C:\pic_customizer")  # sub your own directory containing images to rename
